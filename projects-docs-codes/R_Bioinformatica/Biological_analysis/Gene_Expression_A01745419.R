#Alan Josué Melgar Fuentes A01752228
#Christian Parrish Gutiérrez Arrieta A01751584
#Jorge Isidro Blanco Martínez A01745907
#José Luis Madrigal Sánchez	 A01745419

#Lectura de archivos
library(GEOquery)
library(limma)
library(umap)
#knitr::opts_chunk$set(echo = TRUE)
#Lectura del conjunto de datos
gset <- getGEO("GSE40967", GSEMatrix =TRUE, AnnotGPL=TRUE)
if (length(gset) > 1) idx <- grep("GPL570", attr(gset, "names")) else idx <- 1
gset <- gset[[idx]]

#Se obtienen los valores de expresion
ex <- exprs(gset)

#Se convierte a data frame
ex <- as.data.frame(ex)
probes <- getEAWP(gset)$probes

#Division de los grupos
muestras_cancer_hombres <- exprs(gset[,gset$`Sex:ch1`=="Male"])
muestras_cancer_mujeres <- exprs(gset[,gset$`Sex:ch1`=="Female"])

#Creacion de un micro arreglo
microarray <- cbind(muestras_cancer_hombres,muestras_cancer_mujeres)

#Normalizacion de los datos
raw_means <- apply(microarray,2,mean,trim=0.02)
microarray_norm <- sweep(microarray, 2, raw_means, "/") * 100

#Obtencion de las medias
means_cancer_hombres <- rowMeans(microarray_norm[,1:322])
means_cancer_mujeres <- rowMeans(microarray_norm[,323:585])
microarray_means = data.frame(means_cancer_hombres,means_cancer_mujeres)

#Calculo de las proporciones
ratios <- microarray_means$means_cancer_hombres / microarray_means$means_cancer_mujeres
microarray_ratios = data.frame(ratios)
row.names(microarray_ratios) = row.names(microarray)

#Cambiar a log2                                         
microarray_norm = log2(microarray_norm)
microarray_norm <- na.omit(microarray_norm)
microarray_means = log2(microarray_means)
microarray_ratios = log2(microarray_ratios)

#t-test
get_pvalue <- function(values, idx1, idx2) {
return(t.test(values[idx1], values[idx2])$p.value)}
genero_p <- apply(microarray_norm, 1, get_pvalue, 1:322, 323:585)

#Seleccion de genes con p < 0.001
filtrado_p_genero <- genero_p[genero_p < 0.001]
filtrado_p_genero = sort(filtrado_p_genero)
filtrado_p_genero = as.data.frame(filtrado_p_genero)

#Nombre de la sonda
sondas = probes$ID

#Nombre del gen asociado
genes = probes$`Gene symbol`
combinado = cbind(genes, sondas)
combinado = as.data.frame(combinado)

library(dplyr)

#Calculo de los genes sobreexpreados y menos expresados
squanchy = as.vector(row.names(filtrado_p_genero))
squanchy1 = filter(combinado, as.character(sondas) %in% squanchy)
squanchy1 = squanchy1[match(squanchy, squanchy1$sondas),]

squanchy2 = filter(microarray_ratios, as.character(sondas) %in% squanchy)
squanchy2 = squanchy2[match(squanchy, squanchy1$sondas),]

almacen = row.names(filtrado_p_genero)
filtrado_p_genero = cbind(squanchy1$genes,squanchy2,filtrado_p_genero)
filtrado_p_genero = as.data.frame(filtrado_p_genero)

row.names(filtrado_p_genero) = squanchy

#Plots
#Genes "LOC389906", "GAGE1", "RPS4X", "JPX", "CLUHP3", "ALG13", "MYEF2", "POF1B", "KLC2", "COLGALT2".
m = microarray_norm
n_genes = c("LOC389906", "GAGE1", "RPS4X", "JPX", "CLUHP3", "ALG13", "MYEF2", "POF1B", "KLC2", "COLGALT2")
n_sondas = c("1569629_x_at", "208283_at", "213347_x_at", "1554447_at", "238910_at",
             "219015_s_at", "232676_x_at", "1555382_at", "218906_x_at", "209883_at")

# Mapa de calor y dendograma
microarray_selection = m[n_sondas,313:332]
row.names(microarray_selection) = n_genes
  

medias <- rowMeans(microarray_selection)
devs = apply(microarray_selection, 1, sd)

centered_filtrado = sweep(microarray_selection, 1, medias)
centered_filtrado = sweep(centered_filtrado, 1, devs, "/")

names(centered_filtrado) = c("Hombres", "Mujeres")
hclustering = hclust(dist(centered_filtrado))

plot(hclustering)
names(microarray_selection) = c("Hombres", "Mujeres")

heatmap(as.matrix(centered_filtrado), Colv = NA)

# Gráfica de dispersión
plot(microarray_means$means_cancer_hombres, 
     microarray_means$means_cancer_mujeres, 
     xlim = c(0,16), ylim = c(0,16),
     xaxt="n", yaxt="n",
     main = "Expression in Colon Cancer: Cancer Hombres vs Mujeres",
     xlab = "Hombres (log2 expression value)",
     ylab = "Mujeres (log2 expression value)")
axis(1, at=seq(0,16,2))
axis(2, at=seq(0,16,2))

abline(lm(microarray_means$means_cancer_hombres ~ microarray_means$means_cancer_mujeres),
       col = "red")

# Gráfica R-I
plot(microarray_means$means_cancer_hombres + microarray_means$means_cancer_mujeres,
     microarray_means$means_cancer_hombres - microarray_means$means_cancer_mujeres,
     main = "Expression in Colon Cancer: Cancer Hombres vs Mujeres",
     xlab = "Hombres (log2 expression value)",
     ylab = "Mujeres (log2 expression value)")

# Gráfica de volcán

colores = rep(1, length(genero_p))
colores[genero_p < 0.001 & microarray_ratios$ratios < -1] = 2
colores[genero_p < 0.001 & microarray_ratios$ratios > 1] = 3

plot(microarray_ratios$ratios,genero_p, col = colores,
     log = "y", ylim = rev(range(genero_p)),
     main = "Genero volcano plot",
     xlab = "log2 expression ratio: Hombres vs Mujeres",
     ylab = "p-value")