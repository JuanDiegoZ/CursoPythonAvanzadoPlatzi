import random

def ordenamiento_mezcla(lista: list) -> list:
    if len(lista) > 1:
        middle = len(lista)//2
        izquierda = lista[:middle]
        derecha = lista[middle:]
        print(izquierda)
        print(derecha)

        ordenamiento_mezcla(izquierda)
        ordenamiento_mezcla(derecha)

        i = 0
        j = 0

        #iterador lista principal.

        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha [j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1

            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
    return lista


if __name__ == '__main__':

    lista = [random.randint(0,100) for i  in range (0 , 20)] 
    print(lista)
    print("*" * 100)
    print(ordenamiento_mezcla(lista))