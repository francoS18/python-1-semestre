#Creamos las variables de las tarifas de los pagos
turno_diurno = 12000*10
turno_nocturno = 16000*10
dom_diurno = (12000+2000)*10
dom_nocturno = (16000+3000)*10  

#Definimos el diccionario de los empleados mas las tarifas de los dias de que ha trabajado
empleados = {
    1: {
        "Nombre" : "Boris",
        "Lunes" : turno_nocturno,
        "Martes" : turno_nocturno,
        "Miercoles" : turno_nocturno,
        "Jueves" : turno_diurno,
        "Viernes" : turno_diurno
        },
    
    2: {
        "Nombre" : "Franco",
        "Martes" : turno_nocturno,
        "Miercoles" : turno_nocturno,
        "Jueves" : turno_nocturno,
        "Domingo" : dom_diurno
        },
    
    3: {
        "Nombre" : "Cristian",
        "Miercoles" : turno_diurno,
        "Jueves" : turno_diurno,
        "Viernes" : turno_diurno,
        "Sabado" : turno_nocturno,
        "Domingo" : dom_nocturno
    }
}

#Arrojamos un print con la informacion de los empleados como un respaldo de informacion
print("""\n -EMPLEADOS- """,
      "\n1:", 
        "\nNombre :Boris",
        "\nLunes :", turno_nocturno,
        "\nMartes :", turno_nocturno,
        "\nMiercoles :", turno_nocturno,
        "\nJueves :", turno_diurno,
        "\nViernes :", turno_diurno,
        
        "\n2:", 
        "\nNombre : Franco""",
        "\nMartes :", turno_nocturno,
        "\nMiercoles :", turno_nocturno,
        "\nJueves :", turno_nocturno,
        "\nDomingo :", dom_diurno,
        
        "\n3:",
        "\nNombre : Cristian",
        "\nMiercoles :", turno_diurno,
        "\nJueves :", turno_diurno,
        "\nViernes :", turno_diurno,
        "\nSabado :", turno_nocturno,
        "\nDomingo :", dom_nocturno,
        )

#Arrojamos un print del 1er empleado mas la informacion de los dias que ha trabajado mas su pago diario correspondiente, y su pago semanal 
print("\nEmpleado 1:")
print("El pago diario nocturno del 1er empleado es:",turno_nocturno,'CLP',"\nEl pago diario diurno del 1er empleado es:",turno_diurno,'CLP',"\nEl pago semanal del 1er empleado es:",(turno_nocturno*3+turno_diurno*2),'CLP')

#Arrojamos un print del 2do empleado con su respectiva informacion de los dias que ha trabajado mas su pago diario correspondiente, y su pago semanal 
print("\nEmpleado 2:")
print("El pago diario nocturno del 2do empleado es:",turno_nocturno,'CLP',"\nEl pago diario diurno del 2do empleado es:",dom_diurno,'CLP',"\nEl pago semanal del 2do empleado es:",(turno_nocturno*3+dom_diurno),'CLP')

#Arrojamos un print del 3er empleado junto a la informacion de los dias que el ha trabajado mas su pago diario correspondiente, y su pago semanal  
print("\nEmpleado 3:")
print("El pago diario nocturno del 3er empleado es:",turno_nocturno+dom_nocturno,'CLP',"\nEl pago diario diurno del 3er empleado es:",turno_diurno,'CLP',"\nEl pago semanal del 3er empleado es:",(turno_nocturno+dom_nocturno+turno_diurno*3),'CLP')

#Agregamos al diccionario de empleados sus pagos diarios y su pago semanal de forma detallada
empleados[1]["Pago diario Lunes, Martes y Miercoles"] = (turno_nocturno )
empleados[1]["Pago diario Jueves y Viernes"] = (turno_diurno)
empleados[1]["Pago semanal"] = (turno_nocturno*3 + turno_diurno*2)

#Lo mismo hacemos con el 2do empleado, agregamos su informacion al diccionario ya creado, y lo actualizamos
empleados[2]["Pago diario Martes, Miercoles y Jueves"] = (turno_nocturno)
empleados[2]["Pago diario Domingo"] = (dom_diurno)
empleados[2]["Pago semanal"] = (turno_nocturno*3 + dom_diurno)

#Repetimos la accion con el ultimo empleado, y actualizamos la informacion del diccionario agregandole los datos recientemente creados
empleados[3]["Pago diario Miercoles, Jueves y  Viernes"] = (turno_diurno)
empleados[3]["Pago diario Sabado y Domingo"] = (turno_diurno, turno_nocturno)
empleados[3]["Pago semanal"] = (turno_nocturno + turno_diurno*3 + dom_nocturno)

#Por ultimo con for realizamos un recorrido en el que dias y tarifas ordena de manera estructurada el diccionario completo separandolos por secciones con \n y ':' para luego imprimnir el diccionario completo y ordenado
for dias, tarifas in empleados.items():
    print('\n',dias, ':', tarifas)