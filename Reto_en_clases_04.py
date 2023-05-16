pacientes = []
for i in range(3):
    nombre=input("Ingrese el nombre del paciente {}: ".format(i+1))
    peso=float(input("Ingrese el peso del paciente {} (kg): ".format(i+1)))
    estatura=float(input("Ingrese la estatura del paciente {} (m): ".format(i+1)))
    edad=input("Ingrese la edad del paciente: ")
    while not edad.isdigit() and int(edad) < 0:
        print("Edad invalida. Intente nuevamente.")
        edad=input("Ingrese la edad del paciente {}: ".format(i+1))
    pacientes.append((nombre,peso,estatura,edad))

print(pacientes)