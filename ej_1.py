"""
Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.
"""

def max(a,b):
  if a>b:
    return a
  else:
    return b


a = int(input("Teclea un numero: "))
b = int(input("Teclea otro numero: "))
maxi = max(a,b)
print(f"Entre {a} y {b}, el más grande es {maxi}")
