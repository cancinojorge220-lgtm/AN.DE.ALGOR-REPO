# Complejidad O(n)

numeros = int(input("Ingrese un numero del 1 al 100: "))

numeros_impares = []

for numero in range(numeros):
    if(numero % 2 != 0):
        numeros_impares.append(numero)
        
print(numeros_impares)
