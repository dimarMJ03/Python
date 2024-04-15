tupla=("Perú","Lima","Ámerica")
tupla2=("Francia","París","Europa")
tupla3=("Argentina","Buenos Aires","Ámerica")
tupla4=("Alemania","Berlín","Europa")
tupla5=("Japón","Tokio","Asia")
listas=[]
#meter las tuplas en una lista
for i in range(len(tupla)):
  listas.append(tupla[i])
  listas.append(tupla2[i])
  listas.append(tupla3[i])
  listas.append(tupla4[i])
  listas.append(tupla5[i])
print(listas)
print("")
#funcion para ordenar los paises con sus capitales y continentes
def lista_paises(lista):
  for i in range(5):
    print(f"País: {lista[i]}")
    print(f"Capital: {lista[i+5]}")
    print(f"Continente: {lista[i+10]}")
    print("")
lista_paises(listas)
