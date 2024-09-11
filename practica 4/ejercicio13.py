# ejercicio 6
# Lista
nombres=["Luis","Frida","Manuel","Akemy","Maria","Yedimar","Dimarj´","Omar","Melissa"]

# a
# remueve el elemento final de la lista ´Melissa´ y agrega ´juan´ 
nombres.remove("Melissa")
nombres.append("Juan")
print(nombres)
print("")

# b
# imprime el antepenultimo elemento de cualquier lista
print(nombres[len(nombres)-3])
print("")

# c
# imprime cada elemento de la lista
for nombre in nombres:
  print(nombre)
print("")

# d
# triplica y imprime la lista
triplicar=nombres*3
print(triplicar)