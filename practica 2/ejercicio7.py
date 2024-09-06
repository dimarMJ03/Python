#ejercicio 4
#año del usuario
año1=int(input("Ingrese su año de nacimiento: "))
#año de referencia para calcular la edad
año2=int(input("Ingrese un año para calcular su edad en el mismo: "))

#resta de los años
resta=año2-año1
if año2 >= año1:
  
  print(f"La edad que va a tener en el año {año2} sera de {resta} años")
else:
  print("Usted no habia nacido en ese año")


