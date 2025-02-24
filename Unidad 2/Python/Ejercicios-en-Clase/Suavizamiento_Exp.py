import numpy as np
import matplotlib.pyplot as plt
import Metrica_de_error as errores
from PIL.ImageSequence import Iterator

#Analisis de sensibilidad de los parametros trata de ver como se comporta el algoritmo con diferentes valores en los parametros
def calc_suavizado_exponencial(serie, alfa):
    new_serie = np.zeros_like(serie)
    new_serie[0] = serie[0]
    for t in range(1, len(serie)):
        new_serie[t] = round(alfa * serie [t] + (1 - alfa) * new_serie[t-1],2)
    return new_serie
