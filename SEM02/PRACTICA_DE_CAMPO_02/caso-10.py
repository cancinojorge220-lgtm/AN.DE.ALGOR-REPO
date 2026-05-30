# Complejidad O(n³)
# Tres Bucles Anidados (Tiempo Cúbico)

def encontrar_triplete(n):
    contador = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                if i**2 + j**2 == k**2:
                    print(f"Triplete pitagórico encontrado: {i}, {j}, {k}")
                    contador += 1
    return contador

n = int(input("Ingrese límite para buscar tripletes pitagóricos (ej. 15): "))
total = encontrar_triplete(n)
print(f"Total de tripletes encontrados: {total}")
