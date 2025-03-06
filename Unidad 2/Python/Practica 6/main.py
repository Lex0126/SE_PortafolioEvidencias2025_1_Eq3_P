import time
import serial
from Practica_6 import limpiar_datos, proc_ses

def main():
    ser = serial.Serial('COM6', 9600)
    dia = 1
    data = []
    previous_estado = ""

    while True:
        print(f"\nDía {dia}")

        while len(data) < 24:
            if ser.in_waiting > 0:
                temp = ser.readline().decode('utf-8').strip()
                if temp.replace('.', '', 1).isdigit():
                    data.append(float(temp))
                    print(f"Temperatura leida: {temp}°C")
                else:
                    print("dato no valida")

            else:
                print("leyendo mas datos")

        print(f"\nDatos del dia {dia} (datos leidos): {data}")

        cleaned_data = limpiar_datos([[d] for d in data])

        n_vector, s_valor = proc_ses([d[0] for d in cleaned_data], dia=dia)

        print(f"\nValores procesados del dia {dia}: {n_vector}")
        print(f"Estado del AC en el dia {dia}: {s_valor}")

        for hora, estado in enumerate(s_valor, start=1):
            print(f"{estado}")
            if 'Prender' in estado:
                ser.write(b'1')
            else:
                ser.write(b'0')

            time.sleep(1)

        dia += 1

        if dia == 8:
            dia = 1
            print("\nSiguiente semana\n")

        data.clear()
        time.sleep(10)

if __name__ == "__main__":
    main()


