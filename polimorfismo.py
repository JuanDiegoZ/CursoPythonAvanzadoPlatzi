class Persona:

    def __init__(self,nombre) -> None:
        self.nombre = nombre

    def avanza(self):
        print('Ando caminando')

class Ciclista(Persona):

    def __init__(self, nombre) -> None:
        super().__init__(nombre)

    def avanza(self):
        print('Ando en la rodada')
    


juan = Persona('juan')
juan.avanza()
tom = Ciclista('tom')
tom.avanza()



