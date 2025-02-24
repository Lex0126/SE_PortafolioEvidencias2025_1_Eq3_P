import numpy as np
import math
import matplotlib.pyplot as plt


def leer_datos(archivo="SegundaLectura.csv"):
    with open(archivo, 'r') as file:
        data = [line.strip().split(',') for line in file.readlines()]

    # Extraer solo la columna de temperatura
    temperaturas = [float(row[1]) if row[1] != '' else '' for row in data[1:]]
    return temperaturas


def calcular_iqr(dataset):
    #metodo que dio el doctor
    dataset.sort()
    posQ1 = 1 * (len(dataset) - 1) / 4 + 1
    posQ3 = 3 * (len(dataset) - 1) / 4 + 1

    def interpolar(pos, data):
        p_decimal, p_entera = math.modf(pos)
        p_entera = int(p_entera)
        return data[p_entera - 1] + p_decimal * (data[p_entera] - data[p_entera - 1])

    Q1 = interpolar(posQ1, dataset)
    Q3 = interpolar(posQ3, dataset)

    IQR = Q3 - Q1
    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    print(f"Limite IQR: Inferior = {lower_limit}, Superior = {upper_limit}")
    return lower_limit, upper_limit


def interpolar_lineal(data):
    for i in range(len(data)):
        if data[i] == '':
            if 0 < i < len(data) - 1:
                data[i] = data[i - 1] + ((data[i + 1] - data[i - 1]) / ((i + 1) - (i - 1))) * (i - (i - 1))
            elif i == 0:  # Si el primer dato falta, copia el siguiente
                data[i] = data[i + 1]
            elif i == len(data) - 1:  # Si el ultimo dato falta, copia el anterior
                data[i] = data[i - 1]
    return data



def limpiar_datos(data):
    column_data = [float(row) if row != '' else '' for row in data]
    column_data = interpolar_lineal(column_data)

    plt.boxplot(column_data)
    plt.title("Ver outliers")
    plt.show()

    lower_limit, upper_limit = calcular_iqr(column_data)

    datos_limpios = column_data.copy()
    for i in range(len(column_data)):
        if column_data[i] < lower_limit or column_data[i] > upper_limit:
            if 0 < i < len(column_data) - 1:
                datos_limpios[i] = (column_data[i - 1] + column_data[i + 1]) / 2
            elif i == 0:
                datos_limpios[i] = column_data[i + 1]
            elif i == len(column_data) - 1:
                datos_limpios[i] = column_data[i - 1]

    return datos_limpios


def proc_ses(vector, alfa=0.7):
    n_vector = [vector[0]]  # Ya es float
    for i in range(1, len(vector)):
        n_valor = alfa * vector[i] + (1 - alfa) * n_vector[i - 1]
        n_vector.append(n_valor)
    return n_vector

