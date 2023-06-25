print("# # # # # EJERCICIO 3 # # # # #")

a = float(input("Ingrese un numero: "))
b = float(input("Ingrese otro numero: "))
c = float(input("Ingrese otro numero: "))

if a==b or a==c or b==c:
    print("El triangulo es isoseles")
elif a==b and a==c:
    print("El triangulo es equilatero")
else:
    print("El triangulo es escaleno")

p = (a+b+c)/2
area = (p*(p-a)*(p-b)*(p-c))**0.5
print(f"El area del triangulo es {area:.2f}")
