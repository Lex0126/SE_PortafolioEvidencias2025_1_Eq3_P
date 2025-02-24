import time
import serial
from Practica_5 import leer_datos, limpiar_datos, proc_ses

def main(archivo="24hrs.csv"):
    ser = serial.Serial('COM6', 9600)
    dia = 1
    data = leer_datos(archivo)

    while True:
        print(f"\nDía {dia}")

        if dia == 1:
            vector = [float(row[0]) for row in data]
            print(f"Datos originales del lunes: {vector}")
        else:
            cleaned_data = limpiar_datos(data)
            vector = [float(row[0]) for row in cleaned_data]
            print(f"Datos limpios (dia {dia}): {vector}")

        n_vector, s_valor = proc_ses(vector, dia=dia)

        print(f"\nValores procesados del dia {dia}: {n_vector}")
        print(f"Estado del AC en el dia {dia}: {s_valor}")

        for hora, estado in enumerate(s_valor, start=1):
            if 'Prender' in estado:
                ser.write(b'1')
            else:
                ser.write(b'0')
            print(f"Hora {hora}: {estado}")
            time.sleep(1)

        dia += 1

        if dia == 8:
            dia = 1
            print("\nSiguiente semana\n")

        time.sleep(10)

if __name__ == "__main__":
    main()





