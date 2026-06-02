# Complejidad O(n)

numero = int(input("Ingrese un numero del 1 al 100: ")) 

def encontrarNumerosImpares(numero):
    numeros_impares = []
    for numero in range(numero):
        if(numero % 2 != 0):
            numeros_impares.append(numero)
    return numeros_impares
        
print(encontrarNumerosImpares(numero))
