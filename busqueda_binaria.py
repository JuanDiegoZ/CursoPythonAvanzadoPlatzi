from pickle import TRUE
import random
from tkinter.messagebox import RETRY

def binary_search(lista :list, start :int, end :int, objetive :int) -> bool:
    """
    This fuction search the number of the list , using binary search.
    """
    if start > end:
        return False

    medium = (start + end) // 2

    if lista[medium] == objetive:
        return True

    elif lista[medium] < objetive:
        return binary_search(lista, medium + 1,end ,objetive)

        
    else:
     
        return binary_search(lista, start, medium - 1 ,objetive)
        


      

if __name__ == '__main__':
    objetive = int(input('ingresa el valor a buscar: '))
    size = int(input('Cual es el tamaño de la lista: '))
    lista = sorted([random.randint(0,100) for i  in range (0 , size)])
    print(lista)
    print(binary_search(lista,0 , len(lista),objetive))
    
