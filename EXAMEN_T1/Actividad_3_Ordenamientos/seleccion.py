import sys; sys.path.append('..')
from datos_pedidos import pedidos

def seleccion(lista):
    res = lista.copy()
    n = len(res)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if res[j]["costo"] < res[min_idx]["costo"]:
                min_idx = j
        res[i], res[min_idx] = res[min_idx], res[i]
    return res

print("Ordenado por Selección:", seleccion(pedidos))
