# Ejercicio 05: Problema de la mochila (Knapsack) con programación dinámica
def knapsack(W, wt, val, n):
    # Crear una matriz K para almacenar los valores máximos de subproblemas
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    
    # Llenar la matriz K de abajo hacia arriba
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    
    # Devolver el valor máximo que se puede obtener con la capacidad W
    return K[n][W]

# Datos de ejemplo para el problema de la mochila
W = 10 
pesos = [2, 3, 5, 7] 
valores = [20, 30, 45, 50] 
n = len(valores)
valor_maximo = knapsack(W, pesos, valores, n)

# Mostrar los resultados
print("PROBLEMA DE LA MOCHILA :")
print(f"Capacidad máxima: {W} kg")
print(f"Objetos disponibles (Peso, Valor):")
objetos = ['A', 'B', 'C', 'D']
for i in range(n):
    print(f"  Objeto {objetos[i]}: {pesos[i]} kg -> S/.{valores[i]}")

print("-" * 30)
print(f"El valor máximo óptimo que se puede transportar es: S/.{valor_maximo}")