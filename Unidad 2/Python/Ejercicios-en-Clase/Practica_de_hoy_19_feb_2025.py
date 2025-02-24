import numpy as np
import math
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller

import Limpieza_de_datos as lp

def leer_datos(archivo="24hrs.csv"):
    # Leemos el archivo como una lista
    with open(archivo, 'r') as file:
        data = [line.strip().split(',') for line in file.readlines()]
    return data


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

    #plt.boxplot(dataset)
    #plt.title("Boxplot basico")
    #plt.show()

    return lower_limit, upper_limit


def limpiar_datos(data):
    # Convertimos a lista de valores numericos
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
    datos_d1 = np.diff(n_vector)
    resultado_d1 = adfuller(datos_d1)
    print(f"p-valor con d=1: {resultado_d1[1]}")  # Si sigue p > 0.05, diferenciamos otra vez
    s_valor = []  # Para cada dia

    for i in range(1, len(vector)):
        n_valor = ARIMA(2,1,2)
        n_vector.append(n_valor)

        # vemos si prende o apaga
        if n_valor > 27.5:
            s_valor.append(f"{i}: Prender AC")
        else:
            s_valor.append(f"{i}: Apagar AC")

    return n_vector, s_valor




