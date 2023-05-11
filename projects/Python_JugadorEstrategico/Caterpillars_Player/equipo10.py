# ----------------------------------------------------------
# Project: Adversarial Caterpillars
#
# Date: 01-Dec-2022
# Authors:
#           A01745419 Jose Luis Madrigal Sanchez
#           A01745907 Jorge Isidro Blanco Martinez
# ----------------------------------------------------------
from dagor import JuegoOrugas, JugadorOrugas, \
    JugadorOrugasInteractivo, JugadorOrugasAleatorio


class JugadorOrugasEquipo10(JugadorOrugas):

    def heuristica(self, posicion):
        puntaje = 0
        simbolocontrario = self.contrario.simbolo
        if self.triunfo(posicion) == self.simbolo:
            return 1000
        if self.triunfo(posicion) == simbolocontrario:
            return -1000

        t = posicion[1]
        s = self.simbolo
        rens = self.juego.renglones
        cols = self.juego.columnas
        contrariomin = "f"
        simbolomin = "f"
        if s == "B":
            contrariomin = "n"
            simbolomin = "b"
        else:
            contrariomin = "b"
            simbolomin = "n"
        for r in range(rens):
            for c in range(cols):

                if t[r][c] == s:

                    if r == 0 or r == rens - 1:
                        puntaje += 30
                    if c == 0 or c == cols - 1:
                        puntaje += 30

                    renglon1 = r
                    renglon2 = r
                    columna1 = c
                    columna2 = c
                    obs1 = False
                    obs2 = False
                    obs3 = False
                    obs4 = False
                    if r == 0:
                        renglon1 = rens - 1
                    elif r == (rens - 1):
                        renglon2 = rens + 1
                    elif c == 0:
                        columna1 = cols - 1
                    elif c == (cols - 1):
                        columna2 = cols + 1
                    for i in range(renglon1, -1, -1):
                        if t[i][c] == " ":
                            puntaje += 50
                        else:
                            obs1 = True
                            if t[i][c] == contrariomin:
                                puntaje -= 51
                            elif t[i][c] == simbolocontrario:
                                puntaje += 10
                            break
                    if obs1 is False:
                        for i in range(rens, r, -1):
                            if t[i][c] == " ":
                                puntaje += 30
                            else:
                                obs1 = True
                                if t[i][c] == contrariomin:
                                    puntaje -= 51
                                elif t[i][c] == simbolocontrario:
                                    puntaje += 10
                                break
                    for i in range(renglon2, rens + 1):
                        if t[i][c] == " ":
                            puntaje += 50
                        else:
                            obs2 = True
                            if t[i][c] == contrariomin:
                                puntaje -= 51
                            elif t[i][c] == simbolocontrario:
                                puntaje += 10
                            break
                    if obs2 is False:
                        for i in range(0, r):
                            if t[i][c] == " ":
                                puntaje += 30
                            else:
                                obs2 = True
                                if t[i][c] == contrariomin:
                                    puntaje -= 51
                                elif t[i][c] == simbolocontrario:
                                    puntaje += 10
                                break

                    for i in range(columna1, -1, -1):
                        if t[r][i] == " ":
                            puntaje += 50
                        else:
                            obs3 = True
                            if t[r][i] == contrariomin:
                                puntaje -= 51
                            elif t[r][i] == simbolocontrario:
                                puntaje += 10
                            break
                    if obs3 is False:
                        for i in range(cols + 1, c, -1):
                            if t[r][i] == " ":
                                puntaje += 30
                            else:
                                obs3 = True
                                if t[r][i] == contrariomin:
                                    puntaje -= 51
                                elif t[r][i] == simbolocontrario:
                                    puntaje += 10
                                break

                    for i in range(columna2, cols + 1):
                        if t[r][i] == " ":
                            puntaje += 50
                        else:
                            obs4 = True
                            if t[r][i] == contrariomin:
                                puntaje -= 51
                            elif t[r][i] == simbolocontrario:
                                puntaje += 10
                            break
                    if obs4 is False:
                        for i in range(0, c):
                            if t[r][i] == " ":
                                puntaje += 30
                            else:
                                obs4 = True
                                if t[r][i] == contrariomin:
                                    puntaje -= 51
                                elif t[r][i] == simbolocontrario:
                                    puntaje += 10
                                break
                    # Verificar localidad de arriba
                    if r > 0:
                        if t[renglon1][c] == contrariomin:
                            puntaje -= 30
                        elif t[renglon1][c] == simbolocontrario:
                            puntaje -= 100
                        elif t[renglon1 - 1][c] == simbolocontrario \
                                or t[renglon1 - 1][c] == contrariomin:
                            puntaje += 200

                    # Verificar localid de abajo
                    if r < rens - 1:
                        if t[renglon2][c] == contrariomin:
                            puntaje -= 30
                        elif t[renglon2][c] == simbolocontrario:
                            puntaje -= 100
                        elif t[renglon2 + 1][c] == simbolocontrario \
                                or t[renglon2 + 1][c] == contrariomin:
                            puntaje += 200

                    # Verificar localidad de la izquierda
                    if c > 0:
                        if t[r][columna1] == contrariomin:
                            puntaje -= 30
                        elif t[r][columna1] == simbolocontrario:
                            puntaje -= 100
                        elif t[r][columna1 - 1] == simbolocontrario \
                                or t[r][columna1 - 1] == contrariomin:
                            puntaje += 200

                    # Verificar localidad de la derecha
                    if c < cols - 1:
                        if t[r][columna2] == contrariomin:
                            puntaje -= 30
                        if t[r][columna2] == simbolocontrario:
                            puntaje -= 100
                        elif t[r][columna2 + 1] == simbolocontrario \
                                or t[r][columna2 + 1] == contrariomin:
                            puntaje += 200
        return puntaje

    def minimax(self, posicion, maximizing, max_depth=6):
        # Base case – terminal position or maximum depth reached
        if self.triunfo(posicion) or max_depth == 0:
            return self.heuristica(posicion)
        # Recursive case - maximize your gains or minimize the opponent's gains
        if maximizing:
            best_eval: float = float("-inf")  # arbitrarily low starting point
            for move in self.posiciones_siguientes(posicion):
                result: float = self.minimax(move, False, max_depth - 1)
                best_eval = max(result, best_eval)
            return best_eval
        else:  # minimizing
            worst_eval: float = float("inf")
            for move in self.posiciones_siguientes(posicion):
                result = self.minimax(move, True, max_depth - 1)
                worst_eval = min(result, worst_eval)
            return worst_eval

    def tira(self, posicion):
        '''Busca el mejor tiro entre todos los posibles.'''
        posibles = self.posiciones_siguientes(posicion)
        mp = posibles[0]
        mh = self.minimax(mp, True)
        for p in posibles[1:]:
            h = self.minimax(p, True)
            if h > mh:
                mh = h
                mp = p
        return mp


if __name__ == '__main__':
    juego = JuegoOrugas(
        JugadorOrugasEquipo10('Equipo 10'),
        JugadorOrugasAleatorio('RandomBoy'),
        4, 4)
    juego.inicia(veces=100, delta_max=2)
