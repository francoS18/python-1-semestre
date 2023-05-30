print("# # # # # EJERCICIO 8.1 # # # # #")
print("Meses y su estacion correspondiente")
print("""
    _ _ _ _ _ _ _ _ _
    |                |
    |      Enero     | 
    |     Febrero    |    
    |      Marzo     |
    |      Abril     |
    |      Mayo      |
    |      Junio     |
    |      Julio     |
    |     Agosto     |
    |   Septiembre   |
    |     Octubre    |
    |    Noviembre   |
    |    Diciembre   |
    |_ _ _ _ _ _ _ _ |
""")
meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

#sw=True
while True:
    mes = input("¿Que mes desea consultar?\n ")
    mes = mes.title()
    if mes not in meses:
        print("Mes invalido")
        continue
    else:
        if mes == "Enero" or mes == "Febrero" or mes == "Marzo":
            print("El mes corresponde a la estacion de: Verano")
            #sw=False
        elif mes == "Abril" or mes == "Mayo" or mes == "Junio": 
            print("El mes corresponde a la estacion de: Otoño")
        elif mes == "Julio" or mes == "Agosto" or mes == "Septiembre":
            print("El mes corresponde a la estacion de: Invierno")
        elif mes == "Octubre" or mes == "Noviembre" or mes == "Diciembre" :
            print("El mes corresponde a la estacion de: Primavera")
        break
        