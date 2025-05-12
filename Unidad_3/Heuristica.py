import random
import copy

solucion =[3,1,2,5,4]

def vecindario(arr):
    posicion = random.randint(0,len(arr)-1)
    arr[posicion] = random.randint(1,5)
    return arr
def funciob(arr):
    fo =0
    for i in range(len(arr)):
        fo +=arr[i]
    return fo
So = solucion
Sbest = So[:]
vbest = funciob(So)
print(vbest)
print(So)

it =0
while it<10000:
    nsol=vecindario(So)
    vnsol = funciob(nsol)
    if(vnsol <vbest):
        vbest = vnsol
        Sbest = nsol
    So=nsol
    it+=1

print(vbest)
print(Sbest)