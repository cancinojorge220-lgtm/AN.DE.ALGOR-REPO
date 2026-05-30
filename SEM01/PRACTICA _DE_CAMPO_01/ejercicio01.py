# EJERCICIO 1: OPERACIONES BÁSICAS

def operaciones_basicas():
    try:
        # Solicitar dos números enteros
        num1 = int(input("Ingrese el primer número entero: "))
        num2 = int(input("Ingrese el segundo número entero: "))
        
        # Calcular operaciones
        suma = num1 + num2
        resta = num1 - num2
        multiplicacion = num1 * num2
        
        # Mostrar resultados
        print("\nResultados:")
        print(f"Suma: {suma}")
        print(f"Resta: {resta}")
        print(f"Multiplicación: {multiplicacion}")
        
        if num2 != 0:
            division = num1 / num2
            print(f"División: {division}")
        else:
            print("División: No es posible dividir por cero.")
            
    except ValueError:
        print("Error: Por favor, ingrese solo números enteros.")

if __name__ == "__main__":
    operaciones_basicas()
