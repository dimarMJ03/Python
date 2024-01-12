def sumador():
  numero1=int(input("Ingrese el primer numero: "))
  numero2=int(input("Ingrese el segundo numero: "))
  suma= numero1 + numero2
  if suma < 100:
    print("La suma es menor a 100")
    resto=100-suma
    print("Falta ", resto, " para llegar a 100")
  elif suma > 100:
    print("Llega a 100")
    
sumador()

