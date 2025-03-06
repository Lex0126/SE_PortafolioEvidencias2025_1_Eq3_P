import Lectura as opt

if __name__ == "__main__":
    lectura = opt.Lectura()

    n = 144

    vectores = lectura.generar_Vector(n)
    lectura.guardar_vectores_csv(vectores, 'QuintaLectura.csv')

    