class satisfaccion:

    def __init__(self, preferencias):  # preferencias: solo int_luminosa
        self.preferencias = preferencias
        self.vector = []

    def actualiza_vector(self, vector):
        self.vector = vector
        ## valida vector

    def calcula_satisfaccion(self, vector):  # vector: solo int_luminosa
        self.actualiza_vector(vector)

        satisfaccion = []

        for key, valor_a_analizar in vector.items():
            rango_preferencias = self.preferencias[key]
            vmin = rango_preferencias[0]
            vmax = rango_preferencias[1]
            wservicio = rango_preferencias[3]
            if rango_preferencias[2] == 0:  # minimización
                temp = self.calcula_satisfaccion_minimizacion(valor_a_analizar, vmin, vmax)
            else:  # maximización
                temp = self.calcula_satisfaccion_maximizacion(valor_a_analizar, vmin, vmax)
            temp = temp * wservicio
            satisfaccion.append(temp)

        return satisfaccion

    def calcula_satisfaccion_minimizacion(self, valor_a_analizar, vmin, vmax):
        xnew = (vmax - valor_a_analizar) / (vmax - vmin)
        return xnew

    def calcula_satisfaccion_maximizacion(self, valor_a_analizar, vmin, vmax):
        xnew = 1 - (vmax - valor_a_analizar) / (vmax - vmin)
        return xnew

    def calcula_ganancia_satisfaccion(self, satisfaccion):
        ganancia = sum(satisfaccion)
        return round(ganancia, 4)


if __name__ == "__main__":
    # PESO DE LA LUZ
    pesosPreferencias = [1.0]

    prefServicios = {  # 1 = maximización
        "int_luminosa": [400, 900, 1, pesosPreferencias[0]]
    }

    # VALOR ACTUAL EN EL ENTORNO
    valoresActuales = {
        "int_luminosa": 300
    }

    # VALOR OPTIMIZADO (RECOMENDACIÓN)
    valoresOptimizados = {
        "int_luminosa": 600
    }

    satis = satisfaccion(prefServicios)

    satisfaccion_resultado = satis.calcula_satisfaccion(valoresOptimizados)
    ganancia = satis.calcula_ganancia_satisfaccion(satisfaccion_resultado)
    print("Ganancia:", ganancia)

    print()

    # MEJOR VALOR POSIBLE
    valoresOptimizados = {
        "int_luminosa": 900
    }
    satisfaccion_resultado = satis.calcula_satisfaccion(valoresOptimizados)
    ganancia = satis.calcula_ganancia_satisfaccion(satisfaccion_resultado)
    print("Ganancia (mejor caso):", ganancia)

    # PEOR VALOR POSIBLE
    valoresOptimizados = {
        "int_luminosa": 400
    }
    satisfaccion_resultado = satis.calcula_satisfaccion(valoresOptimizados)
    ganancia = satis.calcula_ganancia_satisfaccion(satisfaccion_resultado)
    print("Ganancia (peor caso):", ganancia)
