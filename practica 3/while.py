# Uso del Conitnue
#Estado Previo (inicalizo var en 0, se usa en al condicion)
var = 0
#COndicion del while, que var sea menor que 15
while (var < 15):
  #Cuerpo del while
  if var == 10:
    var += 1
    continue
    
  print("hola " + str(var))
  #Paso, cambio de a variable usada en la condicion
  var += 1

print("hola termino")

# Uso del break
var = 0
while (var < 15):
  if var == 10:
    break

  print("hola " + str(var))
  var += 1

print("hola termino")

