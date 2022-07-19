def is_cousin(number: int) -> bool:
    for i in range(2,number - 1):
        if(number % i == 0):
            return False
    return True

def main():
    if(is_cousin("a")):
        print(f'The number is cousin')
    else:
        print(f'The number is not cousin')
main()