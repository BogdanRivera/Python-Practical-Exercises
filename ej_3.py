"""
Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.
"""

def longitud(texto):
  counter = 0
  for i in texto:
    counter += 1
  return counter

text = input("Ingresa una cadena de texto: ")
contador = longitud(text)
print(f"La longitud de la cadena introducida es de {contador}")


