#6. Crear una función que reciba un número y muestre el anterior y el siguiente.
numero_usuario=int(input("Ingrese un numero: "))
print(" ")
def mostrar_anterior_posterior(numero):
  print(f"El numero anterior es {numero-1}")
  print(f"El numero posterior es {numero+1}")
mostrar_anterior_posterior(numero_usuario)  


