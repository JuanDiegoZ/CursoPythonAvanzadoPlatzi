from __future__ import print_function


def morral(tamanno_morral,pesos,valores,n):
    if n == 0 or tamanno_morral == 0:
        return 0
    
    if pesos[n - 1] > tamanno_morral:
       return morral(tamanno_morral,pesos,valores,n - 1)
        

    return max(valores[n - 1] + morral(tamanno_morral - pesos[n - 1],pesos,valores,n - 1),morral(tamanno_morral,pesos,valores,n - 1))        





if __name__ == '__main__':
    valores = [60,100,120]
    pesos = [10,20,30]
    tamanno_morral = 30
    n = len(valores)

    resultado = morral(tamanno_morral,pesos,valores,n)
    print(resultado)