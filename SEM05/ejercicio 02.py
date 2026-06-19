# Ejercicio 2: Subir Escaleras
# Una persona puede subir 1 o 2 escalones por vez.
# Determinar cuántas formas distintas existen para subir n escalones.

def contar_formas(n):
    # Casos base
    if n == 0:
        return 1
    if n == 1:
        return 1

    # Crear arreglo para guardar resultados
    dp = [0] * (n + 1)

    # Inicializar casos base
    dp[0] = 1
    dp[1] = 1

    # Llenar la tabla
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


n = int(input("Ingrese el número de escalones: "))

formas = contar_formas(n)

print("Cantidad de formas distintas para subir la escalera:", formas)
