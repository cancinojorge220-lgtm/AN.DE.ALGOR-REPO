# Complejidad O(n) amortizada
# Bucle con terminación temprana (break)

def buscar_numero(lista, objetivo):
    for i in range(len(lista)):       
        if lista[i] == objetivo:
            print(f"Número {objetivo} encontrado en el índice {i}")
            break
    else:
        print(f"Número {objetivo} no encontrado.")

mi_lista = [10, 20, 30, 40, 50]
objetivo = int(input("Ingrese el objetivo a buscar: "))
buscar_numero(mi_lista, objetivo)
