#Agregar solo numeros pares en otra lista
numeros=[1,6,2,8,2,14,7,15,13]
pares=[]
for numero in numeros:
  if numero%2==0:
    pares.append(numero)
print(pares)


