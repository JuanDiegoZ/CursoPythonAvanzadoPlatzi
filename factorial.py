# 4 de agosto 2022

def factorial(n :int ) -> int:
    """This fuction calculate the factorial of 
        number using recursive.
        input n -> int.
        return int.
    """
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(f'el factoria de 3 es {factorial(3)}')    