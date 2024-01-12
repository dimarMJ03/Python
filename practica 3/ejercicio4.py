print("Verano = V", "Otoño = O", "Invierno = I", "Primavera = P")
def muestra_estaciones(estacion):
  if estacion == "V":
    print("Verano")
  elif estacion == "O":
    print("Otoño")
  elif estacion == "I":
    print("Invierno")
  elif estacion == "P":
    print("Primavera")
  else:
    print("Error")
muestra_estaciones(input("Ingrese una estacion del año: "))
