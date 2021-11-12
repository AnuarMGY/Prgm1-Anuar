class Rectangulo:
  def __init__(self, altura, base):
    print("Instanciando esta clase")
    self.altura = altura
    self.base = base
  def mostrarBase(self):
    print("La base del rectangulo es: ", self.base)
  def mostrarAltura(self):
    print("La altura del rectangulo es: ", self.altura)
  def Perimetro(self, altura, base):
    vResult = 0
    vResult = (self.altura*2)+(self.base*2)
    print("El perimetro es: ", vResult)

rec = Rectangulo(3, 6)
rec.mostrarBase()
rec.mostrarAltura()
rec.Perimetro(3, 6)
