#01-WHILE
edad=15
num=0

#Bucle Infinito

#while edad<18:
#   print("Eres menor de edad no puedes manejar")
#¿Que hace este bucle?

print("####### 01. CICLO WHILE ######")
while num<=100:
    print(num)
    num+=2
print("¡Primer bucle terminado!\n")

#Combinando un while y un else
while num<=200:
    print(num)
    num+=2
else:
    print("Mi condición es igual o mayor a 200")
print("Segundo bucle terminado")