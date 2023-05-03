"""Este es un ejemplo de uso de la libreria de python"""

#01-DATOS DE TIPO NUMERICO

edad = 18 # Entero(int)
estatura = 1.72 # Real(float)
peso = 70
complejo =1+4j

print("Transformando un valor real a un entero:", int(peso),"\n")
print("impresion del numero complejo:", complejo)
print("transformando un valor real a un entero:", float(edad), "\n")

#OPERACION ARITMETICA BASICA

imc = peso / estatura**2
print("mi imc es:{:.2f}".format(imc), "\n")
"""------------------------------------------------------------------------------------------------------------------"""
#02- DATOS DE TIPO DE CADENA DE CARACTERES
'utilizando la funcion len(cuenta la cantidad de caracteres)'

asignatura = "Programación"
carrera = "Ingeniería Civil Informática"
print("####### 02-STRINGS #####")
print(" la asignatura de",asignatura,"Corresponde a la carrera de",carrera)
print("la cantidad de caracteres de la palabra", asignatura,"es de:",len(asignatura))
print("la cantidad de caracteres de la palabra", carrera,"es de:",len(carrera))


"""------------------------------------------------------------------------------------------------------------------"""

#03-VALORES BOOLEANOS
ampolleta = False
interruptor = True

print('###### 03-BOOLEANS ######')
print(ampolleta,interruptor)
print("la variable ampolleta es de tipo", type(interruptor),"\n")
#TYPE SABEMOS EL TIPO DE DATO QUE ESTAMOS TRATANDO
'podemos transformar cualquie valor a un booleano (al igual que un string, int, etc.)'
print(bool(0))
print(bool(""))
print(bool(None))
print(bool(True))
print(bool(1))
print(bool("\in"))

"""------------------------------------------------------------------------------------------------------------------"""
'04-Datos tipo list(objeto de colección)-(mutables)'
print("##### 04-LISTAS #####")
nueva_lista= list()
otra_lista= []
print("Esta es una lista vacia:",nueva_lista)
print(" esta es otra lista vacia:", otra_lista)
print(type(otra_lista))
#04 DATOS DE TIPO ARRAY (OBJETOS DE TIPO DE COLECCION)

estudiantes = ("Matias", "Marco", "Cristobal", "Sebastian","Gerardo", "Gabriela", "Boris", "Yuliana", " Cristian", "Carlos", "Matias", "Juan", "Diego")
num = (1,2,4,5,6,2,5,4,4,5,7,1,2,4,1,2,4,6,2,4,5,2,1,1,8,6,5,6,4,9)
lenguaje =["Python"]
print(estudiantes)
print(num)

#OPERACIONES ARITMETICAS

'FUNCIONES EXCLUSIVAS DEL PYTHON (STR(), INT(), FLOAT(), LEN(), TYPE())'
'len en una lista cuenta la cantidad de elementos en una lista'
#DATOS TIPO LIST (objetos de tipo coleccion) - (Mutabilidad)
#¿Se puede realizar una lista de datos
data = ["Osorno", {"UV": "nivel bajo", "Temp °C": 15}, (-40.5725, -70.8383)]
lista_mixta= ["Felipe", 100, True, "Matias", 333, "Patricio Estrella"]
print("lista de cadena de caracteres:",estudiantes)
print("lista de numeros:", num)
print("lista de elemntos:", lenguaje)
print("esto igual es una lista:", data)
print("lista mixta:", lista_mixta)
print(len(lista_mixta)) #Para saber la cantidad de elementos de una 
print("la cantidad de veces que se repide", estudiantes.count("Marco")) #Para cantidad de ocurrencia de su mismo elemento
print("la cantidad de veces que se repite", num.count(1),"\n")

lenguaje = ["JavaScript"]
print("Nueva asignacion a la variable:", lenguaje)

'¿Como accedo a un elemento especifico de la lista? (### INDEX ###)'
'En cualquier lenguaje de programacion los Index parten desde el 0 en adelante'
print("posicion", estudiantes[10]) #correcto (1° elemento de la lista)
print("posicion", estudiantes[1]) #(2° elemento de la lista)
#print("posicion", estudiantes[13]) Inconrrecto
print("posicion -7", estudiantes[-7]) #Esta correcto
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

"""---------------------------------------------------------------------------------"""
'05 - TUPLAS - (no son mutables)'
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
'06 - SETS (Conjuntos)'
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
diccionario = dict()
diccionario={}

datos_personales = {
    "Nombre":"Victor",
    "Institución":"Ulagos",
    "Edad":29,
    "Asignaturas":{"Estructura de Datos","Programación"}
}
print(datos_personales)
print(datos_personales["Institución"])
datos_personales["Institución"] = "USS"
print("Diccionario actualizado", datos_personales)

#AÑADIR DATOS
datos_personales["Ciudad"] = "Osorno"
print("Diccionario con el nuevo campo", datos_personales)

#BORRAR DATOS
del datos_personales["Ciudad"]
print("Sin Osorno", datos_personales)