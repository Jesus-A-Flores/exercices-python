'''Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el
mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.'''
def es_palindromo(a):
  inv = a[::-1]
  if inv == a:
    return True
  else:
    return False
