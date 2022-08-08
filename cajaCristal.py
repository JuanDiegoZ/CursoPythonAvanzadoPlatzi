import unittest


def es_mayor_de_edad (age):
    if age >= 18:
        return True
    else:
        return False


class TestCrystalBox(unittest.TestCase):
    def test_es_mayor_de_edad(self):
        age = 39 

        resultado = es_mayor_de_edad(age)
        self.assertEquals(resultado,True)
    def test_es_menor_de_edad(self):
        age = 17
        
        resultado = es_mayor_de_edad(age)
        self.assertEquals(resultado,False)


    

if __name__ == '__main__':
    unittest.main()

