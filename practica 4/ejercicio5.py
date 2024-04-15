frase=["entender", "pueden", "humanos", "los", "que", "código","escriben", "programadores", "buenos", "Los", "entiende.", "computadora", "una", "que", "código","escribe", "tonto", "Cualquier"]

def unir_palabras(palabras):
  for palabra in palabras:
    print(palabra, end=" ")
    
unir_palabras(frase[::-1])