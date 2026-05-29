# Complejidad O(n log n)
# Anidación de Lineal y Logarítmico

def algoritmo_combinado(n):
    for i in range(1, n + 1):
        j = n
        while j > 1:
            if j % 2 == 0:
                print(f"Iteración exterior {i}, interior {j}")
            j = j // 2

n = int(input("Ingrese un número n (ej. 8): "))
algoritmo_combinado(n)
