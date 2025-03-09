import Practica_4
import matplotlib.pyplot as plt

if __name__ == "__main__":
    datos = Practica_4.leer_datos()

    # Limpiar los datos
    datos_limpios = Practica_4.limpiar_datos(datos)

    # Suavizar los datos
    valores_suavizados = Practica_4.proc_ses(datos_limpios)

    # Graficar los datos limpios y suavizados
    plt.plot(datos_limpios, label="Datos Limpiados")
    plt.plot(valores_suavizados, label="Datos Suavizados", linestyle='dashed')
    plt.legend()
    plt.title("Procesamiento de Datos")
    plt.show()