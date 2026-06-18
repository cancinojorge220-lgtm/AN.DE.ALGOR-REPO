import sys; sys.path.append('..')
from datos_pedidos import pedidos

l1 = pedidos.copy()
i1 = 0
for i in range(len(l1)):
    for j in range(0, len(l1) - i - 1):
        i1 += 1
        if l1[j]["costo"] > l1[j + 1]["costo"]: l1[j], l1[j + 1] = l1[j + 1], l1[j]

l2 = pedidos.copy()
i2 = 0
for i in range(len(l2)):
    m = i
    for j in range(i + 1, len(l2)):
        i2 += 1
        if l2[j]["costo"] < l2[m]["costo"]: m = j
    l2[i], l2[m] = l2[m], l2[i]

l3 = pedidos.copy()
i3 = 0
for i in range(1, len(l3)):
    a = l3[i]
    j = i - 1
    while j >= 0:
        i3 += 1
        if l3[j]["costo"] > a["costo"]:
            l3[j + 1] = l3[j]
            j -= 1
        else: break
    l3[j + 1] = a

print("¿Mismo resultado?:", l1 == l2 == l3)
print(f"Iteraciones - Burbuja: {i1}, Selección: {i2}, Inserción: {i3}")
print("Conclusión: Inserción es más eficiente porque hace menos iteraciones.")
