import serial as conn
import csv

class P1_LECTURA_SENSORES:
    def leer_arduino(self):
        arduino = conn.Serial(port="COM4", baudrate=9600, timeout=1)
        while True:
            a = arduino.readline().decode().strip()
            if a:
                try:
                    valores = [int(x) for x in a.split('-')]
                    return valores
                except ValueError:
                    pass

    def generar_vector(self):
        V = self.leer_arduino()
        vo = self.valor_objetivo(V)
        return V, vo

    def valor_objetivo(self, vector):
        return sum(x ** 2 for x in vector)

    def generar_matriz(self, M):
        matriz = [self.generar_vector() for _ in range(M)]
        return matriz

    def guardar_csv(self, matriz, archivo_csv):
        with open(archivo_csv, "w", newline="") as f:
            writer = csv.writer(f)
            headers = [f"Valor {i+1}" for i in range(len(matriz[0][0]))] + ["Valor Objetivo (VO)"]
            writer.writerow(headers)
            for vector, vo in matriz:
                writer.writerow(vector + [vo])
        print(f"Población guardada en '{archivo_csv}'")





















