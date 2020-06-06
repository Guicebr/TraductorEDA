import random
class MyNodo:

    def __init__(self, tam):
        self.Id = -1
        self.Tam = tam
        self.Datos = []
        self.SumD = 0
        i = 0
        for i in range(self.Tam):
            self.Datos.append(1)
            self.SumD = self.SumD + 1

    def printNodo(self):
        print(self.Datos, "SumD ", self.SumD)

    def getRNGiter(self):

        if self.SumD == len(self.Datos):
            i = random.randrange(0, len(self.Datos))
            print(self.Datos, " i ", i)
            return i

        num = random.randrange(0, self.SumD+1)

        """s = 0
        for i in range(len(self.Datos)):
            s += self.Datos[i]

        print("num=", num, "sumD=", self.SumD, "sumD Real=",s)"""
        sum = 0
        for i in range(len(self.Datos)):
            sum = sum + self.Datos[i]
            if sum >= num:
                print(self.Datos, "rngn ", num, " i ", i)
                return i

        print("Err getRNGiter")
        return 0