
# O(log n)
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

def calcularMCD(numero1,numero2):
    while numero2 != 0:
        residuo = numero1%numero2 
        numero1 = numero2
        numero2 = residuo
    print(f"El MCD es: {numero1}")

calcularMCD(numero1,numero2)