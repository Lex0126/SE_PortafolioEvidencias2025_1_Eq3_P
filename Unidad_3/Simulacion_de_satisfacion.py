def Sat(rn, vo, st):
    mins = rn[0]
    maxs = rn[1]
    sat = []
    for f in vo:
        f_sat = []
        i = 0
        for val in f:
            s = (maxs[i] - val) / (maxs[i] - mins[i])
            if st[i]:
                s = 1 - s
            f_sat.append(s)
            i += 1
        sat.append(f_sat)
    return sat

def Sattot(sats, p):
    sat_tot = []
    for f_sat in sats:
        tot = 0
        for i in range(len(f_sat)):
            tot += f_sat[i] * p[i]  # peso por posicion y lo voy sumando
        sat_tot.append(tot)
    return sat_tot

def Minim(cx, va, vo):
    if va >= vo:
        return cx + cx * (va - vo)
    else:
        return 0

def Maxim(cx,vo,va):
    if va<= vo:
        return cx + cx*(vo-va)
    else:
        return 0


def CalcularEncost(cx,va,vo,rn):
    encost = []
    for i in range(len(cx)):
        if st[i]:
            Eo = Maxim(cx[0],vo[0][i],va[0][i])
            Emin = Maxim(cx[0],rn[0][i],va[0][i])
            Emax = Maxim(cx[0],rn[1][i],va[0][i])
            if Emin== Emax:
                encost.append(0)
            else:
                encost.append(1-(Emax-Eo)/(Emax-Emin))
        else:
            Eo = Minim(cx[0], va[0][i], vo[0][i])
            Emin = Minim(cx[0], va[0][i], rn[1][i])
            Emax = Minim(cx[0], va[0][i], rn[0][i])
            if Emax == Emin:
                encost.append(0)
            else:
                encost.append(1 - (Emax - Eo) / (Emax - Emin))
    return encost


rn = [
    [20, 40, 60, 400],
    [28, 80, 120, 900]
]
p = [0.4, 0.2, 0.1, 0.3]
st = [False, False, False, True]


vo = [
    [23, 70, 61, 724]
]
va = [
    [20, 80, 100, 750]
]
cx = [40, 25, 12, 3]




sat_tot = Sattot(Sat(rn, vo, st), p)
encos_t = CalcularEncost(cx, va, vo, rn)

print(encos_t)
print(sat_tot)



