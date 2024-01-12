lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(0, 10):
  if lista[i] == 8:
    print("El numero 8 esta en la lista")
    break
  print(str(i))

i=0
while( lista[i] != 8):
  print(str(i))
  i+=1
  if lista[i]==8:
    print("El numero 8 esta en la lista")
