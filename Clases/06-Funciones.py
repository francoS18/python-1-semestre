print("# # # # # 01.Declarando una función simple # # # # #")
def mi_primera_funcion():
    print("Esta es mi primera funcion")

mi_primera_funcion()

print("# # # # # 02-Declarando una funcion y utilizando listas  # # # # #")

def concatenar(lista1,lista2):
    return lista1 + lista2
lista1 =[1,2,3]
lista2 = [4,5,6]

#Concatenar()
print(concatenar(lista1,lista2))

print("# # # # # 03-Declarando una funcion multiplicacion # # # # #")
def multiplicacion(num1,num2):
    return num1 * num2

#multiplicacion()
print(multiplicacion(5,50))

print("# # # # # 04-Funciones suma y resta # # # # #")

def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

a=int(input("Ingrese el valor de a: "))
b=int(input("Ingrese el valor de b: "))
#Se llama la funcion suma
resultado = suma(a,b)
print("la suma es de: ", resultado)

#Se llama a la funcion resta
resultado2=resta(a,b)
print("La resta es de: ", resultado2)