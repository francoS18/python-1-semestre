print("# # # # # Ejercico 2 # # # # #")

palabra1=input("Ingrese una palabra: ")
palabra2=input("Ingrese otra palabra: ")

if len(palabra1) > len(palabra2):
    print(f'La palabra "{palabra1}" tiene mas letras que la palabra "{palabra2}"')
elif len(palabra2) > len(palabra1):
    print(f'La palabra "{palabra2}" tiene mas letras que la palabra "{palabra1}"')
else:
    print(f'Las palabras "{palabra1}" y "{palabra2}" tienen las misma cantidad de caracteres')