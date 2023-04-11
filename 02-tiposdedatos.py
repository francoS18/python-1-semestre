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
print("posicion", estudiantes[3])
print("posicion", estudiantes[4]) #¿Estara correcto?
print("posicion", estudiantes[5])
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
