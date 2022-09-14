from logging import exception
import time
class EvenNumbers:
  """Clase que implementa un iterador de todos los números pares,
  o los números pares hasta un máximo
  """

  #* Constructor de la clase
  def __init__(self, max = None): #self hace referencia al objeto futuro que voy a crear con esta clase
    self.max = max


  # Método para tener elementos o atributos que voy a necesitar para que el iterador funcione
  def __iter__(self):
    self.num = 0 #Primer número par
    #* Convertir un iterable en un iterador
    return self

  # Método para tener la función "next" de Python
  def __next__(self):
    if not self.max or self.num <= self.max:
      result = self.num
      self.num += 2
      return result
    else:
      raise StopIteration



class FiboIter():
    """O
    Objeto iterador de la funcion fibonnaci, no resive ningun parametro.
    """
    def __init__(self, max_cont = None): #self hace referencia al objeto futuro que voy a crear con esta clase
      self.max_cont = max_cont


    def __iter__(self):
      self.one_number = 0
      self.two_number = 1
      self.cont = 0
      return self
    
    def __next__(self):
      if self.cont <= self.max_cont:
          if self.cont == 0:
            self.cont += 1
            return self.one_number
          elif self.cont == 1:
            self.cont += 1
            return self.two_number
          else:
            self.max = self.one_number +  self.two_number
            self.one_number, self.two_number = self.two_number, self.max
            self.cont += 1
            return self.max
      else:
          raise StopIteration



if __name__ == "__main__":
    fibonacci = FiboIter(50)
    for iter in fibonacci:
      
      print(iter)
      
