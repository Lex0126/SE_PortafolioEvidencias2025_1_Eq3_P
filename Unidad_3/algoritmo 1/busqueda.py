import random as rnd


class Energia:
    def __init__(self, preferencias_energia):
        self.preferencias_energia = preferencias_energia

    def actualiza_vector(self, vectorPorAplicar):
        self.vectorPorAplicar = vectorPorAplicar

    def calcula_energia(self, vectorPorAplicar, vDatosActuales):
        self.actualiza_vector(vectorPorAplicar)
        energia = []
        for key, valor_a_analizar in vectorPorAplicar.items():
            rango_preferencias = self.preferencias_energia[key]
            vmin = rango_preferencias[0]
            vmax = rango_preferencias[1]
            wservicio = rango_preferencias[3]
            #####
            costo = rango_preferencias[4]  # costo por cambio de unidad
            va = vDatosActuales[key]
            #######
            temp = -1
            if rango_preferencias[2] == 0:  # min
                if va >= vmin:
                    Eo = self.calcula_satisfaccion_energia_min(costo, valor_a_analizar, va)
                    Emin = self.calcula_satisfaccion_energia_min(costo, valor_a_analizar, vmax)
                    Emax = self.calcula_satisfaccion_energia_min(costo, valor_a_analizar, vmin)
                else:
                    temp = 1
            else:  # max
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

    def calcula_satisfaccion_energia_min(self, costo, valor_to_analizar, vReferencia):
        valor = 0
        if valor_to_analizar >= vReferencia:
            valor = costo + costo * (valor_to_analizar - vReferencia)
        return valor

    def calcula_satisfaccion_energia_max(self, costo, valor_to_analizar, vReferencia):
        valor = 0
        if valor_to_analizar <= vReferencia:
            valor = costo + costo * (vReferencia - valor_to_analizar)
        return valor

    def calcula_ganancia_satisfaccion(self, energia):
        ganancia = sum([ i ** 2 for i in energia])
        return round(ganancia, 4)

    def generar_vecino(self, solucion):
        vecino = solucion.copy()
        key = rnd.choice(list(vecino.keys()))
        min_val = self.preferencias_energia[key][0]
        max_val = self.preferencias_energia[key][1]
        vecino[key] = rnd.randint(min_val, max_val)
        return vecino


if __name__ == "__main__":
    pesosPreferencias = [0.4, 0.2, 0.1, 0.3]
    Precios = [40, 25, 12, 3]

    prefServicios = {
        "temperatura": [20, 28, 0, pesosPreferencias[0], Precios[0]],
        "humedad": [40, 80, 0, pesosPreferencias[1], Precios[1]],
        "ruido": [60, 120, 0, pesosPreferencias[2], Precios[2]],
        "int_luminosa": [400, 900, 1, pesosPreferencias[3], Precios[3]]
    }

    valoresActuales = {"temperatura": 18, "humedad": 60, "ruido": 90, "int_luminosa": 300}
    valoresOptimizados = {"temperatura": 20, "humedad": 40, "ruido": 60, "int_luminosa": 900}

    satis = Energia(prefServicios)
    best_sol = valoresOptimizados.copy()
    best_vo = satis.calcula_ganancia_satisfaccion(satis.calcula_energia(best_sol, valoresActuales))

    max_it = 20000
    it = 0
    while it < max_it:
        vecino = satis.generar_vecino(best_sol)
        vo_temporal = satis.calcula_ganancia_satisfaccion(satis.calcula_energia(vecino, valoresActuales))

        if vo_temporal > best_vo:
            best_vo = vo_temporal
            best_sol = vecino.copy()
            print("Nueva mejor solucion:", best_sol)
            print("Ganancia:", best_vo)

        it += 1

    print("Mejor solucion encontrada:", best_sol)
    print("Mejor ganancia:", best_vo)
