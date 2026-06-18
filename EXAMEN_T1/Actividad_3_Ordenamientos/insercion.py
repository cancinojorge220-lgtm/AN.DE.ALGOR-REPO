import sys; sys.path.append('..')
from datos_pedidos import pedidos

def insercion(lista):
    res = lista.copy()
    for i in range(1, len(res)):
        actual = res[i]
        j = i - 1
        while j >= 0 and res[j]["costo"] > actual["costo"]:
            res[j + 1] = res[j]
            j -= 1
        res[j + 1] = actual
    return res

print("Ordenado por Inserción:", insercion(pedidos))
