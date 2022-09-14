from re import A
import time

def fibo_gen(max) -> int:
     n1, n2 = 0, 1
     cont = 0
     while True:
        cont += 1
        yield n1
        if cont <= max:
            n1, n2 = n2 , n1 + n2
        else:
            raise StopIteration
        


if __name__ == "__main__":
    fibonacci =fibo_gen(5)
    for element in fibonacci:
        print(element)
        time.sleep(1)

