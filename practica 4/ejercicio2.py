#agregar nombres y edad de una tupla a una lista
nombres1=("Melissa",40,"Dimarj´",20)
nombres2=("Omar",42,"Yedimar",5)
nombres3=("Maria",14,"Akemy",17)
varios_nombres=[]
for i in range(len(nombres1)):
  varios_nombres.append(nombres1[i])
  varios_nombres.append(nombres2[i])
  varios_nombres.append(nombres3[i])
print(varios_nombres)