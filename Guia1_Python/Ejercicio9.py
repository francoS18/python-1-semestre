print("# # # # # EJERCICIO 9 # # # # #")
numeros = [4, 3, 8, 12, 6, 10, 14, 3, 6]
print("Lista de numeros: ", numeros)
numeros.pop()
print("Lista de numeros sin el ultimo elemento: ", numeros)
numeros.insert(0, 2)
print("Lista de numeros con el numero 2 en la primera posicion: ", numeros)
numeros = list(set(numeros))
print("Lista de numeros sin duplicados: ", numeros)
print(f"Media de la lista de numeros:  {sum(numeros)/len(numeros):.1f}")
numeros.sort()
print("Mediana de la lista de numeros: ", numeros[int(len(numeros)/2)])

