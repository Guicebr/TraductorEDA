import random
from src.MyNodo import MyNodo


class MyMapa:

    def __init__(self, Nivel):
        assert isinstance(Nivel, int)
        if Nivel<0: Nivel = 0
        self.Nivel = Nivel
        self.LNodos = []
        self.LChar = []

    def inicializarMapa (self, entrada):
        for letra in entrada:
            if letra not in self.LChar:
                self.LChar.append(letra)
        print(self.LChar)
        tam = len(self.LChar)
        nivel = self.Nivel
        self.LNodos = MyNodo(tam)

        if(nivel > 0):

            #Tamaño de la entrada
            tame = len(entrada)
            #Para evitar problemas de desborddamiento añadimos caracteres según el nivel
            entrada = entrada + entrada[0:self.Nivel]

            for i in range(tame):
                fin = i+self.Nivel
                #print(entrada[i:fin])
                self.addDatos(self.LNodos, entrada[i:fin], self.Nivel)



    def crearNodo(self, nodo, nivel):
        #self.printLNodos(self.LNodos,self.Nivel)
        tam = len(self.LChar)
        if nivel <= 0:
            return 0
        else:
            for i in range(tam):
                nodo.Datos[i] = MyNodo(tam)
                self.crearNodo(nodo.Datos[i], nivel-1)
        return 0

    def addDatos(self, nodo, cad, nivel):
        if nivel < 2:
            pos = self.LChar.index(cad)
            nodo.Datos[pos] = nodo.Datos[pos] + 1
            nodo.SumD = nodo.SumD + 1
        else:
            pos = self.LChar.index(cad[0:1])
            if(type(nodo)!= type(nodo.Datos[pos])):
                nodo.Datos[pos] = MyNodo(len(self.LChar))
            self.addDatos(nodo.Datos[pos], cad[1:], nivel-1)

    def printLNodos(self, nodo, nivel):

        tam = len(self.LChar)
        if nivel == self.Nivel:
            print(nodo, "N ", nivel)
        if nivel <= 0:
            #print(self.LChar)
            #print(nodo.Datos)
            nodo.printNodo()
        else:
            for i in range(tam):
                print(nodo.Datos[i],"N ",nivel-1)
                self.printLNodos(nodo.Datos[i], nivel - 1)
        return 0

    def getNextChar(self, nodo, cad, nivel):

        nc = self.LChar[0]
        if nivel < 1:
            return self.LChar[nodo.getRNGiter()]
        else:
            pos = self.LChar.index(cad[0:1])
            nc = self.getNextChar(nodo.Datos[pos], cad[1:], nivel - 1)
        return nc

    def getRandomChar(self):
        return self.LChar[random.randrange(0, len(self.LChar))]


