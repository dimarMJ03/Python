# la funcion concatena una palabra y un numero
def concatenar(palabra,numero):
  cadena=palabra +""+ str(numero)
  return cadena

#se pide ingresar un string
tex=input("Ingrese una palabra: ")
#se pide ingresar un numero
num=int(input("Ingrese un numero: "))
union=concatenar(tex,num)
print(union)
