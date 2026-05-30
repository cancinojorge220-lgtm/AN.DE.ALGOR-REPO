# Complejidad O(n + m)
# Bucles Consecutivos (Lineal combinado)

def procesar_dos_listas(lista1, lista2):
    print("Procesando lista 1...")
    for elemento in lista1:
        if elemento > 0:
            print("Positivo")
            
    print("Procesando lista 2...")
    for elemento in lista2:
        if elemento < 0:
            print("Negativo")

lista_n = [1, 2, -1]
lista_m = [-3, -4, 5, 6]
procesar_dos_listas(lista_n, lista_m)
