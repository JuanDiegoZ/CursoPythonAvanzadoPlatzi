# HOLA 3 -> HOLAHOLA
# Facundo 2 -> FacundoFacundo 
# Platzi 4 -> PlatziPlatziPlatziPlatzi 

def make_repeater_of(n):
    
    def sentence_repeat(str_one):
        assert type(str_one) == str, "Solo puedes utilizar cadenas de texto." 
        return str_one*n
    
    return sentence_repeat

total = make_repeater_of(2)
print(total(7))
