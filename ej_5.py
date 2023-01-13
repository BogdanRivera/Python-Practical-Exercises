"""
Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""
import functools #Viene en esta librería y solo devuelve un valor

item = [1,2,3,4]
suma = functools.reduce(lambda counter,sum:counter+sum,item)
multiplica = functools.reduce(lambda counter,mult:counter*mult,item)
print("La suma de la lista es",suma)
print("La multiplicacion de la lista es",multiplica)
