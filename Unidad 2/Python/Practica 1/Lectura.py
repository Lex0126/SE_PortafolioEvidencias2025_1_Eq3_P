import serial as conn
import pandas as pd

class Lectura:
    def leer_arduino(self, puerto="COM4", baudrate=9600):
        with conn.Serial(port=puerto, baudrate=baudrate, timeout=1) as arduino:
            while True:
                try:
                    a = arduino.readline().decode('utf-8', errors='ignore').strip()
                    if a:
                        return [int(x) for x in a.split('-')]
                except (UnicodeDecodeError, ValueError):
                    continue

    def generar_matriz(self, n):
        return [self.leer_arduino() for i in range(n)]

    def calcular_desviacion(self, matriz):
        df = pd.DataFrame(matriz, columns=["V1", "V2", "V3", "V4", "V5", "V6"])


        df['Desviacion_Fila'] = df.std(axis=1, ddof=1)


        desviacion_columnas = df.std(axis=0, ddof=1).tolist()


        desviacion_fila = pd.DataFrame([desviacion_columnas], columns=[f'Desviacion_{col}' for col in df.columns])
        df = pd.concat([desviacion_fila, df], ignore_index=True)

        return df

    def guardar_matriz_csv(self, df, filename):
        df.to_csv(filename, index=False)
        print(f"Datos guardados en {filename}")



