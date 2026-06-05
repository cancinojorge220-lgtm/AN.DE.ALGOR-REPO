# Algoritmo Recursivo: Suma de los Dígitos de un Número
# Entrada: 1234
# Salida: 10 (porque 1 + 2 + 3 + 4 = 10)

def suma_digitos(n):
    # Usamos el valor absoluto para manejar correctamente números negativos
    n = abs(n)
    # Caso base: si el número tiene un solo dígito (es menor a 10), la suma es el mismo número
    if n < 10:
        return n
    # Caso recursivo: sumar el último dígito (n % 10) con la suma de los dígitos del resto (n // 10)
    return (n % 10) + suma_digitos(n // 10)

if __name__ == "__main__":
    # Ejemplo de prueba indicado en la práctica
    entrada = 1234
    salida = suma_digitos(entrada)
    print("--- CASO A: SUMA DE LOS DÍGITOS DE UN NÚMERO ---")
    print(f"Entrada: {entrada}")
    print(f"Salida: {salida} (porque {' + '.join(list(str(entrada)))} = {salida})")
    
    # Entrada interactiva para demostración
    try:
        num_usuario = int(input("\nIngrese un número entero para probar con otro valor: "))
        print(f"La suma de los dígitos de {num_usuario} es: {suma_digitos(num_usuario)}")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")
