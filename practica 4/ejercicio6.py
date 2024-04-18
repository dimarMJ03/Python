#Imprime solo las vocales de un string
def vocales(palabra):
  vocales = ['a','e','i','o','u']
  for letra in vocales:
   if letra in palabra:
     
     print("Las vocales de la palabra son: ",letra ) 
  

vocales(input("Ingrese una palabra:"))
