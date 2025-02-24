import numpy as np
import math
import matplotlib.pyplot as plt

def leer_datos():
    # ya no funciona con esto
    pass

def calcular_iqr(dataset):
    dataset.sort()

    # Posiciones de Q1 y Q3
    posQ1 = 1 * (len(dataset) - 1) / 4 + 1
    posQ3 = 3 * (len(dataset) - 1) / 4 + 1

    p_decimal, p_entera = math.modf(posQ1)
    p_entera = int(p_entera)
    Q1 = dataset[p_entera - 1] + p_decimal * (dataset[p_entera] - dataset[p_entera - 1])

    p_decimal, p_entera = math.modf(posQ3)
    p_entera = int(p_entera)
    Q3 = dataset[p_entera - 1] + p_decimal * (dataset[p_entera] - dataset[p_entera - 1])

    IQR = Q3 - Q1
    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    return lower_limit, upper_limit

def limpiar_datos(data):
    # Aqui hacemos que data sean los 24 que estamos leyendo desde arduino
    # Convertimos nuestra lista leida en valores numericos
    column_data = [float(row[0]) for row in data]

    # Rellenar vacíos
    for i in range(1, len(column_data) - 1):
        if column_data[i] == '' and i != 0 and i != len(column_data) - 1:
            column_data[i] = column_data[i - 1] + (
                    (column_data[i + 1] - column_data[i - 1]) / ((i + 1) - (i - 1))) * (i - (i - 1))

    # Identificar outliers con IQR manual
    lower_limit, upper_limit = calcular_iqr(column_data)
    datos_limpios = [row for row in data if float(row[0]) >= lower_limit and float(row[0]) <= upper_limit]

    return datos_limpios

def proc_ses(vector, alfa=0.7, dia=1):
    n_vector = [float(vector[0])]
    s_valor = []  # Para cada día

    for i in range(1, len(vector)):
        n_valor = alfa * (vector[i] + (1 - alfa) * n_vector[i - 1])
        n_vector.append(n_valor)

        # vemos si prende o apaga
        if n_valor > 30.5:
            s_valor.append(f"{i}: Prender AC")
        else:
            s_valor.append(f"{i}: Apagar AC")

    return n_vector, s_valor
