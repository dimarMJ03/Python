ticket_1= [("Leche", 250), ("Pan", 300), ("Queso", 500), ("Arroz", 300)]

ticket_2= [("Leche", 250), ("Pan", 300),("Queso", 50)]

lista_de_tickets=[]
# Agrego ticket_1 y ticket_2 en una lista
for elemento in ticket_1:
  lista_de_tickets.append(elemento)
for elemento in ticket_2:
  lista_de_tickets.append(elemento)
print("Lista de compras:")
print("")
print(lista_de_tickets)
print("")
# Calculo de el precio total de la lista de tickets
def calcular_total(ticket):
  total=0
  for producto, precio in ticket:
    total+=precio
  return total

total_a_pagar= calcular_total(lista_de_tickets)
print("El total a pagar es: $", total_a_pagar)