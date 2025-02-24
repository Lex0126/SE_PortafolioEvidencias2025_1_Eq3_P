import clase_suma_cuadrados as opt
import random
if __name__ == "__main__":
    minv = 0
    maxv = 100
    rm = 50 #si es mayor el resultado de las instancias muta si no se queda igual
    Vo = []
    obj = opt.SumadeCuadrados(minv, maxv, Vo)
    pop = obj.Poblacion(10,4)
    promedio = float("inf")
    rangoLimite = random.randint(0,5)
    print(rangoLimite)
    while promedio > rangoLimite:
        print("Poblacion:")
        for indv in pop:
            print(indv)
        padres = obj.ObtenerPadres(10, pop)
        print(len(pop))
        print("\nPadres:")
        for padre in padres:
            print(padre)

        print(len(padres))
        descendencia = obj.cruzaEnunPunto(padres)
        print("\nHijos:")
        for hijo in descendencia:
            print(hijo)

        mutacionDes = obj.mutacion(descendencia, rm)
        print("\nHijos despues de mutacion:")
        for hijo in mutacionDes:
            print(hijo)

        seleccion = obj.seleccionAmbiental(descendencia, padres, 10)
        print("\nSeleccion:")
        for seleccionados in seleccion:
            print(seleccionados)
        pop = seleccion
        promedio = obj.promedioVO()
        Vo.clear()

"""import one_max_problem as opt
import random

if __name__ == "__main__":
    rm = 50  # Probabilidad de mutacion
    Vo = []
    obj = opt.OneMaxProblem(Vo)
    pop = obj.Poblacion(10, 4)  # 10 individuos de longitud 4
    promedio = float("inf")
    rangoLimite = random.randint(0, 4)  # Se detiene cuando la media sea <= a este valor
    print("Limite de parada:", rangoLimite)

    while promedio > rangoLimite:
        print("\nPoblacion:")
        for indv in pop:
            print(indv)

        padres = obj.ObtenerPadres(10, pop)
        print("\nPadres:")
        for padre in padres:
            print(padre)

        descendencia = obj.cruzaEnunPunto(padres)
        print("\nHijos antes de mutacion:")
        for hijo in descendencia:
            print(hijo)

        mutacionDes = obj.mutacion(descendencia, rm)
        print("\nHijos después de mutacion:")
        for hijo in mutacionDes:
            print(hijo)

        seleccion = obj.seleccionAmbiental(descendencia, padres, 10)
        print("\nSeleccion final:")
        for seleccionados in seleccion:
            print(seleccionados)

        pop = seleccion
        promedio = obj.promedioVO()
        Vo.clear()"""

"""import valor_absoluto as opt
import random

if __name__ == "__main__":
    rm = 50  # Probabilidad de mutación
    Vo = []
    obj = opt.ValorAbsoluto(Vo)
    pop = obj.Poblacion(10, 4)
    promedio = float("inf")
    rangoLimite = random.randint(0, 5)
    print("Limite de paro:", rangoLimite)

    while promedio > rangoLimite:
        print("\nPoblacion:")
        for indv in pop:
            print(indv)

        padres = obj.ObtenerPadres(10, pop)
        print("\nPadres:")
        for padre in padres:
            print(padre)

        descendencia = obj.cruzaEnunPunto(padres)
        print("\nHijos:")
        for hijo in descendencia:
            print(hijo)

        mutacionDes = obj.mutacion(descendencia, rm)
        print("\nHijos después de mutacion:")
        for hijo in mutacionDes:
            print(hijo)

        seleccion = obj.seleccionAmbiental(descendencia, padres, 10)
        print("\nSeleccion:")
        for seleccionado in seleccion:
            print(seleccionado)

        pop = seleccion
        promedio = obj.promedioVO()
        Vo.clear()

    print("\nOptimizacion completada")"""
