print("# # # # # Ejercicio 9.1 # # # # #")

numeros = [4, 3, 8, 12, 6, 10, 14, 3, 6] #Lista de numeros.
print("Lista de numeros: ",numeros) #Imprime la lista de numeros.
numeros.pop() #Aqui se elimina el ultimo numero de la lista.
print("Lista de numeros sin el ultimo elemento: ",numeros) 
numeros.insert(0,2) #Aqui se agrega el numero 2 en la primera posicion de la lista.
print("Lista con el numero agregado: ",numeros)
numeros=list(set(numeros)) #Se utiliza el set para eliminar los numeros diplicados de la lista.
print("Numeros sin duplicados: ",numeros)
print(f"Media de la lista de numeros {sum(numeros)/len(numeros):.1f}") #Se calcula la media de la lista de numeros.
print("Suma de los numeros de la lista: ",sum(numeros)) #para sumar todos los nuemeros de la lista se utiliza el comando sum(lista)
numeros.sort() #Se ordenan los numeros de la lista de menor a mayor.
print(f"La mediana de los numeros de la lista: {numeros[int(len(numeros)/2)]} ") #Se calcula la mediana de la lista de numeros.