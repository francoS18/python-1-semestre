print("# # # # # EJERCICIO 8 # # # # #")
print("Meses y su estacion correspondiente")
print("""
    _ _ _ _ _ _ _ _ _
    |                |
    | 1.- Enero      | 
    | 2.- Febrero    | 
    | 3.- Marzo      |
    | 4.- Abril      |
    | 5.- Mayo       |
    | 6.- Junio      |
    | 7.- Julio      |
    | 8.- Agosto     |
    | 9.- Septiembre |
    | 10.- Octubre   |
    | 11.- Noviembre |
    | 12.- Diciembre |
    |_ _ _ _ _ _ _ _ |
""")
while True: 
    mes=int(input("¿Que mes desea consultar?\n"))
    if mes <=0 or mes>12:
        print("Mes invalido")
    else:
        break

if mes==1 or mes ==2 or mes == 3:
    print("Verano")
elif mes == 4 or mes == 5 or mes ==6: 
    print("Otoño")
elif mes == 7 or mes == 8  or mes == 9:
    print("Invierno")
elif mes == 10 or mes == 11 or mes == 12:
    print("Primavera")
else:
     print("Mes invalido.")
    