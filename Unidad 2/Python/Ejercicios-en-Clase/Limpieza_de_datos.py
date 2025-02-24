import Suavizamiento_Exp as se
datos = []
datosTratados = []

f = open("TerceraLectura.csv", "r")
def limpiezaDatos(f, datos):
    for line in f:
        datos.append(line.strip().split(","))
    datos.pop(0)
    for i in range(len(datos)):
        for j in range(1):
            if(datos[i][1]  == ''):
                datosTratados.append(0.0)
            else:
                datosTratados.append(float(datos[i][1]))
    return datosTratados
def interpolacionLineal(datosTratados):
    for i in range(len(datosTratados)):
        if (datosTratados[i] == '' and i != 0 and i != len(datosTratados)):
            datosTratados[i] = datosTratados[i - 1] + (
                        (datosTratados[i + 1] - datosTratados[i - 1]) / ((i + 1) - (i - 1))) * (i - (i - 1))


def busquedaValorQn(tamaño, posicion, alfa, beta):
        Qn = ((posicion * (tamaño - alfa - beta + 1 ) )/ 4) + alfa
        return Qn

def busquedaValorQporInterpolacion(posicion, arreglo):
        size = len(arreglo)
        Qn = posicion * (size + 1) / 4
        if (isinstance(Qn, int) == True):
            Qn = arreglo[Qn]
        else:
            decimal = abs(Qn) - abs(int(Qn))
            entero = abs(int(Qn))
            Qn = (arreglo[entero] + decimal) * (arreglo[entero + 1] - arreglo[entero])
            Qn = round(Qn,2)
        return Qn
def IQR(q1,q3):
    iqr = q3 - q1
    return iqr
if __name__ == '__main__':
    limpiezaDatos(f, datos)
    print(datosTratados)
    Q1 = busquedaValorQporInterpolacion(1, datosTratados )
    Q3 = busquedaValorQporInterpolacion(3, datosTratados )
    iqr = IQR(Q1,Q3)
    print(f"Q1: {Q1}, Q3: {Q3}, IQR: {iqr}")
