from Proyecto_Unidad_3.datos import ComodidadEnConsumoEnergia as s_energia
from Proyecto_Unidad_3.datos import SatisfaccionUsuario as s_usuario

def calculaGanancia(alfa, beta, prefServicios, valoresActuales, valoresOptimizados):
    ganancia_solucion = 0

    objSatisfaccion = s_usuario.satisfaccion(prefServicios)
    satisfaccion_usuario = objSatisfaccion.calcula_satisfaccion(valoresOptimizados)
    gananciaSatisfaccion = objSatisfaccion.calcula_ganancia_satisfaccion(satisfaccion_usuario)
    print("Ganancia Satisfacción:", gananciaSatisfaccion)

    objEnergia = s_energia.Energia(prefServicios)
    satisfaccion_energia = objEnergia.calcula_energia(valoresOptimizados, valoresActuales)
    gananciaEnergia = objEnergia.calcula_ganancia_energia(satisfaccion_energia)
    print("Ganancia Energía:", gananciaEnergia)

    ganancia_solucion = alfa * gananciaSatisfaccion + beta * gananciaEnergia
    return ganancia_solucion

if __name__ == "__main__":
    # Preferencias para intensidad luminosa únicamente
    pesosPreferencias = [1.0]  # Solo una característica
    costoCambio = [5]  # Solo luz

    prefServicios = {
        "int_luminosa": [400, 900, 1, pesosPreferencias[0], costoCambio[0]]
    }

    valoresActuales = {
        "int_luminosa": 300
    }

    valoresOptimizados = {
        "int_luminosa": 600  # Recomendado
    }

    alfa = 0.5
    beta = 0.5

    gananciaModelo = calculaGanancia(alfa, beta, prefServicios, valoresActuales, valoresOptimizados)
    print("Ganancia del Modelo:", gananciaModelo, end="")
