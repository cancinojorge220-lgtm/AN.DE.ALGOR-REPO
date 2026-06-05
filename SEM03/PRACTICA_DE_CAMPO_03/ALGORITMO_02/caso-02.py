# Algoritmo Recursivo: Contar Ocurrencias de un Elemento en una Lista
# Entrada: lista = [1, 2, 3, 2, 2, 4], x = 2
# Salida: 3

def contar_ocurrencias(lista, x):
    # Caso base: si la lista está vacía, el elemento aparece 0 veces
    if not lista:
        return 0
    
    # Caso recursivo: verificar si el primer elemento coincide con 'x'
    primer_elemento_coincide = 1 if lista[0] == x else 0
    
    # Sumar la coincidencia del primer elemento con las coincidencias en el resto de la lista (lista[1:])
    return primer_elemento_coincide + contar_ocurrencias(lista[1:], x)

if __name__ == "__main__":
    # Ejemplo de prueba indicado en la práctica
    lista_prueba = [1, 2, 3, 2, 2, 4]
    x_prueba = 2
    resultado = contar_ocurrencias(lista_prueba, x_prueba)
    
    print("--- CASO B: CONTAR OCURRENCIAS DE UN ELEMENTO EN UNA LISTA ---")
    print(f"lista = {lista_prueba}")
    print(f"x = {x_prueba}")
    print(f"SALIDA = {resultado}")
