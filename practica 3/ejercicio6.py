print("Tablas de multiplicar del 1 al 10")
def aprender_a_multiplicar(entero):
  for i in range(1,11):
    print(entero, "x", i, "=", entero*i)
  
   
    
aprender_a_multiplicar(int(input("Ingrese un numero: ")))
