"""Este es un ejemplo de uso de la libreria de python"""

#01-DATOS DE TIPO NUMERICO

estatura = 1,72
peso = 70
complejo =1+4j

print("impresion del numero complejo:", complejo)

#OPERACION ARITMETICA BASICA

#imc = peso/estatura**2
#print(imc)
"""------------------------------------------------------------------------------------------------------------------"""
#02- DATOS DE TIPO DE CADENA DE CARACTERES

asignatura = "programacion"
carrera = "Ingenieria Civil Informatica"


"""------------------------------------------------------------------------------------------------------------------"""

# TYPE SABEMOS EL TIPO DE DATO QUE ESTAMOS TRATANDO
ampolleta = False
interruptor = True

#TYPE SABEMOS EL TIPO DE DATO QUE ESTAMOS TRATANDO
print(type(ampolleta))

"""------------------------------------------------------------------------------------------------------------------"""

#04 DATOS DE TIPO ARRAY (OBJETOS DE TIPO DE COLECCION)

estudiantes = ("Matias", "Marco", "Cristobal", "Sebastian")
num = (1,2,3,4,5,6)
print(estudiantes)
print(num)

#CLASE 11 DE ABRIL

#01-DATOS DE TIPO NUMERICO


print(f"mi estatura es de {estatura}y mi peso es de {peso}")

#OPERACION ARITMETICA 


#print("mi IMC es de: {:.2f}" .format(imc), "\n")

#FUNCIONES EXCLUSIVAS DEL PYTHON (STR(), INT(), FLOAT(), LEN(), TYPE())

#DATOS TIPO LIST (objetos de tipo coleccion) - (Mutabilidad)
print("########## 04-LISTAS #######3#")

#DECLARANDO E INICIALIZANDO UNA LISTA
nueva_lista = list()
print("Esta es una lista vacia:", nueva_lista)

otra_lista = []
print("Esta es otra lista vacia:", otra_lista)
print(type(otra_lista))

#DECLARANDO OTRAS LISTAS
estudiantes = ["Matias", "Marco", "Cristobal", "Sebastian", "Marco", "Boris"]
num = [1,2,3,4,5,6]
lenguaje = ["python"]

# ¿Se puede realizar una lista de datos
data = ["Osorno", {"UV": "nivel bajo", "Temp °C": 15}, (-40.5725, -70.8383)]

print("lista de cadena de caracteres:",estudiantes)
print("lista de numeros:", num)
print("lista de elemntos:", lenguaje)
print("esto igual es una lista:", data)
print(len(lenguaje)) #Para saber la cantidad de elementos de una 
print(num.count("Marco")) #Para cantidad de ocurrencia de su mismo elemento

lenguaje = ["JavaScript"]
print("Nuevo valor del arreglo de un elemento:", lenguaje)

#¿Como accedo a un elemento especifico de la lista?
print("posicion", estudiantes[0]) #¿Estara correcto?
print("posicion", estudiantes[1]) #¿Es el primer elemento?
print("posicion", estudiantes[3]) #¿Estara correcto?
print("posicion", estudiantes[4]) #¿Estara correcto?
print("posicion", estudiantes[5]) #¿Estara correcto?
print("posicion -2", estudiantes[-2]) #¿Estara correcto?
#iniciando otra lista de datos mixtos
data_asig = [10023, "programacion", 1, True]

#¿Que hace este codigo?
cod,ramo,semestre,estado = data_asig
print(ramo)

#¿Se pueden sumar listas?
print("suma de listas",estudiantes + num)

#¿Que hacen estas funciones?
print(list("Python"))
print(list(range(10)))
print("\n")

#03 - TUPLAS - (no son mutables)
grupo1 = ("Daniel","Cristian","Felipe",200,100,"Daniel")
print("######## 05-TUPLAS ###########") #{LLAVES}-[CORCHETES]-(PARENTESIS)
print(type(grupo1))

#Accediendo al primer elemento de la tupla
print(grupo1[0])

#Consultando el elemento "Daniel" cuantas veces se encuentra en la tupla
print("el elemento se repite: ", grupo1.count("Daniel"))

#Muestra el indice del primer elemento buscado
print("indice del elemento: ", grupo1.index ("Daniel"))

#Reasignando el primer elemento de la tupla
"""grupo1[0] = "Franco"
print(grupo1)"""

#¿Se pueden sumar tuplas?
grupo2 = ("Sebastian","Matias","boris","Cristian","Benjamin",10,20,30,500000)
print("Trozo de la tupla", grupo2[0:3])
#Obteniendo un trozo de la tupla
print(grupo1[2:4])
#Entonces como no puedo modificar una tupla,¿que puedo hacer?

grupo1 = list(grupo1)
print("la tupla ahora es de tipo:", type(grupo1),"\n")
print("\n")
#06 - SETS (Conjuntos)
#Formas de inicializar un set
conjunto_vacio = set()
print(type(conjunto_vacio))
conjunto_vacio1 = {} #¿Diccionario o set?
print(type(conjunto_vacio1))
conjunto_colores = set({"Azul","Rojo","Verde"}) #utilizando el conjunto set
print(type(conjunto_colores))
conjunto_animales = {"Gato","Perro","Lobo"}
#print(conjunto_animales[0])
print("el primer conjunto contiene los siguientes colores:", conjunto_colores)
print("el segundo conjunto contiene los siguientes animales:", conjunto_animales)

conjunto_colores.add("Celeste")
print("los colores actualizados son los siguientes:", conjunto_colores)
conjunto_animales.add("Foca")
print("los animales actualizados son los siguientes:", conjunto_animales)
"""-------------------------------------------------------------------------------"""
print("##### diccionario #####")
