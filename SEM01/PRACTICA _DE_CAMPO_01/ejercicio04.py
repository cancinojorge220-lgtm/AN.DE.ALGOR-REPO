#EJERCICIO 4: TUPLAS
#Pregunta: ¿Por qué las tuplas son estructuras inmutables? 
#Las tuplas se definen como estructuras inmutables debido a que, tras su creación, no admiten modificaciones posteriores. 
#Esto implica la imposibilidad de añadir, suprimir o alterar sus elementos una vez han sido instanciados.
#Dicha propiedad resulta fundamental para garantizar la integridad de datos que deben permanecer constantes, 
#tales como coordenadas geográficas, fechas específicas o parámetros de configuración del sistema.

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