from Unidad_3.Problema import ComodidadEnConsumoEnergia as s_energia
from Unidad_3.Problema import SatisfaccionUsuario as s_usuario

def calculaGanancia(alfa, beta, prefServicios, valoresActuales, valoresOptimizados):
    ganancia_solucion = 0
    ##########################################################################################
    objSatisfaccion = s_usuario.satisfaccion(prefServicios)
    satisfaccion_usuario = objSatisfaccion.calcula_satisfaccion(valoresOptimizados)
    gananciaSatisfaccion = objSatisfaccion.calcula_ganancia_satisfaccion(satisfaccion_usuario)
    print("Ganancia Satisfaccion: ", gananciaSatisfaccion)
    ##########################################################################################
    objEnergia = s_energia.energia(prefServicios)
    satisfaccion_energia = objEnergia.calcula_energia(valoresOptimizados, valoresActuales)
    gananciaEnergia = objEnergia.calcula_ganancia_energia(satisfaccion_energia)
    print("Ganancia Energia: ", gananciaEnergia)
    ##########################################################################################
    ganancia_solucion = alfa * gananciaSatisfaccion + beta * gananciaEnergia

    return ganancia_solucion

if __name__ == "__main__":
    # PREFERENCIAS MINIMAS Y MAXIMAS DE UN USUARIO...
    # C1 C2 C3 C4
    # C1 = TEMP
    # C2 = HUMEDAD
    # C3 = RUIDO
    # C4 = INTENSIDAD LUMINOSA

    # PESOS(IMPORTANCIA) QUE TIENE QUE SE CUMPLA CADA CARACTERISTICA
    pesosPreferencias = [0.4, 0.3, 0.1, 0.2]

    # COSTO POR CAMBIAR UNA UNIDAD CADA CARACTERISTICA...
    costoCambio = [8, 3, 1, 5]  # C1, C2,..., Cn

    prefServicios = {  # 0 = minimizacion ---- 1 = maximizacion
        "temperatura": [20, 28, 0, pesosPreferencias[0], costoCambio[0]],
        "humedad": [40, 80, 0, pesosPreferencias[1], costoCambio[1]],
        "ruido": [60, 120, 0, pesosPreferencias[2], costoCambio[2]],
        "int_luminosa": [400, 900, 1, pesosPreferencias[3], costoCambio[3]]
    }

    # VALORES ACTUALES EN EL ENTORNO...
    valoresActuales = {
        "temperatura": 18,  ######
        "humedad": 60,
        "ruido": 90,
        "int_luminosa": 300
    }

    # VALORES OPTIMIZADOS... RECOMENDACION...
    valoresOptimizados = {
        "temperatura": 20,
        "humedad": 70,
        "ruido": 95,
        "int_luminosa": 600
    }

    alfa = 0.5
    beta = 0.5

    gananciaModelo = calculaGanancia(alfa, beta, prefServicios, valoresActuales, valoresOptimizados)
    print("Ganancia del Modelo:" , gananciaModelo, end= "")