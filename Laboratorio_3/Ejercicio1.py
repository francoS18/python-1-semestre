print("# # # # # Ejercicio 1 # # # # #")
print("")
#Creando un diccionario conformado por listas que almacenan datos de cada region.
ciudades= ["Valdivia", "Punta Arenas"]
superficie_l= 18_429
superficie_m= 1_382_291
habitantes_l= 404.432
habitantes_m= 166.533
#creando un nuevo modulo llamado densidad.
densidad_l= superficie_l/habitantes_l
densidad_m= superficie_m/habitantes_m
#Agregando la capital de cada region.
capital_l=["Valdivia"]
capital_m=["Punta Arenas"]
#Agregando un modulo llamado comunas.
comunas_l=["Río Bueno", "La Unión", "Paillaco"]
comunas_m=["Antartica Chilena","Magallanes","Tierra del Fuego","Ultima Esperanza"]
#Agregando un modulo llamado provincias en tuplas.
provicincias_l=("Valdivia", "Ranco")
provicincias_m=("Antartica Chilena","Magallanes","Tierra del Fuego","Ultima Esperanza")
dict1 = {"Región de Los Rios": [ciudades[0],superficie_l,habitantes_l,densidad_l,capital_l,comunas_l,provicincias_l],"Región de Magallanes": [ciudades[1],superficie_m,habitantes_m,densidad_m,capital_m,comunas_m,provicincias_m]}
print(dict1)