import random
def insertion_short(lista : list) -> bool:
    for i in range (1,len(lista)):
        iter_actual = lista[i]
        j = i - 1

        while(j >= 0 and lista[j] > iter_actual):
            lista[j + 1] = lista[j]
            j = j - 1
    
        lista[j + 1 ] = iter_actual

    return lista
    

            
            







if __name__ == '__main__':

    lista = [random.randint(0,100) for i  in range (0 , 20)] 
    print(lista)
    print(insertion_short(lista))
