def knapsack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
                
    return K[n][W]

W = 10 
pesos = [2, 3, 5, 7] 
valores = [20, 30, 45, 50] 
n = len(valores)
valor_maximo = knapsack(W, pesos, valores, n)

print("PROBLEMA DE LA MOCHILA :")
print(f"Capacidad máxima: {W} kg")
print(f"Objetos disponibles (Peso, Valor):")
objetos = ['A', 'B', 'C', 'D']
for i in range(n):
    print(f"  Objeto {objetos[i]}: {pesos[i]} kg -> ${valores[i]}")

print("-" * 30)
print(f"El valor máximo óptimo que se puede transportar es: ${valor_maximo}")