# funcion para saldar deuda
def recibir_num(cobro_total):
  print("El importe a pagar es de", cobro_total," pesos. Por favor,ingrese un monto.")
  monto=int(input())
  print(monto)
  #bucle hasta que se cumpla la condicion
  while monto<cobro_total:
    
    cobro_total=cobro_total-monto
    print("El importe a pagar es de", cobro_total," pesos. Por favor,ingrese un monto:")
    monto=int(input())
    
  print("Deuda saldada")
    
recibir_num(100)
