import random as rnd

xmin =-100
xmax = 100
lista_tabu ={}
tiempo_tabu = 5

def crear_sol_vecina(solucion):
    vector =solucion[:]
    pos = rnd.randint(0, len(solucion) - 1)
    while pos in lista_tabu:
        pos = rnd.randint(1, len(solucion) - 1)

    nuevo_val = rnd.randint(xmin,xmax)
    vector[pos] = nuevo_val
    return vector,pos


def calcula_fo(solucion):
    vo = sum([i**2 for i in solucion])
    return vo

def crear_solucion(n):
    v=[rnd.randint(xmin,xmax)for i in range(n)]
    return v

def pertubacion(solucion):
    vector = solucion[:]
    pos1 = vector[0]
    vector[0] = pos1
    while pos1 in lista_tabu:
        for i in range(1,len(solucion)):
            vector[i] = rnd.randint(xmin,xmax)

    return vector,pos1


if __name__ =="__main__":
    print("inicia algoritmo")
    solucion_temporal = crear_solucion(5)
    print("solucion temporal: ",solucion_temporal)
    best_so = solucion_temporal[:]
    best_vo = calcula_fo(best_so)

    max_it_ils = 1000
    it_ils = 0

    max_it_local  =10000
    it_local = 0


    while it_ils<max_it_ils:#busqueda loca iterada

        while it_local< max_it_local: #busqueda local
            solucion_temporal,idx1 =crear_sol_vecina(solucion_temporal)  # se hace un cambio ya sea bueno o malo
            vo_temporal = calcula_fo(solucion_temporal)

            if vo_temporal<best_vo:
                best_vo= vo_temporal
                best_so = solucion_temporal[:]
                print("nueva best solucion:",solucion_temporal)
                print("vo:",vo_temporal)
                lista_tabu[idx1] = tiempo_tabu

            lista_tabu_temp = lista_tabu.copy()
            for key in lista_tabu.keys():
                lista_tabu_temp[key] -= 1
                if lista_tabu_temp[key] == 0:
                    del lista_tabu_temp[key]
            lista_tabu = lista_tabu_temp
                                                    # calculamos si dio buenos resultados y solo se tienen que hace pequenios cambios, y solo se tiene que ver si pequenios cambios
            it_local+=1

        solucion_temporal,idx1 = pertubacion(solucion_temporal)
        vo_temporal =calcula_fo(solucion_temporal)
        if vo_temporal<best_vo:
            best_vo= vo_temporal
            best_so = solucion_temporal[:]
            print("nueva best solucion:",solucion_temporal)
            print("vo:",vo_temporal)
            lista_tabu[idx1] = tiempo_tabu

        lista_tabu_temp = lista_tabu.copy()
        for key in lista_tabu.keys():
            lista_tabu_temp[key] -= 1
            if lista_tabu_temp[key] == 0:
                del lista_tabu_temp[key]
        lista_tabu = lista_tabu_temp
        it_ils+=1
    print("mejor sol: ",best_so) #entonces se hace como una prueba y venemos el mejor rendimiento y se ira acomodando difrente por cada cambio
    print("mejor vo",best_vo)

    #pertubacion: en la busqueda normal solo cambio una posicion, iterada todos jugaran en una posicion diferente,es eo cambio brusco en toda la solucion , entonces tomamos que la pertubacion es all cambio brusco de nuestra sol
    # entonce para determinar el uso de pertubacion es de forma visual
