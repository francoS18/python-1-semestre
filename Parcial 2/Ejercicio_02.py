num=1
lista_de_numeros=[num]
print(lista_de_numeros)
for i in range(10):
    num=num+1
    lista_de_numeros.append(num)
    lista_de_numeros.append(num+1)
    lista_de_numeros.remove(lista_de_numeros[0])
    #lista_de_numeros.insert()
    print(lista_de_numeros)

