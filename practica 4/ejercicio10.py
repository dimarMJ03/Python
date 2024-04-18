#Contar gustos
empanadas=["jamon y queso","carne","pollo","verdura","pollo","jamon y queso","carne","pollo"]
def contar_gustos(lista):
  gustos={}
  for gusto in lista:
    if gusto in gustos:
      gustos[gusto]+=1
    else:
      gustos[gusto]=1
  return gustos


print(contar_gustos(empanadas))




