class Lavadora:


    def __init__(self) -> None:
        pass

    def lavar (self, temperatura = 'caliente'):
        self._llenar_tanque_de_agua(temperatura)
        self._añadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque_de_agua(self,temperatura):
        print(f'Llenando el tanque con agua {temperatura}')

    def _anadir_jabon(self):
        print('Añadiendo jabon')
    
    def _laver(self):
        print('Lavando la ropa')
    
    def _centrifugar(self):
        print('Centrifugar la ropa')


class Cohete:
    def __init__(self, peso, anno_modelo,numero_motores ) -> None:
        self.peso = peso
        self.anno_modelo = anno_modelo   
        self.numero_motores = numero_motores
    
    def despege(self,estado ='off'):
        self.motor('on')
        if (estado):
            print("despegando 3, 2, 1...")
    
    def motor(self, encender_motor ='off'):

        self.inyectar_combustible()
        self.encender_motor ='on'
        
    def inyectar_combustible(self):
        print('Inyectando combustible.')
    
    def velocidad(self):
        tiempo = 10
        aceleracion = 0
        print('Aumentar veloicidad +, Disminuir velocidad -')
        validar_aceleracion = input()
        if validar_aceleracion == '+':
            aceleracion += 1
        else:
            aceleracion -= 1    
        
        self.velocidad = aceleracion * tiempo 
        print(self.velocidad)


cohete1 = Cohete(10,2012,6)
cohete1.despege("on")
cohete1.velocidad()

