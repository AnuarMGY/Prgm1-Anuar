from abc import (ABC, abstractmethod)

class Animales(ABC):
  def __init__(self,nombre,sexo,raza):
    self.nombre = nombre
    self.__edad = 0
    self.peso = 0
    self.sexo = sexo
    self.raza = raza
    self.vacunado = False
  
  @abstractmethod
  def hablar(self):
    print("El animal esta hablando")
  
  def publicarEdad(self):
    return self.__edad
  
  def actualizarEdad(self, edad):
    if edad > 0:
      self.__edad = edad
      print("Edad = ", edad)
    else:
      print("Ingrese la edad valida")

  def publicarPeso(self):
    return self.peso
  
  def actualizarPeso(self, peso):
    if peso > 0:
      self.peso = peso
      print("Peso = ", peso)
    else:
      print("Ingrese un peso valido")

class Perro(Animales):
  __vacuna = "P12345"
  def vacunar(self, vacuna):
    if self.__vacuna == vacuna:
      super().vacunado = True
    else:
      print("El codigo de vacunacion es incorrecto")
  def hablar(self):
    print("El perro esta ladrando")

class Gato(Animales):
  __vacuna = "G12345"
  def vacunar(self, vacuna):
    if self.__vacuna == vacuna:
      super().vacunado = True
    else:
      print("El codigo de vacunacion es incorrecto")
  def hablar(self):
    print("El gato esta maullando")

class Loro(Animales):
  __vacuna = "L12345"
  def vacunar(self, vacuna):
    if self.__vacuna == vacuna:
      super().vacunado = True
    else:
      print("El codigo de vacunacion es incorrecto")
  def hablar(self):
    print("El loro esta cantando")

perro1 = Perro("Charlie", "Macho", "Pastor")
perro1.hablar()
perro1.actualizarEdad(2)
perro1.actualizarPeso(30)
perro1.publicarEdad()
perro1.publicarPeso()
perro1.vacunar("P12345")

gato1 = Gato("Michis", "Hembra", "Bengala")
gato1.hablar()
gato1.actualizarEdad(4)
gato1.actualizarPeso(15)
gato1.publicarEdad()
gato1.publicarPeso()
gato1.vacunar("G12345")

loro1 = Loro("Lorenzo", "Macho", "Loro Australiano")
loro1.hablar()
loro1.actualizarEdad(5)
loro1.actualizarPeso(7)
loro1.publicarEdad()
loro1.publicarPeso()
loro1.vacunar("L12345")