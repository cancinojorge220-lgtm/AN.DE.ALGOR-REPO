def generar_strings_backtracking(letras, largo, resultado=None, cadena_actual=""):
    if resultado is None:
        resultado = []

    # Caso base: si la cadena actual tiene el largo deseado
    if len(cadena_actual) == largo:
        resultado.append(cadena_actual)
        return resultado

    # Caso recursivo: intentar añadir cada letra disponible
    for letra in letras:
        cadena_actual += letra

        # Exploración recursiva
        generar_strings_backtracking(letras, largo, resultado, cadena_actual)

        # Backtracking: remover la última letra para probar otras combinaciones
        cadena_actual = cadena_actual[:-1]

    return resultado


def main():
    letras = ['a', 'b', 'c']
    largo = 3

    print("=" * 60)
    print(f"Generando todos los strings de largo {largo}")
    print(f"Letras disponibles: {letras}")
    print("=" * 60)

    strings = generar_strings_backtracking(letras, largo)

    # Mostrar resultados
    print(f"\nTotal de combinaciones generadas: {len(strings)}\n")

    for i, string in enumerate(strings, 1):
        print(f"{i:2d}. {string}")

    print("\n" + "=" * 60)
    print(f"Confirmación: 3^3 = {3**3} (combinaciones esperadas)")
    print("=" * 60)


if __name__ == "__main__":
    main()

