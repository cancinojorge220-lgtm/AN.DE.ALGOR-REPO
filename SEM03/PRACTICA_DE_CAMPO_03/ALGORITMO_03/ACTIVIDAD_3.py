# Lista de números
numeros = [3, 5, 1, 2, 8, 9, 4]

# Caso base: un solo elemento
def max_min(inicio, fin):

    # Si solo hay un elemento
    if inicio == fin:
        return numeros[inicio], numeros[inicio]

    # Si hay dos elementos
    if fin == inicio + 1:
        if numeros[inicio] > numeros[fin]:
            return numeros[inicio], numeros[fin]
        else:
            return numeros[fin], numeros[inicio]

    # Dividir la lista en dos partes
    medio = (inicio + fin) // 2

    # Resolver cada mitad
    max_izq, min_izq = max_min(inicio, medio)
    max_der, min_der = max_min(medio + 1, fin)

    # Combinar resultados
    if max_izq > max_der:
        maximo = max_izq
    else:
        maximo = max_der

    if min_izq < min_der:
        minimo = min_izq
    else:
        minimo = min_der

    return maximo, minimo


# Llamada inicial
maximo, minimo = max_min(0, len(numeros) - 1)

print("Lista:", numeros)
print("Máximo:", maximo)
print("Mínimo:", minimo)