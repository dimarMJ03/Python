#Agregar y ordenar elementos en una lista
cartas= [1, 4, 6, 8]
nueva_carta=int(input("Ingrese el numero de la nueva carta: "))
if nueva_carta not in cartas:
  cartas.append(nueva_carta)
  cartas.sort()
  print(cartas)
else:
  print("Esta carta ya esta en el mazo")
  print(cartas)





