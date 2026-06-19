def fibonacci(n):
    if n == 0:
        return 0
        
    f = [0] * (n + 1)
    f[1] = 1
    
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
        55
                
    return f[n]

try:
    n = int(input("Ingresa un número entero n para calcular Fibonacci: "))
    
    if n < 0:
        print("Por favor, ingresa un número entero no negativo, mayor o igual a 0.")
    else:
        resultado = fibonacci(n)
        print(f"El término {n} de la serie de Fibonacci es: {resultado}")

except ValueError:
    print("Error: Debe ingresar un número entero válido.")