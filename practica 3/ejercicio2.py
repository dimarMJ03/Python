#una funcion para ganar si o si el piedra,papel o tijera
print("¡Juguemos! Ingresá piedra ( R), papel (P) o tijera (T)")
def juego():
  jugada = input("Ingresá tu jugada: ")
  if (jugada == 'P'):
    print("T")
  elif (jugada == 'R'):
    print("P")
  elif (jugada == 'T'):
    print("R")
  else:
    print("No vale")
juego()
