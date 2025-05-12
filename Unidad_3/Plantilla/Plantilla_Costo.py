
class Energia: # que tan comodo nos encontramos con base con el consumo de energia en la config

    def __init__(self, preferencias_energia): # [s1, s2, s3, s4]
        self.preferencias_energia = preferencias_energia
        self.vector = []

    def actualiza_vector(self, vectorPorAplicar):
        self.vectorPorAplicar = vectorPorAplicar
        ##valida vector

    def calcula_energia(self, vectorPorAplicar,vDatosActuales): # [v1, v2, v3, v4]
        self.actualiza_vector(vectorPorAplicar)  ###

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
                if va >= vmin:  #
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

    def calcula_satisfaccion_energia_min(self,costo,valor_to_analizar,vReferencia):
        valor =0
        if valor_to_analizar >= vReferencia:
            valor = costo + costo*(valor_to_analizar-vReferencia)
        return valor

    def calcula_satisfaccion_energia_max(self,costo,valor_to_analizar,vReferencia):
        valor = 0
        if valor_to_analizar <= vReferencia:
            valor = costo + costo * (vReferencia - valor_to_analizar)
        return valor



    def calcula_ganancia_satisfaccion(self, energia):
        ganancia = sum(energia)
        return round(ganancia, 4)


if __name__ == "__main__":
    # C1 C2 C3 C4
    # C1 = TEMP
    # C2 = HUMEDAD
    # C3 = RUIDO
    # C4 = INTENSIDAD LUMINOSA
    pesosPreferencias = [0.4, 0.2, 0.1, 0.3]
    Precios =  [40,25,12,3]

    prefServicios = { # 0 = minimizacion ---- 1 = maximizacion
        "temperatura":[20, 28, 0,pesosPreferencias[0],Precios[0]],
        "humedad":[40, 80, 0,pesosPreferencias[1],Precios[1]],
        "ruido":[60, 120, 0,pesosPreferencias[2],Precios[2]],
        "int_luminosa":[400,900, 1,pesosPreferencias[3],Precios[3]]
    }

    #VALORES ACTUALES EN EL ENTORNO...
    valoresActuales = {
        "temperatura": 18,
        "humedad": 60,
        "ruido": 90,
        "int_luminosa": 300
    }

    #VALORES OPTIMIZADOS... RECOMENDACION...
    valoresOptimizados = {
        "temperatura": 20,
        "humedad": 40,
        "ruido": 60,
        "int_luminosa": 900
    }

    #PESOS(IMPORTANCIA) QUE TIENE CADA SERVICIO


    satis = Energia(prefServicios)
    satisfaccion = satis.calcula_energia(valoresOptimizados,valoresActuales)
    ganancia = satis.calcula_ganancia_satisfaccion(satisfaccion)
    print("Ganancia: ", ganancia)

    print()

    #MEJORES VALORES OPTIMIZADOS
    #valoresOptimizados = [20, 40, 60, 900]
    #satisfaccion = calcula_satisfaccion(prefServicios, valoresOptimizados)
    #ganancia = calcula_ganancia_satisfaccion(satisfaccion, pesosPreferencias)
    #print("Ganancia: ", ganancia)

    #PEORES VALORES OPTIMIZADOS
    #valoresOptimizados = [28, 80, 120, 400]
    #satisfaccion = calcula_satisfaccion(prefServicios, valoresOptimizados)
    #ganancia = calcula_ganancia_satisfaccion(satisfaccion, pesosPreferencias)
    #print("Ganancia: ", ganancia)