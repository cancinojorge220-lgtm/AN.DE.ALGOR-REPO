#EJERCICIO 4: TUPLAS
LengProgramacion = ("Java","C#","Python","C++","Go")

#Mostrar Lenguajes de Programación
print("1. Lenguajes de Programación:")

for lp in LengProgramacion:
    print(" - " + lp)

#Mostrar el primer elemento
print("\n2. Primer Lenguaje de Programación:", LengProgramacion[0])

#Mostrar el último elemento
print("\n3. Último Lenguaje de Programación:", LengProgramacion[-1])

#Contar la cantidad de elementos
print("\n4. Cantidad de Lenguajes de Programación:", len(LengProgramacion))