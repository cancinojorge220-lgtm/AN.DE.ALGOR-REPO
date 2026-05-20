# EJERCICIO 9: NÚMERO MAYOR SIN UTILIZAR MAX()
# ¿Cuál es la complejidad temporal de este algoritmo?
# La complejidad temporal es O(n), donde n es el número de elementos en la lista. 
# Esto se debe a que el algoritmo debe iterar una vez por cada elemento de la lista 
# para realizar la comparación.

def encontrar_mayor():
    # Lista de ejemplo
    numeros = [45, 23, 89, 12, 67, 98, 34, 5, 77]
    print(f"Lista de números: {numeros}")
    
    if not numeros:
        print("La lista está vacía.")
        return
        
    # Inicializar el mayor con el primer elemento
    mayor = numeros[0]
    print(f"Asumiendo inicialmente que el mayor es el primer elemento: {mayor}")
    
    # Proceso de comparación
    for i in range(1, len(numeros)):
        actual = numeros[i]
        print(f"Comparando mayor actual ({mayor}) con el siguiente elemento ({actual}):", end=" ")
        
        if actual > mayor:
            print(f"¡{actual} es mayor! Nuevo número mayor.")
            mayor = actual
        else:
            print(f"{actual} no es mayor, se mantiene {mayor}.")
            
    print(f"\nEl número mayor final de la lista es: {mayor}")

if __name__ == "__main__":
    encontrar_mayor()
