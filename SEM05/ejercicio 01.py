# Ejercicio 01: Fibonacci con programación dinámica
def fibonacci(n):
    # Caso base para n = 0
    if n == 0:
        return 0
    
    # Crear una lista para almacenar los valores de Fibonacci calculados
    f = [0] * (n + 1)
    f[1] = 1
    
    # Calcular los términos de Fibonacci desde 2 hasta n utilizando programación dinámica
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
        55
    
    # Devolver el término n de la serie de Fibonacci
    return f[n]

# Solicitar al usuario que ingrese un número entero n para calcular Fibonacci
try:
    n = int(input("Ingresa un número entero n para calcular Fibonacci: "))
    
    # Validar que n sea un número entero no negativo
    if n < 0:
        print("Por favor, ingresa un número entero no negativo, mayor o igual a 0.")
    else:
        resultado = fibonacci(n)
        print(f"El término {n} de la serie de Fibonacci es: {resultado}")

# Manejar el caso en que el usuario ingrese un valor no entero
except ValueError:
    print("Error: Debe ingresar un número entero válido.")