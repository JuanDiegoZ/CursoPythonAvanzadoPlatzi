import random

def busqueda_lineal(lista : list,objetivo : int) -> bool:

    for elemento in lista:
        if elemento == objetivo:
            return True

    return False 

if __name__ == '__main__':
    tamanno_lista = int(input('De que tamano sera la lista ?'))
    objetivo = int(input('Que numero quieres encontrar?'))
    lista = [random.randint(0,100) for i in range(tamanno_lista)]
    print (lista)
    print(busqueda_lineal(lista,objetivo))
