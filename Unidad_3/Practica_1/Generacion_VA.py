import random as rnd
def generarCSV(dicc):
    file = open("../../../../../Downloads/valores_actuales.csv", "w")
    cadena = ","
    for key, value in dicc.items():
        for i in range(len(value)):
            valorenposicion = str(value[i])
            cadena = cadena + valorenposicion + ","
        file.write(key + ":" + cadena + "\n")
        cadena = ","
    file.close()

def generacionVA(rangos):
    dicc = {"Temperatura": [],
            "Humedad": [],
            "Ruido": [],
            "Luminosidad": []}
    for key, value in rangos.items():
        for i in range(100):
            dicc[key].append(rnd.randint(value[0], value[1]))
    return dicc
if __name__ == "__main__":
    rangosdeServicios = {
    "Temperatura": [15,39],
    "Humedad": [60, 90],
    "Ruido": [30,90],
    "Luminosidad": [100, 500]
}
    dicc = generacionVA(rangosdeServicios)
    generarCSV(dicc)