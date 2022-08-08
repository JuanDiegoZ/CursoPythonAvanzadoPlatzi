def list_div( lista ,div):
    try:
        return [i/divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista


lista = list(range(10))
divisor = 0

print(list_div(lista,divisor))