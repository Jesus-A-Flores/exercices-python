'''Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena
"estoy probando" debería devolver la cadena "odnaborp yotse"'''
def inver(a):
  inv = ""
  for i in range(len(a)-1,-1,-1):
    inv+=a[i]
  return inv
