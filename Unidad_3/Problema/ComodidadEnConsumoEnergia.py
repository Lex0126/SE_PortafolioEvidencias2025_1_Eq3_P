class energia: #Que tan comodos nos encontramos con base en el consumo de energia
    #en la configuracion dada

    def __init__(self, preferencias_energia): # [s1, s2, s3, s4]
        self.preferencias_energia = preferencias_energia
        self.vector = []

    def actualiza_vector(self, vectorPorAplicar):
        self.vectorPorAplicar = vectorPorAplicar
        ##valida vector

    def calcula_energia(self, vectorPorAplicar, vDatosActuales): # [v1, v2, v3, v4]
        self.actualiza_vector(vectorPorAplicar) ###

        energia = []

        for key, valor_a_analizar in vectorPorAplicar.items():
            rango_preferencias = self.preferencias_energia[key]
            vmin = rango_preferencias[0]
            vmax = rango_preferencias[1]
            wservicio = rango_preferencias[3]
            #####
            costo = rango_preferencias[4] # costo por cambio de unidad
            va = vDatosActuales[key]
            #######
            temp = -1
            if rango_preferencias[2] == 0: #min
                if va >= vmin: #
                    Eo = self.calcula_satisfaccion_energia_min(costo, valor_a_analizar, va)
                    Emin = self.calcula_satisfaccion_energia_min(costo,valor_a_analizar, vmax)
                    Emax = self.calcula_satisfaccion_energia_min(costo,valor_a_analizar, vmin)
                else:
                    temp = 1
            else: #max
                if va <= vmax:
                    Eo = self.calcula_satisfaccion_energia_max(costo, valor_a_analizar, va)
                    Emin = self.calcula_satisfaccion_energia_max(costo, valor_a_analizar, vmin)
                    Emax = self.calcula_satisfaccion_energia_max(costo, valor_a_analizar, vmax)
                else:
                    temp = 1
            if temp != 1:
                temp = 1-(Eo-Emin)/(Emax-Emin)
            temp = temp*wservicio
            energia.append(temp)

        return energia

    def calcula_satisfaccion_energia_min(self, costo, valor_a_analizar,vReferencia):
        valor = 0
        if valor_a_analizar >= vReferencia:
            valor = costo + costo * (valor_a_analizar-vReferencia)
        return valor

    def calcula_satisfaccion_energia_max(self, costo, valor_a_analizar,vReferencia):
        valor = 0
        if valor_a_analizar <= vReferencia:
            valor = costo + costo * (vReferencia-valor_a_analizar)
        return valor

    def calcula_ganancia_energia(self, satisfaccion):
        ganancia = sum(satisfaccion)
        return round(ganancia, 4)


if __name__ == "__main__":
    #PREFERENCIAS MINIMAS Y MAXIMAS DE UN USUARIO...
    # C1 C2 C3 C4
    # C1 = TEMP
    # C2 = HUMEDAD
    # C3 = RUIDO
    # C4 = INTENSIDAD LUMINOSA

    # PESOS(IMPORTANCIA) QUE TIENE QUE SE CUMPLA CADA CARACTERISTICA
    pesosPreferencias = [0.4, 0.3, 0.1, 0.2]

    #COSTO POR CAMBIAR UNA UNIDAD CADA CARACTERISTICA...
    costoCambio = [8, 3, 1, 5] #C1, C2,..., Cn

    prefServicios = {  # 0 = minimizacion ---- 1 = maximizacion
        "temperatura": [20, 28, 0, pesosPreferencias[0], costoCambio[0]],
        "humedad": [40, 80, 0, pesosPreferencias[1], costoCambio[1]],
        "ruido": [60, 120, 0, pesosPreferencias[2], costoCambio[2]],
        "int_luminosa": [400, 900, 1, pesosPreferencias[3], costoCambio[3]]
    }

    # VALORES ACTUALES EN EL ENTORNO...
    valoresActuales = {
        "temperatura": 18, ######
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

    comodidad_energia = energia(prefServicios)
    satisfaccion_energia = comodidad_energia.calcula_energia(valoresOptimizados, valoresActuales)
    ganancia = comodidad_energia.calcula_ganancia_energia(satisfaccion_energia)
    print("Ganancia: ", ganancia)

    #"MEJORES" VALORES OPTIMIZADOS
    #valoresOptimizados = [18, 400, 20, 15]
    #vEo = calcula_Eo(valoresOptimizados, valoresActuales, costoCambio)
    #vEmin = calcula_Emin(valoresMaximos, valoresMinimos, valoresActuales, costoCambio)
    #vEmax = calcula_Emax(valoresMaximos, valoresMinimos, valoresActuales, costoCambio)
    #ganancia = calcula_ganancia_energia(vEo, vEmin, vEmax)
    #print("Ganancia: ", ganancia)

    #"PEORES" VALORES OPTIMIZADOS
    #valoresOptimizados = [24, 50, 80, 200]
    #vEo = calcula_Eo(valoresOptimizados, valoresActuales, costoCambio)
    #vEmin = calcula_Emin(valoresMaximos, valoresMinimos, valoresActuales, costoCambio)
    #vEmax = calcula_Emax(valoresMaximos, valoresMinimos, valoresActuales, costoCambio)
    #ganancia = calcula_ganancia_energia(vEo, vEmin, vEmax)
    #print("Ganancia: ", ganancia)