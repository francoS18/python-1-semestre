import numpy as np

list_num1 = []
list_num2 = []

while True:
    num1 = float(input("Ingrese un numero flotante para añadir a la primera lista (Si quieres salir ingresa 0 ): "))
    if num1==0:
        print(list_num1)
        break
    else:
        list_num1.append(num1)

while True:
    num2 = float(input("Ingrese un numero flotante para añadir a la segunda lista (Si quieres salir ingresa 0 ): "))
    if num2==0:
        print(list_num2)
        break
    else:
        list_num2.append(num2)

def multiplicacion(list_num1,list_num2):
    multiplicacion_list=[]
    for i in list_num1:
        for k in list_num2:
            resultado = i*k
            multiplicacion_list.append(resultado)
    print(f"El resultado de la ultiplicacion es de: {multiplicacion_list}")

multiplicacion(list_num1,list_num2)

def division(list_num1,list_num2):
    division_list = []
    for i in list_num1:
        for k in list_num2:
            resultado= i/k
            division_list.append(resultado)
    print(f"La division de cada elemento de la lista es: {division_list}")

division(list_num1,list_num2)

listas_combinadas = list_num1.__add__(list_num2)
suma_list= sum(listas_combinadas)

def promedio(suma_list):
    promedio = np.mean(suma_list)
    return promedio

promedio(suma_list)

def mediana(listas_combinada): 
    mediana=np.median(listas_combinada)
    return mediana


