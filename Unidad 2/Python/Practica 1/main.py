import Lectura as opt

if __name__ == "__main__":
    lectura = opt.Lectura()
    n = 100  # Número de lecturas
    matriz = lectura.generar_matriz(n)
    df = lectura.calcular_desviacion(matriz)
    lectura.guardar_matriz_csv(df, "Permutacion_1.csv")

