import clase_suma_cuadrados as opt
import random
if __name__ == "__main__":
    minv = 0
    maxv = 100
    rm = 50 #si es mayor el resultado de las instancias muta si no se queda igual
    Vo = []
    obj = opt.SumadeCuadrados(minv, maxv, Vo)
    pop = obj.Poblacion(10,6)
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
