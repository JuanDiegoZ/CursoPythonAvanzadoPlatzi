import time


def time_funtion(func):
    def wrapper(*args, **kwargs):
        initial_time = time.time()
        func(int(*args), **kwargs)
        final_time = time.time()
        total_time = final_time - initial_time
        print(total_time)

    return wrapper        

@time_funtion
def factorial(n):
    respuesta = 1


    while n > 1:
        respuesta *= n
        n -= 1 
    
    return respuesta

def factorial_r(n : int):
    n = int(n)
    if n == 1:
        return 1
    
    return n * factorial_r(n - 1)

factorial(2000)
initial_time = time.time()
factorial_r(200)
final_time = time.time()
total_time = final_time - initial_time
print(total_time)