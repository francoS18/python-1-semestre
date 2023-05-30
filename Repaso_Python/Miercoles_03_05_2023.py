##### PRACTICA #####
##### SUELDO POR HORA #####
ht=float(input("Ingrese la cantidad de horas trabajadas: "))
ch=float(input("Ingrese el coste por hora: "))
sf=ht*ch
print("El sueldo correspondiente a las horas trabajadas y a lo que se paga por hora es de: ",sf)
##### SUMA ENTEROS #####
n=int(input("Ingrese un numero entero: "))
suma=n*(n+1)/2
print("La suma de los numeros enteros desde 1 hasta " + str(n)+ " es "+str(suma))
##### CALCULAR IMC #####
peso=int(input("Ingrese el peso en kg: "))
estatura=float(input("Ingrese la estatura: "))
imc=peso/estatura**2
print("tu indice de masa corporar(imc) es de: {:.2f}".format(imc),"\n")
##### CLASE #####
##### RETO #####
nombre=input("Ingrese su nombre: ")
edad=int(input("Ingrese su edad: "))
te=edad+20
print(f"Hola mi nombre es {nombre} y tengo {edad} años y en 20 años tendre {te} años.")
###### LISTAS #####
lista_texto="franco","pedro","juan","felipe","diego","bastian","luis","ana","bastian","sebastian"
lista_numero=1,4,6,2,7,0,9,4,5,1,4,6,8,7,6,9,1
lista_mixta= "franco",3,"bastian",4,"luis",2,"ana",1,"numeros",1,2,3,4
print(lista_mixta)
print(lista_numero)
print(lista_texto)
n=[1,2,4,5,6,7,8,9,10]
#05-Tuplas - (No Mutables)

newtupla= tuple()
grupo1=("franco",2,3,4,5,6,"sebastian","matias")
print("##### TUPLAS #####")

print(grupo1[1])
#consultar en que posicion se encuentra un elemento
print("indice del elemento:", grupo1.index("sebastian"))
print(grupo1[1:6])
#Reasignando el primer elemento de la tupla
#grupo1[1]= "alexis"
#print(grupo1)
##### LAS TUPLAS NO SE PUEDEN MODIFICAR #####
tuple=list(grupo1)
print("La tupla ahora es de tipo: ",type(grupo1),"\n")

#06-Sets(conjuntos)- Estructura fija
#Formas de inicializar un set
print("##### Sets #####")
conjunto_vacio=set()
conjunto_vacio1={}#diccionario o sets?
print(type(conjunto_vacio1))
conjunto_colores= set({"Azul","Rojo","Negro","Naranjo","Verde"})#Utilizando la funcion set
conjunto_animales= {"Gato","Perro","Caballo","Loro","Elefante"} #Utilizando llaves

print(type(conjunto_colores)) #tipo de dato set
print(type(conjunto_animales)) #tipo de dato set
print("El primer set contiene los siguientes colores",conjunto_colores)
print("El segundo set contiene los siguientes animales",conjunto_animales)
#print(conjunto_animales[0]) NO SE PUEDEN CONSULTAR ELEMENTOS, YA QUE SE GUARDA DE FORMA DESRODENADA Y CADA VEZ QUE SE ACTUALIZE CAMBIAN POSICIONES DE LOS ELEMENTOS
conjunto_colores.add=("Morado")
#listas = []
#Tuplas = ()
#conjuntos = {}