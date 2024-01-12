#conteo hasta el numero que el usuario ingrese
def aprender_a_contar(entero):
  for numero in range(1, entero+1):
    print(numero)
aprender_a_contar(int(input("Ingrese un numero: ")))
