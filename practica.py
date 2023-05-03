print("Definir variables")
#Para definir una variable se debe escribir el nombre de la variable acompañada de un signo de = y lo que se quiere colocar
#Si la variable es un texto se debe ingresar entre "" y si es una variable de tipo numerico solo se debe ingresar la vaiable 
#Las variables de tipo numerico a la hora de combiarlas con otra variable de otro tipo se les debe agregra el comando (str(variable))
#ejemplos:
#Variable_numerica= 18
#Variable_texto= "Franco"
#print("Hola soy" + " " + Variable_texto +" y tengo" + " " + str(Variable_numerica) + " " + "años")
#Para ingresar un tipo de dato por consola se debe cambiar el comando print por el comado input por ejemplo:
Nombre= input ("hola, ¿como te llamas?\n") #el comando \n se utiliza para que a la hora de que el codigo se ejecute en consola se salte a la linea de abajo
print("Hola," + Nombre + " " + "un gusto conocerte")
edad= input("y ¿cuantos años tienes?\n")
print("asi que tienes" + " " + edad + " " + "años," + "bueno yo tengo 19 años")
ubicacion= input("¿Donde vives?" + " " + Nombre + "\n")
print(f"haber dejame repasar un poco tus datos, te llamas {Nombre}, tienes {edad} años y viven en {ubicacion}")
respuesta = input("¿Es Correcto?\n")
print("OK, entonces tengo buena memoria")
input("entonces, ¿me puedes repetir tu nombre porfavor?")

