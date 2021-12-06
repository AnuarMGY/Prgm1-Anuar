class Cuentas:
  propietario = ""
  tipoCuenta = ""
  __saldo = 0.0

  def __init__(self, propietario, tipoCuenta):
    self.propietario = propietario
    self.tipoCuenta = tipoCuenta
    #self.setSaldo(saldo)

  def getSaldo(self):    
    res = self.__saldo
    return res
  
  def setSaldo(self, saldo):
    self.__saldo = self.__saldo + saldo
  def consultarSaldo(self):
    print("El saldo de la cuenta es: ",self.getSaldo)
  def depositar(self, monto):
    if monto > 0:
      self.setSaldo(monto) 
  def retirar(self,monto):
    if monto < 0:
      self.setSaldo(monto)
  def abonarIntereses(self):
    pass
#class Ahorro(Cuentas):

class PlazoFijo(Cuentas):
  __saldoPF = 0.0
  periodoTiempo = 0
  tasa = 0.1
  def __init__(self, pt):
    self.periodoTiempo = pt
  def getSaldoPF(self):
    return self.__saldoPF
  def setSaldoPF(self, saldo):
      self.__saldoPF = saldo
  def abonarIntereses(self):
    intereses = super().getSaldo * self.tasa + self.periodoTiempo
    self.setSaldoPF(super().getSaldo + intereses)

cuentaAnuar = Cuentas("Anuar","Ahorro")
cuentaAnuar.setSaldo(20)
cuentaAnuar.getSaldo()
print(cuentaAnuar.getSaldo)
