import serial as conn
import pandas as pd
from datetime import datetime
import time


class Lectura:
    def __init__(self):
        self.arduino = conn.Serial(port="COM6", baudrate=9600, timeout=100)

    def leer_arduino(self):
        while True:  # basicamente leemos los bytes del arduino que es el a, lo decodificamos y eliminamos los espacios en blanco
            #convertimos esa cadena en float para guardalos en una lista y retornamos la lista

            a = self.arduino.readline()
            try:
                a = a.decode('utf-8').strip()
            except UnicodeDecodeError:
                print("Error de decode")
                continue
            try:

                V = [float(a)]
            except ValueError:
                print("Valor no valido:", a)
                continue
            return V
    #recolecta n valores de arduino, agregamos tiempo por cada lectura, imprime el valor leido y espera 5 minutos para cada lecturra
    def generar_Vector(self, n):
        vectores = []
        for x in range(n):
            V = self.leer_arduino()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            vectores.append([timestamp] + V)
            print(f"Vector {x + 1}: {vectores[-1]}")
            time.sleep(300)
        return vectores

    def guardar_vectores_csv(self, vectores, filename):
        df = pd.DataFrame(vectores, columns=["FechaHora", "Temperatura"])
        df.to_csv(filename, index=False)
        # Imprimir cada fila leida
        for index, row in df.iterrows():
            print(f"Fila {index + 1}: Fecha y Hora: {row['FechaHora']} - Temperatura: {row['Temperatura']}")
