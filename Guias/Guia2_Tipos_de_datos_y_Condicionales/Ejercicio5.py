print("# # # # # EJERCICIO 5 # # # # #")

notas=[]
for i in range(3):
    nota=float(input("Ingrese nota: "))
    while not 0<=nota<=7:
        print("Nota no valida")
        nota=float(input("Ingrese nota: "))
    notas.append(nota)
promedio=(notas[0]*0.3)+(notas[1]*0.4)+(notas[2]*0.3)
if promedio>=4:
    print(f"El promedio ponderado es: {promedio:.2f} y el alumno esta aprobado")
elif promedio<6:
    print(f"El promedio ponderado es: {promedio:.2f} y el alumno esta aprobado con disticion")
else:
    print(f"El promedio ponderado es: {promedio:.2f} y el alumno esta reprobado")
