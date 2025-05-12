class energia: #Que tan comodo nos encontramos en base con el consumo de energia en la configuracion dada

    def _int_(self, preferencias_energia):
        self.preferencias = preferencias_energia
        self.vector = []

    def actualiza_vector(self, vectorPorAplicar):
        self.vectorPorAplicar = vectorPorAplicar


    def calcula_energia(self, vectorPorAplicar, vDatosActuales):
        self.actualiza_vector(vectorPorAplicar)
        energia = []

        temp = []
        for key, valor_a_analizar in vectorPorAplicar.items():
            rango_preferencias = self.preferencias[key]
            vmin = rango_preferencias[0]
            vmax = rango_preferencias[1]
            wservicio = rango_preferencias[3]
            costo = rango_preferencias[4]
            va = vDatosActuales [key]

            if rango_preferencias[2] == 0:
                Eo = self.calcula_satisfaccion_energia_min(costo, valor_a_analizar, va)
                Emin = self.calcula_satisfaccion_energia_min(costo, valor_a_analizar, vmax)
                Emax = self.calcula_satisfaccion_energia_min(costo, valor_a_analizar, vmin)
                temp = (Emax - Eo)/(Emax - Emin)
            else:
                Eo = self.calcula_satisfaccion_max(costo, valor_a_analizar, va)
                Emin = self.calcula_satisfaccion_max(costo, valor_a_analizar, vmax)
                Emax = self.calcula_satisfaccion_max(costo, valor_a_analizar, vmin)
                temp = 1 - (Emin - Eo) / (Emin - Emax)
            temp = temp * wservicio
            energia.append(temp)
        return energia


    def calcula_satisfaccion_energia_min(self, costo, valor_a_analizar, Vreferencia):
        valor = 0
        if valor_a_analizar > Vreferencia:
            valor = costo + costo * (valor_a_analizar - Vreferencia)
        return valor

    def calcula_satisfaccion_energia_max(self, costo, valor_a_analizar, Vreferencia):
        valor = 0
        if valor_a_analizar < Vreferencia:
            valor = costo + costo * (valor_a_analizar - Vreferencia)
        return valor

    def calcula_ganancia_energia(self, energia):
        ganancia = sum(energia)

if _name_ == "_main_":

    pesosPreferencias = [0.4, 0.3, 0.1, 0.2]










    comodidad_energia = energia(pesosPreferencias)
    satisfaccion_energia = comodidad_energia.calcula_energia()
    ganancia = comodidad_energia.calcula_ganancia_energia(satisfaccion_energia)