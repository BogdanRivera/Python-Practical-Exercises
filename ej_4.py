"""
Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
"""

def is_vocal(c):
  if c in "aeiou":
    return True
  else: 
    return False

c = input("Dame un caracter: ")
c = c.lower()
c = c[0]
resultado = is_vocal(c)
if resultado==True:
  print("Si es una vocal")
else:
  print("No es una vocal")
  
  
  