#programa para agregar un ingrediente nuevo en la lista
ingredientes = ["tomate", "queso", "cebolla", "huevo"]
agregar_ingrediente=input("Ingrese un ingrediente:" )
if agregar_ingrediente not in ingredientes:
  ingredientes.append(agregar_ingrediente)
  print(ingredientes)
else:
  print("Ese ingrediente ya esta en la lista")
  print(ingredientes)




