'''Escribir un programa que pregunte el nombre completo del usuario en la consola 
y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, 
otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula.
 El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera. '''
fullname = input("Full Name?: ")
n1 = fullname.upper()
n2 = fullname.lower()
n3 = fullname.title()
print(f"1. {n1}\n2. {n2}\n3. {n3}")
