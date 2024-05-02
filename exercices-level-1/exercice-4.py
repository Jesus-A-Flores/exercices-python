'''Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario
devuelve False.'''
def isVocal(a):
  for i in "aeiou":
    if a == i:
      return True
  return False
