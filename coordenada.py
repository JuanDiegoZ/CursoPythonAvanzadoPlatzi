
class Coordenada:

    def __init__(self,x : int, y: int) -> None:
        self.x = x;
        self.y = y;

    def distancia(self,otra_coordenada):
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2

        return (x_diff + y_diff)** 0.5


if __name__ == '__main__':
    coordenada_one =  Coordenada(2,8)
    coordenada_two = Coordenada(2,9)
    #print(coordenada_one.distancia(coordenada_two))
    print(isinstance(coordenada_one,Coordenada))