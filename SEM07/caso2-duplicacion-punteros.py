def duplicar_notas():
    notas_originales = []
    print("--- Ingreso de Notas ---")
    for i in range(5):
        while True:
            try:
                nota = float(input(f"Ingrese la nota {i+1}: "))
                notas_originales.append(nota)
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")

    # Usamos .copy() para duplicar los DATOS en otra dirección de memoria.
    notas_copia = notas_originales.copy()
    # Mostrar ambos arreglos en pantalla
    print("\n--- Resultados ---")
    print(f"Arreglo original (ref: {id(notas_originales)}): {notas_originales}")
    print(f"Arreglo duplicado (ref: {id(notas_copia)}): {notas_copia}")

    # Liberar toda la memoria utilizada
    del notas_originales
    del notas_copia
    print("\nMemoria liberada correctamente.")

# Ejecutar la función
duplicar_notas()