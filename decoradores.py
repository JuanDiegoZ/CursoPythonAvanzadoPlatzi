#Decoradores en python.
#29 july 2022.
from datetime import datetime

def decorador(fun):
    def print_menssaje_french():
        print("¡Bonjur!")
        fun()
    return print_menssaje_french

def print_hello():
    print("¡Hello!")

print_hello = decorador(print_hello)
print_hello()


# Syntactic sugar en los decoradores.

def decorador(fun):
    def print_menssaje_french():
        print("¡Bonjur!")
        fun()
    return print_menssaje_french


@decorador
def print_hello():
    print("¡Hello!")


def mayusculas(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura

@mayusculas
def mensaje(name):
    return f'{name}, recibiste un mensaje'

print(mensaje('cesar'))




#Programando decoradores. decorador para ver cuanto tiempo se demora en ejecutar una funcion.

def execution_time(func):
    """
    *args,**kwargs, no importa la cantidad de argumentos los va resiivr para esto se usan, estos 2."
    """
    def wrapper(*args,**kwargs):
        initial_time = datetime.now()
        func(*args,**kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f'Pasaron {time_elapsed.total_seconds()} segundos de tiempo en ejecución')
    return wrapper

@execution_time
def random_func():
    for _ in range(100000):
        pass

random_func()

@execution_time
def suma(a : int, b:int) -> int:
    return a + b``

@execution_time
def saludo(nombre ="cesar"):
    print("Hola " + nombre)

suma(5,5,)
saludo("Juan")









