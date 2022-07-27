#Closures en python.


# HOLA 3 -> HOLAHOLA
# Facundo 2 -> FacundoFacundo 
# Platzi 4 -> PlatziPlatziPlatziPlatzi 

from __future__ import division


def make_repeater_of(n):
    
    def sentence_repeat(str_one):
        assert type(str_one) == str, "Solo puedes utilizar cadenas de texto." 
        return str_one*n
    
    return sentence_repeat

total = make_repeater_of(2)
print(total("Juan"))



"""Practice exercise clousures"""

def make_division_by(n : int):
    """This closure returns a function that returns the division of an x number by n
    """ 
    def divisor(m : int):
        return  m / n
    
    return divisor

division_by_3 = make_division_by(3)
print(division_by_3(18)) #The expected output is 6.

division_by_5 = make_division_by(5)
print(division_by_5(100)) #The expected output is 20.
     
division_by_18 = make_division_by(18)    
print(division_by_18(54)) #The expected output is 3.