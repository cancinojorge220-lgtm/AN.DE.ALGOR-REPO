import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from datos_pedidos import pedidos

def burbuja(lista):
    res = lista.copy()
    n = len(res)
    for i in range(n):
        for j in range(0, n - i - 1):
            if res[j]["costo"] > res[j + 1]["costo"]:
                res[j], res[j + 1] = res[j + 1], res[j]
    return res

print("Antes:", pedidos)
print("Después:", burbuja(pedidos))
