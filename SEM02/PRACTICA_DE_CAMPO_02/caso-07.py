# Complejidad O(n * m)
# Bucles anidados de tamaños distintos

def multiplicar_elementos(lista1, lista2):
    for i in lista1:
        for j in lista2:
            if i == j:
                print(f"Iguales encontrados: {i} == {j}")

lista_n = [1, 2, 3]
lista_m = [3, 4, 1, 5]
multiplicar_elementos(lista_n, lista_m)
