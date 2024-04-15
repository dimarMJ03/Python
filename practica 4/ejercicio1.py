#creo una lista con nombres
nombres=["Maria","Yedimar","Dimarj´","Omar","Melissa"]
#reemplazar el nombre del indice 4 por Juan
nombres.remove("Melissa")
nombres.append("Juan")
#imprimo el nombre que esta a dos posiciones del final, funciona para cualquier lista  con nombres
largo=len(nombres)
print(nombres[largo-3])