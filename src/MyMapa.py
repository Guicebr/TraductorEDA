import random
from src.MyNodo import MyNodo


class MyMapa:

    def __init__(self, Nivel):
        assert isinstance(Nivel, int)
        if Nivel < 0: Nivel = 0
        self.Nivel = Nivel
        self.LNodos = []
        self.LChar = []

    def inicializarMapa(self, entrada):
        for letra in entrada:
            if letra not in self.LChar:
                self.LChar.append(letra)
        print(self.LChar)
        tam = len(self.LChar)
        self.LNodos = MyNodo(tam)

        self.addEntrada(entrada)

    def addEntrada(self, entrada):
        if self.Nivel > 0:
            # Tamaño de la entrada
            tame = len(entrada)

            # Para evitar problemas de desborddamiento añadimos caracteres según el nivel
            entrada = entrada + entrada[0:self.Nivel]

            #print("Texto Entrada ", entrada)
            for i in range(tame):
                fin = i + self.Nivel
                # print(entrada[i:fin])
                self.addDatos(self.LNodos, entrada[i:fin], self.Nivel)

    def crearNodo(self, nodo, nivel):
        # self.printLNodos(self.LNodos,self.Nivel)
        tam = len(self.LChar)
        if nivel <= 0:
            return 0
        else:
            for i in range(tam):
                nodo.Datos[i] = MyNodo(tam)
                self.crearNodo(nodo.Datos[i], nivel - 1)
        return 0

    def addDatos(self, nodo, cad, nivel):
        # Si hemos llegado a la base del arbol añadimos los datos al nodo
        if nivel < 2:
            pos = self.LChar.index(cad)
            nodo.Datos[pos] = nodo.Datos[pos] + 1
            nodo.SumD = nodo.SumD + 1
        # Si estamos en algun nodo intermedio, creamos el nodo si no existe y avanzamos al siguiente nodo
        else:
            pos = self.LChar.index(cad[0:1])
            if type(nodo.Datos[pos]) != type(nodo):
                nodo.Datos[pos] = MyNodo(len(self.LChar))

            nodo.SumD += nodo.Datos[pos].SumD+1
            self.addDatos(nodo.Datos[pos], cad[1:], nivel - 1)

    def printLNodos(self, nodo, nivel):

        tam = len(self.LChar)
        print(nodo, "N ", nivel, nodo.SumD)
        for i in range(tam):
            if(type(nodo.Datos[i])==type(nodo)):
                print(nodo.Datos[i], "N ", nivel - 1)
                self.printLNodos(nodo.Datos[i], nivel - 1)

        return nodo.printNodo()

    def getNextChar(self, nodo, cad, nivel):
        nc = self.getRandomChar()
        if self.Nivel == 0:
            return self.getRandomChar()
        if nivel < 2:
            return self.LChar[nodo.getRNGiter()]
        else:
            pos = self.LChar.index(cad[0:1])
            if type(nodo.Datos[pos]) != type(nodo):
                return nc
            else:
                return self.getNextChar(nodo.Datos[pos], cad[1:], nivel - 1)

    def getRandomChar(self):
        return self.LChar[random.randrange(0, len(self.LChar))]
