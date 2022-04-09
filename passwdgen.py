import random
import string

# Definimos una lista con los caracteres que usaremos
caracteres = list(string.hexdigits + string.ascii_letters + string.punctuation)

# Mensaje de bievenida
print("+---------------------------------------------+")
print("Generador de contraseñas © 2022 Santiago Palacios")
print("+---------------------------------------------+ \n")

# Preguntamos cuantas contraseñas se quieren generar
cantidad_a_generar = input("Cuantas contraseñas quiere generar?: ")
cantidad_a_generar = int(cantidad_a_generar)

# Preguntamos cual sera el largo de la contraseña
longitud = input("Longitud de su contraseña: ")
longitud = int(longitud)

print("\n¡Contraseñas generadas exitosamente!")

# Generamos
for pwd in range(cantidad_a_generar):
    contraseñas = ''
    for c in range(longitud):
        contraseñas += random.choice(caracteres)
    print(contraseñas)

# Mensaje de despedida
print("\nGracias por usar este generador de contraseñas <3")