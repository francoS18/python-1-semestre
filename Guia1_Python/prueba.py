# 11. Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

ganadores=[]
for i in range(6):
    numeros=int(input("Ingrese el numero ganador: "))
    if numeros >= 1 and numeros<=49:
        ganadores.append(numeros)
        ganadores.sort()
    else:
        print("Numero incorrecto.")
print(f"Los numeros ganadores son: {ganadores}")
