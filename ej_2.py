""""
Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

"""

def max_de_tres(a,b,c):
  if a>b and a>c:
    return a
  elif b>a and b>c:
    return b
  else:
    return c

x = int(input("Numero 1: "))
y = int(input("Numero 2: "))
z = int(input("Numero 3: "))

max = max_de_tres(x,y,z)
print(f"Entre {x},{y} y {z} el mayor es {max}")

