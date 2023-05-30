print("# # # # # EJERCICIO 1 # # # # #")

nums=[]
for i in range(3):
    num=int(input("Ingrese un numero para comprarlo: ".format(i+1)))
    nums.append(num)
num_max=max(nums)
num_min=min(nums)
print(f"El numero menor es {num_min} y el numero mayor es {num_max}")
