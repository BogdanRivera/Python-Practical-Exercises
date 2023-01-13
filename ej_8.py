"""
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
"""

frutas = {'platano':1.35,'manzana':0.80,'pera':0.85,'naranja':0.70}

opc = input("Que fruta desea comprar?")
opc_f = opc.lower()
kil = float(input("Cuántos kilos? "))

if(opc_f in frutas):
  print(f"El precio final por {kil}kg de {opc_f} es de: ",round(kil*frutas[opc_f],2))
else:
  print("Fruta no encontrada")
