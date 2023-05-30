num=int(input("Ingrese un numero: "))
if num>0:
    for i in range(2, num-1):
        if num%i==0:
            print("El numero no es primo. ")
            break
    print("El numero es par. " if num%2==0 else "El numero es impar. ")
    print("El numero es mayor a 50. " if num>50 else "El numero es menor a 50. ")