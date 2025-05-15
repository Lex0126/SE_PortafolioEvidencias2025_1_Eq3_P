class Energia:

    def __init__(self, preferencias_energia):
        self.preferencias_energia = preferencias_energia
        self.vector = []

    def actualiza_vector(self, vectorPorAplicar):
        self.vectorPorAplicar = vectorPorAplicar

    def calcula_energia(self, vectorPorAplicar, vDatosActuales):
        self.actualiza_vector(vectorPorAplicar)
        energia = []

        for key, valor_a_analizar in vectorPorAplicar.items():
            rango_preferencias = self.preferencias_energia[key]
            vmin, vmax, tipo, wservicio, costo = rango_preferencias
            va = vDatosActuales[key]

            temp = -1
            if tipo == 0:  # minimización
                if va >= vmin:
                    Eo = self.calcula_satisfaccion_energia_min(costo, valor_a_analizar, va)
                    Emin = self.calcula_satisfaccion_energia_min(costo, valor_a_analizar, vmax)
                    Emax = self.calcula_satisfaccion_energia_min(costo, valor_a_analizar, vmin)
                else:
                    temp = 1
            else:  # maximización
                if va <= vmax:
                    Eo = self.calcula_satisfaccion_energia_max(costo, valor_a_analizar, va)
                    Emin = self.calcula_satisfaccion_energia_max(costo, valor_a_analizar, vmin)
                    Emax = self.calcula_satisfaccion_energia_max(costo, valor_a_analizar, vmax)
                else:
                    temp = 1
            if temp != 1:
                temp = 1 - (Eo - Emin) / (Emax - Emin)
            temp = temp * wservicio
            energia.append(temp)

        return energia

    def calcula_satisfaccion_energia_min(self, costo, valor_a_analizar, vReferencia):
        if valor_a_analizar >= vReferencia:
            return costo + costo * (valor_a_analizar - vReferencia)
        return 0

    def calcula_satisfaccion_energia_max(self, costo, valor_a_analizar, vReferencia):
        if valor_a_analizar <= vReferencia:
            return costo + costo * (vReferencia - valor_a_analizar)
        return 0

    def calcula_ganancia_energia(self, satisfaccion):
        ganancia = sum(satisfaccion)
        return round(ganancia, 4)


if __name__ == "__main__":
    # Preferencias: [mínimo, máximo, tipo (0=min, 1=max), peso, costo]
    prefServicios = {
        "int_luminosa": [400, 900, 1, 1.0, 5]  # Solo intensidad luminosa
    }

    valoresActuales = {
        "int_luminosa": 300  #
    }

    valoresOptimizados = {
        "int_luminosa": 600  # Ideal]
    }

    comodidad = Energia(prefServicios)
    satisfaccion = comodidad.calcula_energia(valoresOptimizados, valoresActuales)
    ganancia = comodidad.calcula_ganancia_energia(satisfaccion)

    print("Ganancia:", ganancia)
