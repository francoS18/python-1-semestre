#1. Elaborar un programa que permita capturar en una lista 10 elementos y un elemento a buscar en la lista. Se deberá imprimir: si el elemento existe en la lista el 
#mensaje “Elemento encontrado en la posición:”+índice , en caso contrario, se deberá imprimir el mensaje “El elemento buscado no existe en la lista”.

#lista1=["Franco","Sebastian","Bastian","Alexis","Luis","Ana","Toby","Princesa","Cacique","Guaton"]
#print(lista1)
#asignatura=["Matematicas","Programacion","Quimica","Ingenieria","Habilidades Comunicativas"]
#for asignatura in asignatura:
#    print("Yo estudio: ",asignatura)

#asignaturas=["Matematicas","Programacion","Quimica","Ingenieria","Habilidades Comunicativas"]
#notas=[]

#for i in asignaturas:
#    nota = float(input("¿Que nota has sacado en "+i+"?"))
#    notas.append(i)
#print(notas)

#for i in range(len(asignatura)):
    #print(f"En {asignatura[i]} has sacado +{nota[i]}")

awarded=[]
for i in range(6):
    awarded.append(int(input("Introduce numero ganador: ")))
    awarded.sort()
print("Los numeros ganadores son: "+str(awarded))