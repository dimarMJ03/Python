#8. Crear una función que reciba dos enteros y que retorne (devuelva) el resto y el cociente
n1=int(input("Ingrese un numero: "))
n2=int(input("Ingrese otro numero: "))
def resto_cociente(num1, num2):
  resto = num1 % num2
  cociente = num1 // num2
  return resto , cociente

res_coci=f"El resto es {resto_cociente(n1,n2)[0]} y el cociente es {resto_cociente(n1,n2)[1]}"
print(res_coci)