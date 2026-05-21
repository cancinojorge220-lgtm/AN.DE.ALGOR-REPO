#EJERCICIO 3: LISTAS
#¿Qué ventajas ofrecen las listas frente a variables individuales?
#Las listas en Python permiten almacenar múltiples datos en una sola variable, 
# facilitando la organización, acceso y manipulación de la información de manera 
# más eficiente que usar muchas variables individuales.

# Lista para guardar los números
numeros = []

# Ingresar 8 números
for i in range(8):
    num = int(input("Ingrese un número: "))
    numeros.append(num)

# Mostrar elementos
print("Lista de números:", numeros)

# Mostrar mayor y menor
print("Número mayor:", max(numeros))
print("Número menor:", min(numeros))

# Mostrar suma total
print("Suma total:", sum(numeros))