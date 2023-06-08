palabra=input("Ingrese una palabra para verificar si es un palindromo: ")
while True:
    try:
        if not palabra.isalpha():
            print("La palabra es invalida.")
            palabra=input("Ingrese una nueva palabra valida: ")
        else:
            break
    except: 
        break

var=list(palabra)
var2=list(palabra)
var2.reverse()
if var == var2:
    print("La palabra si es un palindromo")
else: 
    print("La palabra no es un palindromo")