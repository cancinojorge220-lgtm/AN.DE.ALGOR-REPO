
# Complejidad O(n*m)

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def sumarMatriz(matriz):
    suma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            suma += matriz[i][j]
    return suma
    
print(f"La suma de la matiz es {sumarMatriz(matriz)}")