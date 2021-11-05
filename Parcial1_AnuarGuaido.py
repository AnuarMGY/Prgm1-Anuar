vTemperaturas = [36, 42, 57, 58, 7, 45, 26, 35, 83, 56, 57, 97, 28, 115, 53, 35, 99, 62, 78, 29, 98, 37, 42, 56, 86, 28, 86, 95, 26, 49, 67, 21, 815, 67, 104, 58, 512, 24, 92, 89, 67, 53, 81, 79, 83, 81, 44, 132, 77, 98, 73, 57]
def par(numero):
  return numero % 2 == 0
def cien(numero):
  return numero > 100
def funcionprincipal():
  for i in vTemperaturas:
    if cien(i) and par(i):
      print(i,"URGENTE! La temperatura es mayor a 100 grados y este numero es par")
    elif cien(i):
      print(i,"URGENTE! La temperatura es mayor a 100 grados")
    elif par(i):
      print(i,"es un numero par")
print("Lista de valores:")
print(vTemperaturas)
print("")
print("Resultados:")
funcionprincipal()