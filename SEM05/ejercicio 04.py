# Ejercicio 4: Máxima suma sin elementos consecutivos

numeros = [3, 2, 7, 10]

# Casos iniciales
if len(numeros) == 0:
    resultado = 0
elif len(numeros) == 1:
    resultado = numeros[0]
else:
    # Guardamos las mejores sumas previas
    anterior2 = numeros[0]
    anterior1 = max(numeros[0], numeros[1])

    # Recorremos el arreglo
    for i in range(2, len(numeros)):
        # Elegir entre tomar o no el elemento actual
        actual = max(anterior1, anterior2 + numeros[i])

        # Actualizamos valores
        anterior2 = anterior1
        anterior1 = actual

    resultado = anterior1

print("La máxima suma sin elementos consecutivos es:", resultado)