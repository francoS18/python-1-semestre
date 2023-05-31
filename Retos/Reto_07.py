
def Diccionario_por_consola(frase_como_lista):
    for i in frase_como_lista:
        diccionario[i] = len(i)

while True:
    try:
        frase = input('Ingresa una frase: ')
        frase_sin_espacios= frase.replace(' ', '')
        if not frase_sin_espacios.isalpha():
            print('Ingresa una frase valida')
        else:
            break
    except:
        print('Ingresa una frase valida')

frase_como_lista = frase.split()

diccionario = {}

Diccionario_por_consola(frase_como_lista)
print(diccionario)