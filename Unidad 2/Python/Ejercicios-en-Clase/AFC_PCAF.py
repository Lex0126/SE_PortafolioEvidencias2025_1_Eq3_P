import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import Limpieza_de_datos as lp

# Datos originales
f = open("SegundaLectura.csv", "r")
datos = []
datos = lp.limpiezaDatos(f, datos)

# Diferenciaciones
datos_d1 = np.diff(datos)
datos_d2 = np.diff(datos_d1)

# Graficamos ACF y PACF de la serie diferenciada (d=2)
plt.figure(figsize=(12,5))

ax1=plt.subplot(121)
plot_acf(datos_d1, lags=6, ax=ax1)  # ACF para identificar q

ax2=plt.subplot(122)
plot_pacf(datos_d1, lags=6, ax=ax2)  # PACF para identificar p

plt.tight_layout()
plt.show()
