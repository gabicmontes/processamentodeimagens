import random

lista = [2,4,10,1,7]
print(lista)

def verificaOrdem(lista) :
    for i in range(len(lista)-1):
        if(lista[i+1]<lista[i]):
            continue
        else:
            return False
    return True


while(verificaOrdem(lista) != True):
    random.shuffle(lista)
    verificaOrdem(lista)
    
print(lista)


