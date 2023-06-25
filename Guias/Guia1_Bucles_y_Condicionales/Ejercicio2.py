num=500
baja=44
todos_num=[]
todos_num.append(num)
while num<800:
    num=num-baja
    todos_num.append(num)
    sube=baja+10
    baja+=12
    num+=sube
    todos_num.append(num)
print("Los numeros son: ", todos_num)
print(f"La sumatoria es: {sum(todos_num)}")

