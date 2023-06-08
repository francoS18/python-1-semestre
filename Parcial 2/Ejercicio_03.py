temperaturas_minimas= {9, 5, 2, 7, 6, 1}
temperaturas_maximas= {12, 14, 11, 10, 15, 9}
#se saca el numero repetido de las tuplas y se almacena en una variable.
num=temperaturas_minimas.intersection(temperaturas_maximas)
print("##### A #####")
#se verifica se el numero duplicado corresponde a "9"
if  num == {9}:
    print("si se repite el 9")
else:
    print("No se repite el 9")

print("##### B #####")

if 6 in temperaturas_maximas:
    print("si se encuentra el 6 en las temperaturas maximas")
else:
    print("No se encuentra el 6 en las temperaturas maximas")

if 6 in temperaturas_minimas:
    print("Si se encuentra el 6 en las temperaturas minimas")
else:
    print("No se encuentra el 6 en las temperaturas minimas")
if 17 in temperaturas_maximas:
    print("Si se encuentra el 17 en las temperaturas maximas")
else:
    print("No se encuentra el 17 en las temperaturas maximas")

if 17 in temperaturas_minimas:
    print("Si se encuentra el 17 en las temperaturas minimas")
else:
    print("No se encuentra el 17 en las temperaturas minimas")

for i in temperaturas_minimas:
    print(f"temperaturas minimas\n{i}={i**4}")

for i in temperaturas_maximas:
    print(f"temperaturas maximas\n{i}={i**4}")

union=temperaturas_maximas.union(temperaturas_minimas)
print(f"union de sets: {union}")