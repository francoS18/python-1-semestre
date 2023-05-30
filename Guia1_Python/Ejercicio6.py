print("# # # # # EJERCICIO 6 # # # # #")
# Existen dos grupos de estudiantes de la carrera de Programacion que formaron
# sus grupos para elaborar el Laboratorio N°3. Los grupos son los siguientes:
#Grupo 1: Marcos, Gabriela, Benjamin, Matias
#Grupo 2: Marcos, Nicolas, Diego, Matias
# Se necesita saber si en ambos grupos tienen algun estudiante en comun y, en caso
# de que asi sea, imprimir los nombres de esos estudiantes. Todo esto utilizando
# Sets.
grupo1={"Marcos", "Gabriela", "Benjamin", "Matias"}
grupo2={"Marcos", "Nicolas", "Diego", "Matias"}
print("Grupo 1: ", grupo1)
print("Grupo 2: ", grupo2)
print("Estudiantes en comun: ", grupo1.intersection(grupo2))