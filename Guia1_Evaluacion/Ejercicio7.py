#Arrojamos mensajes de introducción para que el usuario sepa la función de la maquina
print("BIENVENIDO AL PROGRAMA QUE CALCULA EL FACTORIAL DE UN NUMERO")
print("Ingrese el numero al que le desea calcular el factorial")

#Creamos un bucle en el que declaramos la variable num que será registrada por consola, y se utilizará para calcular su factorial, en caso de que el digito ingresado sea negativo, el programa entrara en un bucle 
# hasta que el usuario ingrese un numero entero que sea positivo
while True:
    num = int(input())
    if num < 0:
        print("El programa esta diseñado para trabajar solo con números enteros que no sean negativos", "Porfavor ingrese otro numero")
        continue
    else:
        break

#Fijamos la base para nuestro factorial que será 1, que se multiplicará por todos los valores que va tomando numero_factorial a medida que el ciclo de for vaya realizando iteraciones
base_factorial = 1
for numero_factorial in range(1, num+1):
    base_factorial*=numero_factorial 
    
#Por ultimo arrojamos un mensaje con el resultado del numero que se quiera resolver y su solución de factorial
print("El factorial de ",num, "es: ", base_factorial)