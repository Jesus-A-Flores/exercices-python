'''Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1
miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for
anidado. '''
def superposicion(a,b):
  for i in a:
    for j in b:
      if i == j:
        return True
  return False
