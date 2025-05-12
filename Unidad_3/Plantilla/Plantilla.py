
class satisfaccion:

    def __init__(self, preferencias): # [s1, s2, s3, s4]
        self.preferencias = preferencias
        self.vector = []

    def actualiza_vector(self, vector):
        self.vector = vector
        ##valida vector

    def calcula_satisfaccion(self, vector): # [v1, v2, v3, v4]
        self.actualiza_vector(vector) ###

        satisfaccion = []

        temp = []
        for key, valor_to_analizar in vector.items():
            rango_preferencias = self.preferencias[key]
            vmin = rango_preferencias[0]
            vmax = rango_preferencias[1]
            wservicio = rango_preferencias[3]

            if rango_preferencias[2] == 0:
                temp = self.calcula_satisfaccion_minimizacion(valor_to_analizar,vmin,vmax)
            else:
                temp = self.calcula_satisfaccion_maximizacion(valor_to_analizar,vmin,vmax)
            temp =temp*wservicio
            satisfaccion.append(temp)

        return satisfaccion

    def calcula_satisfaccion_minimizacion(self,valor_to_analizar,vmin,vmax):
        xnew =(vmax-valor_to_analizar)/(vmax-vmin)

        return xnew

    def calcula_satisfaccion_maximizacion(self,valor_to_analizar,vmin,vmax):
        xnew = 1-(vmax-valor_to_analizar)/(vmax-vmin)
        return xnew


    def calcula_ganancia_satisfaccion(self, satisfaccion):
        ganancia = sum(satisfaccion)
        return round(ganancia, 4)


if __name__ == "__main__":
    # C1 C2 C3 C4
    # C1 = TEMP
    # C2 = HUMEDAD
    # C3 = RUIDO
    # C4 = INTENSIDAD LUMINOSA
    pesosPreferencias = [0.4, 0.2, 0.1, 0.3]

    prefServicios = { # 0 = minimizacion ---- 1 = maximizacion
        "temperatura":[20, 28, 0,pesosPreferencias[0]],
        "humedad":[40, 80, 0,pesosPreferencias[1]],
        "ruido":[60, 120, 0,pesosPreferencias[2]],
        "int_luminosa":[400,900, 1,pesosPreferencias[3]]
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


    satis = satisfaccion(prefServicios)
    satisfaccion = satis.calcula_satisfaccion(valoresOptimizados)
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