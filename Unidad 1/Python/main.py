from P1_LECTURA_SENSORES import P1_LECTURA_SENSORES

if __name__ == "__main__":
    sensor = P1_LECTURA_SENSORES()
    M = 5

    matriz = sensor.generar_matriz(M)
    for i, (vector, vo) in enumerate(matriz):
        print(f"Vector {i+1}: {vector} - Valor objetivo: {vo}")

    sensor.guardar_csv(matriz, "practica1.csv")

