#agrego los diccionarios en una lista
lista=[]
for elemento in range(0,3):
  
  producto=input("Ingrese el nombre del producto: ")
  precio=float(input("Ingrese el precio del producto: "))
  cantidad=int(input("Ingrese la cantidad de productos: "))
  print("")
  ticket={
    "Nombre del producto": producto,
    "Precio por unidad": precio,
    "Cantidad":cantidad
    }
  print()
  lista.append(ticket)
  #se calcula el total de cada producto
  def pagar_monto(x):
    total=precio*cantidad
    sumar=print("Monto a pagar: " ,total)
  pagar_monto(ticket)  
  print("")
print("Total de su compra")
print("")
print(lista)
