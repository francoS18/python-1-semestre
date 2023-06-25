""". Crear un algoritmo que permita saber si un año es bisiesto (calendario gregoriano) desde el año 0 en adelante. Utilizar funciones para resolver el problema."""

def año_bisiesto(año):
    while True:
        if año <= 0:
            año = int(input("- Porfavor, indique un año válido: "))
            continue
        else:
            break 
    if año == 1582:
        print(f"| {año} | Esta en debate por el mes de octubre, ¿desde que fecha quiere saber? ")
        print("""
                  -------------------------------------------------------
                  1. Desde el 1 de octubre hasta el 4 de octubre de 1582.
                  
                  2. Desde el 15 de octubre de 1582 en adelante.
                  -------------------------------------------------------
                  """)
        while True:
            fecha = int(input("- "))
            if fecha <= 0 or fecha >= 3:
                print("           - Escoga una un numero que este dentro de las opciones - ")
                continue
            else:
                if fecha == 1:
                    print(f"\n| {año} | Es un año común")
                else:
                    print(f"\n| {año} | Es año bisiesto")   
            break      
    elif año <= 1581:
        print(f"\n| {año} | No está dentro del período del calendario gregoriano")
    else:
        if año % 4 != 0:
            print(f"\n| {año} | Es un año común")
        elif año % 100 != 0:
            print(f"\n| {año}| Es un año bisiesto")
        elif año % 400 != 0:
            print(f"\n| {año} | Es un año común")
        else:
            print(f"\n| {año} | Es un año bisiesto")
    return ''
        
año = int(input("\nIngrese el año: "))
comprobacion = año_bisiesto(año)
print(comprobacion)
