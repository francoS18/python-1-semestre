a = [21,8,15,3,12]
b = [10,9,12,15,18]
c = [2,3,8,9,12]
l3=a+b+c
print("Lista 3: ",l3)
l3.insert(-1,20)
print("Lista con el 20 agregado en la penultima pocision: ",l3)
l3.reverse()
print("Lista ordenada de forma inversa: ",l3)
d=[4,5,6]
l3=l3+d
print("Lista 3 + nueva lista: ",l3)
suma=sum(l3)
print("suma de todos los numeros de la lista: ",suma)
promedio=suma/len(l3)
print("Promedio de la lista final: ",promedio)