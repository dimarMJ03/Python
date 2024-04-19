#funcion para crear un diccionario de planta y guardar en una lista de diccionarios
def guardar_plantas(x, especie_nueva, necesita_luz_solar, precio_nueva_planta):
  planta_nueva={
    "especie":especie_nueva,
    "necesita luz":necesita_luz_solar,
    "precio": precio_nueva_planta
  }  
  plantas.append(planta_nueva)
plantas=[]
guardar_plantas(plantas, "rosa",True, 200)
guardar_plantas(plantas, "jazmin", False, 900)

print(plantas)