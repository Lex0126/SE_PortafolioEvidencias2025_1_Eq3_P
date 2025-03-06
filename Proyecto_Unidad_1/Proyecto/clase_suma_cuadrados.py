import random as rnd
import serial
import time

class SumadeCuadrados:
    def __init__(self, minv, maxv, Vo,port ="COM6",baudrate = 9600,timeout=100,max_intentos =10 ):
        self.__min = minv
        self.__max = maxv
        self.__vO = Vo
        self.ser = serial.Serial(port, baudrate, timeout=timeout)
        self.max_intentos = max_intentos

    def crearVector(self, n):
        for i in range(self.max_intentos):
            if self.ser.in_waiting > 0: # esto verifica si hay datos disponibles en el puerto
                linea = self.ser.readline().decode('utf-8').strip()
                valores = linea.split("-") #separamos por guion por ejemplo "100-23-34-54" [100,23,34,54]
                if len(valores) == n:  # Verificamos que tengamos los 4 valores
                    return [int(v) for v in valores]
            print("LEYENDO VALORES...")
            time.sleep(1)  # Esperamos 1 segundo entre intentos para mejor lectura

        raise Exception("No se pudieron tomar suficiente valores") #por lo que lei funciona para que el programa no continua sin los datos de lectura
        #esto fue tomado por documentacion,

    def ValorObjetivo(self, V):
        va = sum([i**2 for i in V])
        return va

    def Poblacion(self, m, n):
        poblacion = [self.crearVector(n) for i in range(m)]
        return poblacion

    def ObtenerPadres(self, p, pop):
        padres = []
        temp = len(pop)-1
        for i in range(p):
            idx1 = idx2 = rnd.randint(0, temp)
            while idx1 == idx2:
                idx2 = rnd.randint(0, temp)
            obj_val1 = self.ValorObjetivo(pop[idx1])
            obj_val2 = self.ValorObjetivo(pop[idx2])
            self.__vO.append(obj_val1)
            if obj_val1 < obj_val2:
                padres.append(pop[idx1][:]) #Se busca el valor objetivo menor el cual sera agregado a la lista de padres
            #[:] realiza una copia independiente del valor en la posicion dada para que en futuros cambios no afecte directamente a la instancia original
            else:
                padres.append(pop[idx2][:])
        return padres
    def cruzaEnunPunto(self, parents):
        descendencia = []
        for i in range(0, len(parents), 2):
            if i + 1 < len(parents):
                padre1 = parents[i]
                padre2 = parents[i + 1]
                tamano = len(padre1)
                cruce = rnd.randint(1, tamano - 1)
                hijo = padre1[:cruce] + padre2[cruce:]
                descendencia.append(hijo)
        return descendencia

    def mutacion(self,descendencia, rm):
        for hijo in descendencia:
            for i in range(len(hijo)):
                r = rnd.randint(0,100)
                if r>rm:
                    hijo[i]= rnd.randint(self.__min, self.__max)
        return descendencia

    def seleccionAmbiental (self, descendencia, padres, n):
        seleccion = []
        aux = 0
        for i in range(len(descendencia)):
            seleccion.append(descendencia[i])
        for i in range(len(padres)):
            seleccion.append(padres[i])
        for i in range(len(seleccion)):
            num1  = self.ValorObjetivo(seleccion[i])
            seleccion[i].append(num1)
        seleccion.sort(key = lambda individuo : individuo[-1])
        for seleccionado in seleccion:
            seleccionado.pop(4)
        seleccion = seleccion[:n] #nos quedamos con los mejores N
        return seleccion
    def promedioVO(self): # SE UTILIZA COMO PARAMETRO DE PARO CUANDO LOS VALORES OBJETIVOS EN LA POBLACION SELECCIONADA SEA DE 5
        promedio = 0
        for i in range(len(self.__vO)):
            promedio += self.__vO[i]
        promedio /= len(self.__vO)
        return promedio