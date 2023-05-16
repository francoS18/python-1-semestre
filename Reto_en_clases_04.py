paciente=[]
for i in range(3):
    nombre=input("Ingrese el nombre del paciente {}: ".format(i+1))
    peso=input("Ingrese el peso del paciente {}: ".format(i+1))
    estatura=float(input("Ingrese la estatura del paciente {} ".format(i+1)))
    edad=input("Ingrese la edad del paciente {}".format(i+1))
    while not edad.isdigit() and int(edad)<0:
        print("Edad invalida. Intente nuevamente")
        edad= input("Ingrese la edad del paciente {} :".format(i+1))
        