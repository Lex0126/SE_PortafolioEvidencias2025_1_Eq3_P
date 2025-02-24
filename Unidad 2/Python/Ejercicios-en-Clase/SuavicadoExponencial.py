import numpy as np
import matplotlib.pyplot as plt
#analisis de sensibilidad
def calc_suavizado_exponencial (serie,alfa):


    new_serie = np.zeros_like(serie)
    new_serie[0] =serie[0]
    for t in range(1,len(serie)):
        new_serie[t] = alfa *serie[t]+(1-alfa)*new_serie[t-1]
    return new_serie

datos = np.array([100,132,105,133,141,137,156,136,157,124,132,142])