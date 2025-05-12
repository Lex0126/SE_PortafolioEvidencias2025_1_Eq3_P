import random as rnd

def solucionInicial(preferencias):
    vector = {}
    for key in preferencias.keys():
        registro = preferencias[key]
        val = rnd.randint(registro[0], registro[1])
        vector[key] = val
    return vector

def GenerarVecina(vector,preferencias):
    vectorTemp = vector.copy()
    idx_servicio = rnd.randint(0, len(preferencias)-1)
    key = list(preferencias.keys())[idx_servicio]
    vmin = preferencias[key][0]
    vmax = preferencias[key][1]
    vectorTemp[key] = rnd.randint(vmin, vmax)
    return vectorTemp


if __name__ == "__main__":
    #rnd.seed(5)

    #PREFERENCIAS MINIMAS Y MAXIMAS DE UN USUARIO...
    # C1 C2 C3 C4
    # C1 = TEMP
    # C2 = HUMEDAD
    # C3 = RUIDO
    # C4 = INTENSIDAD LUMINOSA

    # PESOS(IMPORTANCIA) QUE TIENE CADA SERVICIO
    pesosPreferencias = [0.4, 0.2, 0.1, 0.3] # = 1.0

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
        "temperatura": 18,
        "humedad": 60,
        "ruido": 90,
        "int_luminosa": 300
    }

    #busqueda local....
    #condiciones de paro:
    #1.- convergencia - iteraciones sin mejora*
    #2.- convergencia - optimo global
    #3.- iteraciones / generaciones
    #4.- evaluaciones de la funcion objetivo
    #5.- tiempo

    tot_mejoras_buscadas = 10
    tot_iteraciones = 100

    mejorasRealizadas = 0
    iteracionesRealizadas = 0

    mejorGanancia = 0
    mejoresValoresEncontrados = []

    alfa = 0.5
    beta = 0.5

    from Unidad_3.Problema import FuncionObjetivo as problema

    valoresOptimizados = solucionInicial(prefServicios)

    mejoresValoresEncontrados = valoresOptimizados #como se copia/clona un diccionario para evitar
    mejorGanancia = problema.calculaGanancia(alfa, beta, prefServicios, valoresActuales, valoresOptimizados)

    # la referencia de memoria

    while iteracionesRealizadas<tot_iteraciones and mejorasRealizadas<tot_mejoras_buscadas:
        # solucion vecina...
        valoresOptimizados = GenerarVecina(valoresOptimizados, prefServicios)
        fo_vecina = problema.calculaGanancia(alfa, beta, prefServicios, valoresActuales, valoresOptimizados)

        print("Ganancia de la Vecina:" , fo_vecina, end= "")

        if fo_vecina > mejorGanancia:
            print("     Se actualizo la mejor ganancia", end="")
            mejorGanancia = fo_vecina
            mejoresValoresEncontrados = valoresOptimizados.copy()
            mejorasRealizadas +=1
            iteracionesRealizadas = -1

        iteracionesRealizadas +=1
        print()

print("\nMejor Ganancia encontrada: ", mejorGanancia)
print("Mejores Valores Encontrados: ", mejoresValoresEncontrados)