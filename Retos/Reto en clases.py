nombre = input("hola mi nombre es\n")
edad = input("y tengo\n")
print(type(edad))
edad_a_futuro = int(edad) + 20

formato = f"hola mi nombre es {nombre}, tengo {str(edad)} años y en 20 años tendre {str(edad_a_futuro)} años"
print(formato)