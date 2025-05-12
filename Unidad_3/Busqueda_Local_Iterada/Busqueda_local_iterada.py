import random as rnd

def solucionInicial(preferencias):
    vector = {}
    for key in preferencias.keys():
        registro = preferencias[key]
        val = rnd.randint(registro[0], registro[1])
        vector[key] = val
    return vector

def GenerarVecina(vector, preferencias):
    vectorTemp = vector.copy()
    idx_servicio = rnd.randint(1, len(preferencias)-1)
    key = list(preferencias.keys())[idx_servicio]
    vmin = preferencias[key][0]
    vmax = preferencias[key][1]
    vectorTemp[key] = rnd.randint(vmin, vmax)
    return vectorTemp

def perturbar(solucion, preferencias):
    vector = solucion.copy()
    idx1 = list(vector.keys())[0]
    vector[idx1] = vector[idx1]  # Mantiene el primer valor sin cambios
    for i in list(vector.keys())[1:]:
        vector[i] = rnd.randint(preferencias[i][0], preferencias[i][1])
    return vector

if __name__ == "__main__":
    #rnd.seed(5)

    #PREFERENCIAS MINIMAS Y MAXIMAS DE UN USUARIO...
    # C1 C2 C3 C4
    # C1 = TEMP
    # C2 = HUMEDAD
    # C3 = RUIDO
    # C4 = INTENSIDAD LUMINOSA

    # PESOS(IMPORTANCIA) QUE TIENE CADA SERVICIO
    pesosPreferencias = [0.5, 0.4, 0.05, 0.05] # = 1.0

    # COSTO POR CAMBIAR UNA UNIDAD CADA CARACTERISTICA...
    costoCambio = [40, 32, 10, 3]  # C1, C2,..., Cn

    prefServicios = {  # 0 = minimizacion ---- 1 = maximizacion
        "temperatura": [20, 28, 0, pesosPreferencias[0], costoCambio[0]],
        "humedad": [40, 80, 0, pesosPreferencias[1], costoCambio[1]],
        "ruido": [60, 120, 0, pesosPreferencias[2], costoCambio[2]],
        "int_luminosa": [400, 900, 1, pesosPreferencias[3], costoCambio[3]]
    }

    # VALORES ACTUALES EN EL ENTORNO...
    valoresActuales = {
        "temperatura": 18,
        "humedad": 60,
        "ruido": 90,
        "int_luminosa": 300
    }

    # Variables para la búsqueda local iterada
    tot_mejoras_buscadas = 10
    tot_iteraciones = 10000

    mejorasRealizadas = 0
    iteracionesRealizadas = 0

    tot_mejoras_buscadas_i = 10
    tot_iteraciones_i = 100

    mejorasRealizada_i = 0
    iteracionesRealizadas_i = 0
    mejorGanancia = 0
    mejoresValoresEncontrados = []

    alfa = 0.75
    beta = 0.25

    from Unidad_3.Problema import FuncionObjetivo as problema

    valoresOptimizados = solucionInicial(prefServicios)

    mejoresValoresEncontrados = valoresOptimizados  # como se copia/clona un diccionario para evitar la referencia de memoria
    mejorGanancia = problema.calculaGanancia(alfa, beta, prefServicios, valoresActuales, valoresOptimizados)





    while iteracionesRealizadas_i<tot_iteraciones_i and mejorasRealizada_i<tot_mejoras_buscadas_i:
        while iteracionesRealizadas<tot_iteraciones and iteracionesRealizadas_i<tot_mejoras_buscadas:  #while de local
            valoresOptimizados = GenerarVecina(valoresOptimizados, prefServicios)  # Se genera una vecina, cambio pequeño
            fo_vecina = problema.calculaGanancia(alfa, beta, prefServicios, valoresActuales, valoresOptimizados)
            print("Ganancia de la Vecina:", fo_vecina, end="")


            if fo_vecina > mejorGanancia:
                print("    Se actualizó la mejor ganancia", end=" ")
                mejorGanancia = fo_vecina
                mejoresValoresEncontrados = valoresOptimizados.copy()
                mejorasRealizadas += 1
                iteracionesRealizadas = -1

            iteracionesRealizadas += 1


        valoresOptimizados = perturbar(valoresOptimizados, prefServicios)
        fo_vecina = problema.calculaGanancia(alfa, beta, prefServicios, valoresActuales, valoresOptimizados)
        if fo_vecina > mejorGanancia:
            mejorGanancia = fo_vecina
            mejoresValoresEncontrados = valoresOptimizados.copy()
            mejorasRealizada_i += 1
            iteracionesRealizadas_i = -1

        iteracionesRealizadas_i +=1
        print()


    print("\nMejor Ganancia encontrada:", mejorGanancia)
    print("Mejores Valores Encontrados:", mejoresValoresEncontrados)
