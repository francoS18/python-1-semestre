print("# # # # # EJERCICIO 4 # # # # #")

nombre1=input("Ingrese un nombre: ")
nombre2=input("Ingrese otro nombre: ")

if nombre1[0]==nombre2[0]:
    print(f'Los nombres "{nombre1}" y "{nombre2}" comienzan con la misma letra')
elif nombre1[-1]==nombre2[-1]:
    print(f'Los nombres "{nombre1}" y "{nombre2}" terminan con la misma letra')
else:
    print(f'Los nombres "{nombre1}" y "{nombre2}" no comienzan ni terminan con la misma letra')