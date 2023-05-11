
"""
ENTREGA FINAL HACK MX
RETO NDS 

EQUIPO: CYBERBOTS
ESCUELA: ITESM CEM
REALIZADO POR:
    ANA PATRICIA ISLAS MAINOU
    PAULO OGANDO GULIAS
    CESAR EMILIANO PALOME LUNA
    JOSE LUIS MADRIGAL SANCHEZ
"""

# IMPORTAR LIBRERIAS 
# Librerias para manejo de datos
import pandas as pd

# Librerias para machine learning
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

# Liberias para crear la red neuronal
import tensorflow
from tensorflow import keras
from tensorflow.keras import layers
# Importar la Liberia de Tensorflow Sequential que nos permite crear la red
from tensorflow.keras.models import Sequential
#Importar la Liberia que nos permite poner capas de neuronas
from tensorflow.keras.layers import Dense


# --------------------------------------------------------------------------
# PROGRAMA PRINCIPAL
# --------------------------------------------------------------------------

# Leer la base de datos de transacciones de tarjetas de credito
datos = pd.read_csv("creditcard.csv")

# Standardizzacion de los datos del monto
scaler = preprocessing.StandardScaler()
# Normalizacion de los montos de -1 a 1
datos["NORMALIZADO"] = scaler.fit_transform(datos["Amount"\
                                                  ].values.reshape(-1, 1))

# Borar las columnoas de tiempo y monto no normalizado
datos = datos.drop(["Amount", "Time"], axis = 1)

# La clase de y contiene si es fraude (1) o no (0)
y = datos.drop(["V1","V2","V3","V4","V5","V6","V7","V8","V9","V10","V11", \
                "V12","V13","V14","V15","V16","V17","V18","V19","V20","V21", \
                    "V22","V23","V24","V25","V26","V27","V28","NORMALIZADO"], \
               axis = 1)
# La clase de x tiene las transaccioens y el monto normalizado
X = datos.drop(["Class"], axis = 1)

# Crear conjuntos de entrenamiento y de pruebas
# El 70 % de los datos es para entrenar la red neuronal
# El 30 % de los datos es para probar la red neuronal
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size = 0.3, \
                                                   random_state = 0)

# Convertir los data frames de entradas a tensores de tensorflow
X_train = tensorflow.convert_to_tensor(X_train)
X_test = tensorflow.convert_to_tensor(X_test)
Y_train = tensorflow.convert_to_tensor(Y_train)
Y_test = tensorflow.convert_to_tensor(Y_test)


# CONSTRUCCION DE LA RED NEURONAL -------------------------------------------

#CREAR LA RED
# Creamos una lugar donde vamos a construir la red
modelo = tensorflow.keras.Sequential()

# Agreamos las capas de neuronas 
modelo.add(layers.Dense(29, activation="relu", name = "capa1"))
modelo.add(layers.Dense(16, activation="relu", name = "capa2"))
modelo.add(layers.Dense(8, activation="relu", name = "capa3"))
modelo.add(layers.Dense(1, activation="sigmoid", name = "capa4")) 

# CONSTRUIR LA RED Y REVIASR LA CONSTRUCCION
modelo.build((1,29)) # se le da una tupla con el tamano inicial de la capa
modelo.summary()


modelo.compile("adam",loss='binary_crossentropy',metrics = ["accuracy"])

# ENTRENAR LA RED ------------------------------------------------------------
print("\n")
print("\n")
print("ENTRENAMIENTO DE LA RED NEURONAL------------------------------------")
print("\n")
print("\n")

modelo.fit(X_train, Y_train, steps_per_epoch= 60, batch_size = 15, \
           epochs = 5, verbose=1)

print("\n")
print("\n")
print("PROBAR LA RED NEURONAL-----------------------------------------------")

score = modelo.evaluate(X_test, Y_test, steps = 1, verbose =1)
print("El error es de: " + str(score[0]))
print("La efectividad es de: " + str(round(score[1]*100,2)) +"%")
