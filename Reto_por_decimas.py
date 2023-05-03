##### Reto Decimas #####

ne=input("Ingrese el nombre del estudiante\n")
a=input("Ingrese la asignatura\n")
nl1=float(input("Ingrese nota del primer laboratorio\n"))
nl2=float(input("Ingrese nota del segundo laboratorio\n"))

ICINF = [ ne,a]

nf= nl1*0.3 + nl2*0.7

print("Nombre: ",ICINF[0])
print("Asignatura: ",ICINF[1])
print(f"La nota final es {nf:.1f}".format(nf))