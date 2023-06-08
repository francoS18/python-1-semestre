# Desarrollar un programa que permita al usuario ingresar una serie de numeros enteros ´
# positivos (N numeros) hasta que ingrese -1 (S ´ olo positivos ignorando los n ´ umeros ne- ´
# gativos). Luego, el programa debe calcular e imprimir en pantalla lo siguiente: el numero ´
# mayor de los ingresados, la sumatoria total de los numeros, la sumatoria de los n ´ umeros ´
# pares, la sumatoria de los numeros impares y el promedio total. Adem ´ as, se debe impri- ´
# mir si el numero mayor obtenido es mayor, menor o igual que el promedio calculado. ´
# Asegurate de resolver este problema utilizando las funciones que consideres adecua- ´
# das.
# Nota: el -1 no se cuenta. Si el usuario ingresa un numero negativo debe volver a pedir un ´
# numero y no se usa en el calculo. ´
# Ejemplo: el usuario ingresa: 2, 3, 6, 7, 7, 9, -1 se debe imprimir en pantalla:
# La suma de pares es: 8
# La suma de impares es: 26
# La suma total es: 34
# El promedio es: 6
# El numero mayor ingresado fue: 9
# El numero es mayor que el promedio y este es 9

nums = []

def numeros_enteros():
    while True:
        try:
            x = int(input("""
                                                                                                            ##############################################
                                                                                                            Escribe "-1" cuando desee terminar el programa
                                                                                                            ##############################################
Ingresa un numero entero positivo: """))
            if x > 1:
                nums.append(x)
                print("""
                ##################
                Exelente! Sigamos!
                ##################
                """)
                continue
            elif x == -1:
                print("Haz finalizado el programa!")
                break
            else:
                print("""
                    ##########################################
                    Error: Escoge un numero positivo mayor a 0
                    ##########################################
                """)
        except ValueError:
            print("""
                #################################
                Error: Ingrese caracteres validos
                #################################       
            """)

# Luego, el programa debe calcular e imprimir en pantalla lo siguiente: el numero ´
# mayor de los ingresados,

def maxnum(nums):
    print(f"El numero mayor ingresado fue: {max(nums)}")

# sumatoria de todos los numeros

def sumatoria(nums):
    print(f"La sumatoria de todos los numeros ingresados es {sum(nums)}")

# sumatoria de todos los numeros pares

def sumatoria_pares(nums):
    pares = []
    for i in nums:
        if i % 2 == 0:
            pares.append(i)
    print(f"La sumatoria de todos los numeros pares ingresados es {sum(pares)}")

# sumatoria de todos los numeros impares

def sumatoria_impares(nums):
    impares = []
    for i in nums:
        if i % 2 != 0:
            impares.append(i)
    print(f"La sumatoria de todos los numeros impares ingresados es {sum(impares)}")

# promedio de todos los numeros ingresados en la consola

def promedio(nums):
    print(f"El promedio de todos los numeros ingresados es {round(sum(nums) / len(nums))}")

# comparar el numero mayor con el promedio para saber si es mayor, menor o igual al promedio

def comparar(nums):
    if max(nums) > sum(nums) / len(nums):
        print(f"El numero mayor es mayor que el promedio y este es {max(nums)}")
    elif max(nums) < sum(nums) / len(nums):
        print(f"El numero mayor es menor que el promedio y este es {max(nums)}")
    else:
        print(f"El numero mayor es igual que el promedio y este es {max(nums)}")

numeros_enteros()
sumatoria_pares(nums)
sumatoria_impares(nums)
sumatoria(nums)
promedio(nums)
maxnum(nums)
comparar(nums)