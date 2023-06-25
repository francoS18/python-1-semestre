# Utilizar una funcion que permita ingresar nombres para que el usuario ingrese nombres ´
# uno por uno. Los nombres se deben almacenar en una lista. Luego, crear otra funcion´
# que permita contar las letras, la cual debe recorrer la lista de nombres y cuente la canti- ´
# dad total de letras de todos los nombres ingresados. Por ultimo, crear una funci ´ on para ´
# que imprima los resultados y muestre en pantalla los nombres ingresados y el total de
# letras contadas.

lista_nombres=[]
cantidad_de_letras=[]
def Ingreso_de_nombre(lista_nombres,cantidad_de_letras):
    while True:
        nombre=input("""
        ###############################################         ##########################################
        # Ingrese un nombre para agregarlo a la lista #         # Si no desea continuar escribir "Salir" #
        ###############################################         ##########################################
        
        Nombre: """)
        if not nombre.isalpha():
            print("""
        ##############################################
        # Nombre invalido. Ingrese un nombre valido: #
        ##############################################""")
        elif nombre=="salir": 
            print(f"lista de nombres: {lista_nombres} y la suma total de letras: {total_letras}")
            break
        else:
            suma_de_letras=len(nombre)
            cantidad_de_letras.append(suma_de_letras)
            total_letras=sum(cantidad_de_letras)
            lista_nombres.append(nombre)
            continue

Ingreso_de_nombre(lista_nombres,cantidad_de_letras)