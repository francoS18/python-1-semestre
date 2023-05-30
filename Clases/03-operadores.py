##OPERADORES ARITMETICOS
a = 20
b = 4
c = 69
d = 3
print("suma", a+b)
print("resta",c-a)
print("exponente",b**d)
#Faltan mas operadores

#GRAVEDAD
t=5.19
g=9.81
v=g*t
print(f"la velocidad de el objeto en caida libre es de: {v} m/s")
print(f"la velocidad de el objeto en caida libre es de: {v:.1f}m/s") #ACORTAR DECIMALES
print("la velocidad de el objeto en caida libre es de: {:.1f}" .format(v), "m/s")

#COMPLEJOS
c2=complex(3, -5)
print("el número complejo es:",c2)

print(c2.real)
print(c2.imag)

#A PROBAR
print("hola"*5) #funciona
#print("hola"*3.5*2) #ya no
print("hola" * 2)

##OPERADORES DE COMPARACIÓN
print("comparando números")
print(a == b) # "==" no es lo mismo que "="
print(b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print("\n")

#Comparar textos
animal_domestico="gato"
animal_salvaje="leopardo"
print(animal_domestico==animal_salvaje)
print(animal_domestico>animal_salvaje)
print(animal_domestico<animal_salvaje)
institucion="Universidad de los lagos"
print(institucion.split())

bencina=True
encendido=True
edad=19

#Utilizando el operador AND
if bencina and encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede arrancar")

#Utilizando el operador OR
if bencina or encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede arrancar")

#Utilizando el operador NOT junto al AND
if not bencina and encendido:
    print("Utilizando NOT y AND: El vehiculo puede avanzar")#EL NOT INVIERTE LA AFIRMACION SI ES TRUE ENTONCES SE INVIERTE A FALSE
else:
    print("El vehiculo no puede arranzar")

#Utilizando el operador NOT junto al OR
if not bencina or encendido:
    print("Utilizando NOT y OR: El vehiculo puede avanzar") #EL NOT INVIERTE LA AFIRMACION
else:
    print("El vehiculo no puede arrancar")

#Utilizando el operador NOT junto al AND y OR
if not bencina or (encendido and edad>=18): #CUANDO HAY 2 TRUE SE COMPARA CON LA PRIMERA AFIRMACION
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede arrancar")
# Si = if ; Sino = else ; SinoSi = elif 