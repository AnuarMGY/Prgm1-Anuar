class Circunferencia:
  def __init__(self, radio):
    print("Instanciando esta clase")
    self.radio = radio
  def mostrarRadio(self):
    print("El radio de la circunferencia es: ", self.radio)
  def area(self):
    area = 0
    area = self.radio * self.radio * 3.1416
    print("El area de la circunferencia es: ", area)
  def perimetro(self):
    peri = 0
    peri = 2 * 3.1416 * self.radio
    print("El perimetro de la circunferencia es: ", peri)

cir = Circunferencia(3)
cir.mostrarRadio()
cir.area()
cir.perimetro()
