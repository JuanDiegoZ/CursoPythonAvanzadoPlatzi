"""

objetivo =  int(input('Escoge el numero que deseas obtener su raiz cuadrada:'))
epsilon = 0.201
paso = epsilon**2
raiz = 0.0
veces_que_itero = 0


while (epsilon + objetivo) >= raiz**2:
    raiz += paso;
    veces_que_itero += 1
    print(veces_que_itero)
 
if (raiz - objetivo) <= epsilon:
    print(f'La raiz aproximada de {objetivo} es {raiz}')




"""


numero_hallar =int(input('Ingresa el numero del cual deseas saber la raiz: '))
epsilon= 0.001
min_range = 0.0
max_range = max(1.0,numero_hallar)
result_root = (max_range + min_range)/2

while abs(result_root**2 - numero_hallar) >= epsilon:
    print(f'rango max = {max_range}, rango min={min_range},{result_root}')
    if result_root**2 > numero_hallar:
        max_range = result_root
    else:
        min_range = result_root
    result_root = (max_range + min_range)/2

print(result_root**2 - numero_hallar)
print(f'La raiz aproximada de {numero_hallar} es {result_root}')
    
    
        

