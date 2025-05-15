import serial
import time
import random as rnd
from Proyecto_Unidad_3.datos import SatisfaccionUsuario as s_usuario
from Proyecto_Unidad_3.datos import ComodidadEnConsumoEnergia as s_energia

#variables globales
PORT = 'COM6'  # puerto arduino
BAUD = 9600
LECTURAS = 30  # Numero de lecturas del dlr por ciclo
PAUSA_CICLO = 30  # segundos entre ciclos
LAMBDA_ENERGIA = 0.1  # esto es para determinar la prioridad de la iluminacion y la satisfaccion del usuario,costo energetico es de menor impacto en la decision final

#Comunicacion serial
def abrir_serial():
    s = serial.Serial(PORT, BAUD, timeout=2)
    time.sleep(2)
    return s
#esto para poder abir el puerto y poder usarlo
def leer_valor_LDR(ser):
    ser.write(b'1')
    dato = ser.readline().decode().strip()
    return int(dato) if dato.isdigit() else None
#mando un 1 para indicar el inicio de la lectura del sensor de arduino para evitar lecturas no deseadas

def enviar_comando(ser, codigo):
    ser.write(codigo.encode())

#enviamos el codigo que se determino despues del procesamiento

#Funcion Objetivo
def funcion_objetivo(promedio, valor_optimo, focos_encendidos, prefServicios, valoresActuales, valoresOptimizados):
    objSatisfaccion = s_usuario.satisfaccion(prefServicios)
    satisfaccion_usuario = objSatisfaccion.calcula_satisfaccion(valoresOptimizados)
    ganancia_satisfaccion = objSatisfaccion.calcula_ganancia_satisfaccion(satisfaccion_usuario)

    objEnergia = s_energia.Energia(prefServicios)
    energia_consumo = objEnergia.calcula_energia(valoresOptimizados, valoresActuales)
    ganancia_energia = objEnergia.calcula_ganancia_energia(energia_consumo)

    error_luz = abs(promedio - valor_optimo)# saber la cantidad verdadera entre la luz real y la luz deseada(600)

    return error_luz + ganancia_satisfaccion + LAMBDA_ENERGIA * focos_encendidos # focos encendidos sirve para penalizar el gasto de luz
""" calculamos el valor de la funcion, la funcion objetivo calcula que valor n
umerico es el mejor para la solucion que busca un equilibrio entre una cantidad de luz considerable ,poco gasto y satisfaccion del usuario"""
# Solucion inicial y vecina
def solucion_inicial(preferencias):
    vector = {}
    for key in preferencias.keys():
        rango = preferencias[key]
        val = rnd.randint(rango[0], rango[1])
        vector[key] = val
    return vector

def generar_vecina(vector, preferencias):
    vecina = vector.copy()
    idx = rnd.randint(0, len(preferencias) - 1)
    key = list(preferencias.keys())[idx]
    vmin, vmax = preferencias[key][0], preferencias[key][1]
    vecina[key] = rnd.randint(vmin, vmax)
    return vecina

#Busqueda Local
def busqueda_local(prom_actual, vector_optimo, focos_encendidos, prefServicios, valoresActuales):
    mejor_fo = funcion_objetivo(
        prom_actual,
        vector_optimo["int_luminosa"],
        focos_encendidos,
        prefServicios,
        valoresActuales,
        vector_optimo
    )

    iteraciones = 0
    mejoras = 0
    max_iter = 100
    max_mejoras = 10

    while iteraciones < max_iter and mejoras < max_mejoras:
        vecina = generar_vecina(vector_optimo, prefServicios)
        fo_vecina = funcion_objetivo(
            prom_actual,
            vecina["int_luminosa"],
            focos_encendidos,
            prefServicios,
            valoresActuales,
            vecina
        )

        if fo_vecina < mejor_fo:
            mejor_fo = fo_vecina
            vector_optimo = vecina
            mejoras += 1
            iteraciones = 0
        iteraciones += 1

    return vector_optimo
"""
- inicia el valor optimo
- generamos los vecinos como en busqueda normal 
-evaluamos cual es mejor en funcion la nuestra funcion objetivo
-repetimos hasta el alcnazar el numero de interaccicones 
"""
#Programa principal
def main():
    pesosPreferencias = [1.0]
    costoCambio = [5]

    prefServicios = {
        "int_luminosa": [400, 900, 1, pesosPreferencias[0], costoCambio[0]]
    }

    valoresActuales = {
        "int_luminosa": 300
    }

    vector_optimo = solucion_inicial(prefServicios)
    ser = abrir_serial()

    try:
        while True:
            muestras = []
            while len(muestras) < LECTURAS:
                val = leer_valor_LDR(ser)
                if val is not None:
                    muestras.append(val)

            prom_actual = sum(muestras) / LECTURAS
            valor_deseado = vector_optimo["int_luminosa"]
            print(f"\nPromedio LDR: {prom_actual:.2f}  |  Valor optimo buscado: {valor_deseado}")
            """
            para encender en arduino      para saber en nuestro sistma cuantos focos tenemos encendidos
            '3',                          2
            """
            margen = 100# margen de tolerancia se considera el prom de la luz este rnetre un rango del 100 del valor optimo
            if prom_actual <= valor_deseado - margen:
                cmd, focos = '3', 2
                print("Poca luz  encender 2 focos")
            elif prom_actual <= valor_deseado:
                cmd, focos = '1', 1
                print("Luz media  encender 1 foco")
            else:
                cmd, focos = '0', 0
                print("Suficiente luz  apagar focos")


            vector_optimo = busqueda_local(
                prom_actual, vector_optimo, focos,
                prefServicios, valoresActuales
            )

            enviar_comando(ser, cmd)
            time.sleep(PAUSA_CICLO)

    except KeyboardInterrupt:
        print("\nPrograma detenido")
    finally:
        ser.close()

if __name__ == "__main__":
    main()


