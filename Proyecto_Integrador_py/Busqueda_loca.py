import serial
import time
import random as rnd
import requests
from Proyecto_Unidad_3.datos import SatisfaccionUsuario as s_usuario
from Proyecto_Unidad_3.datos import ComodidadEnConsumoEnergia as s_energia

# Configuracion global
PORT = 'COM6'
BAUD = 9600
LECTURAS = 30
PAUSA_CICLO = 30  # segundos entre ciclos
peso_ENERGIA = 0.1

# Parametros para el POST
API_URL = "http://localhost:3000/api/v1/device-with-record"
ID_TYPE = 1
ID_SIGNAL_TYPE = 1
BASE_NAME = "SensorLDR_"
contador = 13  #nombre


# Abrir comunicacion serial
def abrir_serial():
    s = serial.Serial(PORT, BAUD, timeout=2)
    time.sleep(2)
    return s

# Leer valor del sensor
def leer_valor_LDR(ser):
    ser.write(b'1')
    dato = ser.readline().decode().strip()
    return int(dato) if dato.isdigit() else None

# Enviar comando a Arduino
def enviar_comando(ser, codigo):
    ser.write(codigo.encode())

# Enviar datos a la API
def enviar_a_api(id_type, id_signal_type, name, current_value):
    payload = {
        "id_type": id_type,
        "id_signal_type": id_signal_type,
        "name": name,
        "current_value": current_value
    }
    try:
        respuesta = requests.post(API_URL, json=payload)
        if respuesta.status_code == 201:
            print("Registro insertado correctamente en la API")
        else:
            print(f"Error al enviar a la API: {respuesta.status_code} - {respuesta.text}")
    except Exception as e:
        print(f" Error de conexión con la API: {e}")

# Funcion objetivo
def funcion_objetivo(promedio, valor_optimo, focos_encendidos, prefServicios, valoresActuales, valoresOptimizados):
    objSatisfaccion = s_usuario.satisfaccion(prefServicios)
    satisfaccion_usuario = objSatisfaccion.calcula_satisfaccion(valoresOptimizados)
    ganancia_satisfaccion = objSatisfaccion.calcula_ganancia_satisfaccion(satisfaccion_usuario)

    objEnergia = s_energia.Energia(prefServicios)
    energia_consumo = objEnergia.calcula_energia(valoresOptimizados, valoresActuales)
    ganancia_energia = objEnergia.calcula_ganancia_energia(energia_consumo)

    error_luz = abs(promedio - valor_optimo)

    return error_luz + ganancia_satisfaccion + peso_ENERGIA * focos_encendidos

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

# Búsqueda local
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

# Programa principal
def main():
    global contador  # para incrementar el nombre del dispositivo

    pesosPreferencias = 1.0
    costoCambio = 5

    prefServicios = {
        "int_luminosa": [400, 900, 1, pesosPreferencias, costoCambio]
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
            print(f"\nPromedio LDR: {prom_actual:.2f}  |  Valor optimo: {valor_deseado}")

            margen = 100
            if prom_actual <= valor_deseado - margen:
                cmd, focos = '3', 2
                print(" Poca luz --> encender 2 focos")
            elif prom_actual <= valor_deseado:
                cmd, focos = '1', 1
                print(" Luz media --> encender 1 foco")
            else:
                cmd, focos = '0', 0
                print(" Luz suficiente --> apagar focos")

            vector_optimo = busqueda_local(
                prom_actual, vector_optimo, focos,
                prefServicios, valoresActuales
            )

            enviar_comando(ser, cmd)

            # Envio de los datos a la API
            nombre_dispositivo = BASE_NAME + str(contador)
            enviar_a_api(ID_TYPE, ID_SIGNAL_TYPE, nombre_dispositivo, prom_actual)
            contador += 1

            time.sleep(PAUSA_CICLO)

    except KeyboardInterrupt:
        print("\n Programa detenido por el usuario")
    finally:
        ser.close()

if __name__ == "__main__":
    main()

