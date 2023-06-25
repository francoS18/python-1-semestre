import random

lista = []

for i in range(20):
    lista.append(random.randint(40, 351))

print(lista)
lista.sort()
print(f"La lista ordena quedaría así:\n {lista}")

x = int(input("Escriba el numero que desea buscar: "))

if x in lista:
    print(f"El numero {x} se encuentra en la lista y se repite {lista.count(x)} veces")
else:
    print(f"El numero {x} no se encuentra en la lista")