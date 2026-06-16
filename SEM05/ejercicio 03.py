
def minimo_movimientos(n):
    if n < 1:
        raise ValueError("n debe ser mayor o igual a 1")

    return (n + 1) // 3


n = int(input("Ingrese la posición final: "))
print("Mínimo de movimientos:", minimo_movimientos(n))