print("##### FUNCION print() #####")

print("¡Hola Mundo!")
print("hola","como","estas",sep="___",end="***") #El termino "sep="" se usa para los espacios entre cadenas y se le agrega que simbolo quiere que se represente en consola.
print("que","bueno") #Mientras que el "end=" conecta la siguiente linea de codigo y tambien se le debe asignar un simbolo que lo represente en consola.

print("##### ENTEROS Y FLOTANTES #####")
print(0o123) #Para hacer un calculo octal se debe usar (0o).
print(0x123) #Para hacer un calculo decimal se debe usar (0x).
print(.4) #Para escribir un numero flotante que lleve un solo digito delantes y ese digito sea un 0.
print(4.) #Para escribir un numero flotante que lleve un solo digito detras y ese digito sea un 0.
print(3e8) #Para expresar una potencia se utiliza la "E" o "e" que toma como base de potencia el 10.
#El numero anterior al "e" puede ser entero o flotante y el valor despues de la "e" debe ser entero).
print(0.0000000000000000000001) #Python siempre busca a representacion mas simple.

print("##### CADENAS #####")

print("Yo soy una cadena")#Las cadenas necesitan usar comillas.
print("Me gusta \"Monty Python\"") #Para expresar comillas se utiliza el caracter de escape "\". " 
print('mMe gusta "Monty Python"') #La otra forma es utilizando un apostrofe para iniciar la cadena y no una comilla.
print("I'm Monty Python")
print('I\'m Monty Python')
print("") #Esto sigue siendo una cadena.
print('') #Al igual que esto sigue siendo una cadena.

print("##### BOOLEANOS #####")

print(True<False)
print(True>False)
print("\"Estoy\"\n\"\"Aprendiendo\"\"\n\"\"\"Python\"\"\"")

print("##### OPERADORES #####")

print("##### SUMA #####")

print(2+2) 
print(-4+4)
print(-4.+8)
print(+2) #Esto es con un signo Unario.

print("##### POTENCIAS #####")

print(2**3) #Los signos "**" se utilizan para realizar una operacion de potencia, siendo que el numero que va despues de los signos terminaria siendo el exponente.
print(2**3.) #Mismo ejercicio de arriba solo que con un exponente de numero flotante que lleva un 0 solo que esta escrito de forma abreviada(es lo mismoq que escribir 2**3.0)
print(2.**3) #Mismo ejercicio de arriba solo que con una base de numero flotante que lleva un 0  solo que esta escrito de forma abreviada(es lo mismo que escribir 2.0**3)
print(2.**3.) #Al igual que arriba, slo que lleva una base y exponente de tipo flotante(es lo mismo que escribir 2.0**3.0)
#Cuando ambos numeros de ** son enteros el resultado es entero, pero si uno es flotante el resultado se vuelve automaticamente un flotante.

print("##### MULTIPLICACION #####")

print(2*3)
print(2*3.)
print(2.*3)
print(2.*3.)
#Cuando ambos numeros de * son enteros el resultado es entero, pero si uno es flotante el resultado se vuelve automaticamente un flotante.

print("##### DIVISION #####")

print(6/3)
print(6/3.)
print(6./3)
print(6./3.)
#Al realizar una division con / el resultado siempre es un numero flotante.

print("##### DIVISION ENTERA #####")

print(6//3)
print(6//3.)
print(6.//3)
print(6.//3.)
#Al realizar una division de enteros con el signo // da un resultado de enteros, pero si se realiza con algun numero flotante da como resultado un numero flotante.
print(6//4)
print(6.//4)
#Al realizar este tipo de division el resultado es un numero flotante que se redondea siempre hacia abajo.
print(6/4)
print(6./4)
#Al realizar este tipo de division el resultado es un numero flotante con una division bien realizada.
print(-6//4)
print(6.-4)
#Al realizar esta division se redondea al numero menor entero, por eso el resultado.

print("##### RESIDUOS(MODULO) #####")

print(14%4)
print(12%4.5)
#El residuo es lo que sobra de una division de enteros.

print("##### RESTA #####")

print(-4-4)
print(4.-8)
print(-1.1) #Esto es con un signo Unario.

print("##### OPERADORES Y SUS PRIORIDADES #####")

print(2+3*5) #Python tiene en cuenta la jerarquia tipica y empieza por los signos de mayor jerarquia en este caso el signo "*".

print("##### OPERADORES Y SUS ENLACES #####")

print(9%6%2) #Las operaciones se realizan de izquerda a derecha.
print(2**2**3) #Las potencias son las excepciones a esta regla.
print(-3**2)
print(-2**3)
print(-(3**2))

print("##### LISTA DE PRIORIDADES #####")

print("1.- ** ")
print("2.- + y - ") #(Unario) Los operadores unarios a la derecha del operador exponencial enlazan con mayor fuerza. 
print("3.- * , / , // , % ")
print("4.- + , - ") #Binario
print(2*3%5) #Esta operacion se realiza de izquierda a derecha ya que tienen el mismo nivel de prioridad.

print("##### OPERADORES Y PARENTESIS #####")

print((5 * ((25 % 13) + 100) / (2 * 13)) // 2) #Al realizar operaciones con parentesis esto toman mayor prioridad que el resto de los signos.

print("##### EJERCICIOS FINALES #####")

print((2**4),(2*4.),(2*4)) #¿Que se representaria en la pantalla?
print((-2/4),(2/4),(2//4),(-2//4)) #¿Que se representaria en la pantalla?
print((2%-4),(2%4),(2**3**2)) #¿Que se representaria en la pantalla?

print("##### VARIABLES #####")

#Palabras claves de python:['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
#'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
#Estas palabras no se pueden asignar como variables, a menos de que cambian las mayusculas y minusculas de la palabra.
#Por ejemplo: import / se puede escribir como Import.

var=1 #Esto es una variable.
account_balance=1000.0
client_name="John Doe"
print(var,account_balance,client_name)
print(var)
#No se puede utilizar una variable que no existe, por ejemplo print(Var).
version="3.8.5"
print("Python version: " + version)
var=var+1
print(var)
var=100
var=200+300
print(var)
a=3.0
b=4.0
c=(a**2+b**2)**.5
print("c= ",c)
juan=3
maria=5
adan=6
print(juan,maria,adan,sep=",") #Una forma de escribirlo.
print("Juan tenia: ",juan," Manzanas, Maria tenia: ",maria," Manzanas, Adan tenia: ",adan," Manzanas.") #Otra mas especifica y clara.
manzanas_totales=juan+maria+adan
print("En total habian: ",manzanas_totales," Manzanas.")
x=3
x*=2 #Forma mas abreviada de escribir x=x*2
Ovejas=1
Ovejas+=1 #Forma abreviadas de escribir Ovejas=Ovejas+1
#Expresion: i = i + 2 * j
#Abreviado: i += 2 * j
#Expresion: var = var / 2
#Abreviado: var /= 2
#Expresion: rem = rem % 10
#Abreviado: rem %= 10
#Expresion: j = j - (i + var + rem)
#Abreviado: j -= (i + var + rem)
#Expresion: x = x ** 2
#Abreviado: x **= 2

print("##### VARIABLES UN CONVERTIDOR #####")

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "millas son", round(miles_to_kilometers,2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")

print("##### EJERCICIOS DE OPERACIONES #####")
x=0
x=float(x)
y=3*x**3-2*x**2+3*x-1
print("y= ",y)

x=1
x=float(x)
y=3*x**3-2*x**2+3*x-1
print("y= ",y)

x=-1
x=float(x)
y=3*x**3-2*x**2+3*x-1
print("Y= ",y)

print("##### RETROALIMENTACION #####")

var = 2
var = 3
print(var)
 
a = '1'
b = "1"
print(a + b)

a = 6
b = 3
a /= 2 * b
print(a)

print("##### COMENTARIOS #####")

#Los comentarios se realizan para que quede mas laro y legible un codigo para un programador, los buenos programadores dejan comentado las partes mas importantes de su codigo.
#Tambien es bueno comentar fragmentos de codigos para encontrar algun tipo de error en el codigo(se puede ir comentando y descomentando codigos hasta encontrar la solucion.)
#Los comentarios no son leidos por el codigo de programacion, simplemente sirve de apoyo.
#Para comentar un codigo se debe utilizar el simpbolo de #

print("##### INTERACCION CON EL USUARIO #####")

print("Dime lo que sea ...")
anything=input()
print("Hmmm...",anything,"...¿en serio?")


# != significa diferente(No es igual a)
# | prioridad de operadores | operadores |
# |          1	            |     +, -	 |
# |          2	            |     **	 |
# |          3     	        | *, /, //, %|	
# |          4              |	+, -	 |
# |          5              |<, <=, >, >=|	
# |          6	            |   ==, !=   |

