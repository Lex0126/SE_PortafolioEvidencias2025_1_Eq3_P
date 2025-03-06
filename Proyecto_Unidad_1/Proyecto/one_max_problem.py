import random as rnd
import serial
import time

class onemaxproblem:
    def __init__(self, Vo, port="COM6", baudrate=9600, timeout=100, max_intentos=10):
        self.__vO = Vo  # Almacena los valores objetivos
        self.ser = serial.Serial(port, baudrate, timeout=timeout)
        self.max_intentos = max_intentos

    def crearVector(self, n):
        for i in range(self.max_intentos):
            if self.ser.in_waiting > 0:
                linea = self.ser.readline().decode('utf-8').strip()
                valores = linea.split("-")
                if len(valores) == n:
                    return [int(v) for v in valores]
            print("LEYENDO VALORES...")
            time.sleep(1)
        raise Exception("No se pudieron tomar suficientes valores")

    def ValorObjetivo(self, V):
        va = sum(abs(i) for i in V)  # Minimizar la suma absoluta de los valores
        return va

    def Poblacion(self, m, n):
        poblacion = [self.crearVector(n) for i in range(m)]
        return poblacion

    def ObtenerPadres(self, p, pop):
        padres = []
        temp = len(pop) - 1
        for i in range(p):
            idx1 = idx2 = rnd.randint(0, temp)
            while idx1 == idx2:
                idx2 = rnd.randint(0, temp)
            obj_val1 = self.ValorObjetivo(pop[idx1])
            obj_val2 = self.ValorObjetivo(pop[idx2])
            self.__vO.append(obj_val1)
            if obj_val1 < obj_val2:
                padres.append(pop[idx1][:])
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

    def mutacion(self, descendencia, rm):
        for hijo in descendencia:
            for i in range(len(hijo)):
                r = rnd.randint(0, 100)
                if r > rm:
                    hijo[i] = rnd.randint(0, 0)  # Mutacion hacia valores mas cercanos a 0
        return descendencia

    def seleccionAmbiental(self, descendencia, padres, n):
        seleccion = []
        for i in range(len(descendencia)):
            seleccion.append(descendencia[i])
        for i in range(len(padres)):
            seleccion.append(padres[i])
        for i in range(len(seleccion)):
            num1 = self.ValorObjetivo(seleccion[i])
            seleccion[i].append(num1)
        seleccion.sort(key=lambda individuo: individuo[-1])
        for seleccionado in seleccion:
            seleccionado.pop()
        seleccion = seleccion[:n]
        return seleccion

    def promedioVO(self):
        promedio = sum(self.__vO) / len(self.__vO) if self.__vO else 1
        return promedio

