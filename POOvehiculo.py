class Vehiculo:
  def __init__(self, modelo, marca, anio):
    self.marca = marca
    self.modelo = modelo
    self.anio = anio
    print("Vehiculo creado")
  def arrancar(self):
    print("Estoy en movimiento")
'''
class Auto(Vehiculo):
  __litrosGasolina = 0
  transmisionManual = True
  def encender(self):
    print("Auto encendido")
  def arrancar(self):
    print("Auto avanzando")
  def claxon(self):
    print("Sonando el claxon")
  def echarGasolina(self, vLitros):
    if vLitros <= 1:
      print("Debes echar mas gasolina")
    else:
      self.__litrosGasolina = vLitros
  def contadorGasolina(self):
    print("La cantidad de gasolina en el auto es de: ", self.__litrosGasolina)
'''
class Moto(Vehiculo):
  __litrosGasolina = 0
  __maxGasolina = 20
  transmisionManual = True
  __llave = "54321"
  encendida = False
  def encender(self, llave):
    if self.__llave == llave:
      print("Moto encendida")
      self.encendida = True
    else:
      print("Llave incorrecta")
      self.encendida = False
  def arrancar(self):
    if self.encendida == True:
      print("Moto avanzando")
    else:
      print("Moto apagada, no puede avanzar")
  def claxon(self):
    print("Sonando el claxon")
  def echarGasolina(self, vLitros):
    if vLitros <= 1:
      print("Debes echar mas gasolina")
    elif vLitros > 2 and vLitros < self.__maxGasolina:
      self.__litrosGasolina = vLitros
    elif vLitros >= self.__maxGasolina:
      self.__litrosGasolina = self.__maxGasolina
      print("Tanque full")
  def contadorGasolina(self):
    print("La cantidad de gasolina en la moto es de: ", self.__litrosGasolina)
'''
carro1 = Auto("Aveo", "Chevrolet", "2016")
carro1.encender()
carro1.claxon()
carro1.contadorGasolina()
carro1.echarGasolina(100)
carro1.contadorGasolina()
'''
moto1 = Moto("Dos ruedas", "Empire", "2018")
moto1.echarGasolina(15)
moto1.encender("54321")
moto1.arrancar()
moto1.contadorGasolina()