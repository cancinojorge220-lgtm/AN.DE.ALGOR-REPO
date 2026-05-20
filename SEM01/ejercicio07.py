# EJERCICIO 7: BÚSQUEDA LINEAL
# ¿Por qué este algoritmo es considerado de fuerza bruta?
# Se considera de fuerza bruta porque revisa cada elemento de la lista secuencialmente 
# desde el principio hasta el final hasta encontrar el objetivo (o llegar al final), 
# sin usar ninguna heurística o información previa para optimizar la búsqueda.

import random

def busqueda_lineal():
    # Generar una lista de 10 números
    numeros = [random.randint(1, 100) for _ in range(10)]
    print(f"Lista generada: {numeros}")
    
    # Solicitar un número a buscar
    try:
        objetivo = int(input("Ingrese un número a buscar: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return
        
    # Búsqueda lineal
    encontrado = False
    for i in range(len(numeros)):
        if numeros[i] == objetivo:
            print(f"El número {objetivo} fue encontrado en la posición {i}.")
            encontrado = True
            break
            
    if not encontrado:
        print(f"El número {objetivo} no existe en la lista.")

if __name__ == "__main__":
    busqueda_lineal()
