import random as rnd

xmin   =-10
xmax = 10

def crear_sol_vecina(solucion):
    vector =solucion[:]
    pos = rnd.randint(0, len(solucion)-1)
    nuevo_val = rnd.randint(xmin,xmax)
    vector[pos] = nuevo_val
    return vector


def calcula_fo(solucion):
    vo = sum([i**2 for i in solucion])
    return vo

def crear_solucion(n):
    v=[rnd.randint(xmin,xmax)for i in range(n)]
    return v


if __name__ =="__main__":
    print("inicia algoritmo")
    solucion_temporal = crear_solucion(5)
    print("solucion temporal: ",solucion_temporal)
    best_so = solucion_temporal[:]
    best_vo = calcula_fo(best_so)

    max_it  =200
    it = 0

    while it< max_it:
        solucion_temporal =crear_sol_vecina(solucion_temporal)  # se hace un cambio ya sea bueno o malo
        vo_temporal = calcula_fo(solucion_temporal)

        if vo_temporal<best_vo:
            best_vo= vo_temporal
            best_so = solucion_temporal[:]
            print("nueva best solucion:",solucion_temporal)
            print("vo:",vo_temporal)
                                                # calculamos si dio buenos resultados y solo se tienen que hace pequenios cambios, y solo se tiene que ver si pequenios cambios
        it+=1
    print("mejor sol: ",best_so) #entonces se hace como una prueba y venemos el mejor rendimiento y se ira acomodando difrente por cada cambio
    print("mejor vo",best_vo)