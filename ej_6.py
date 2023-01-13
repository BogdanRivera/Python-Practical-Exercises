"""
Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

"""

"""
def inversa(texto):
  invertida = []
  long = len(texto)-1
  while long>=0:
    invertida += texto[long]
    long -= 1
  return invertida

cadena = str(input("Dame una cadena de texto: "))
invierte =str(inversa(cadena))
print(f"La cadena invertida es {invierte}")
"""

#Otra forma
def invierte(text):
  a = text[::-1]
  return str(a)
  
chain = str(input("Dame un texto: "))
invertida = invierte(chain)
print(f"La cadena invertida es {invertida}")





  
