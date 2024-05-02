'''Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente
todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4])
debería devolver 24.'''
def sum(a):
  sum = 0
  for i in a:
    suma+=i
  return sum
def multip(a):
  mult = 1
  for i in a:
    mult*=i
  return mult
