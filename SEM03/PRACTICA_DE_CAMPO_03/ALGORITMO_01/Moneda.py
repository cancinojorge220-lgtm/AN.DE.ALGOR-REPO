#01 Cambio de Moneda

def cambio_monedas(monto, monedas):
    
    #Lista para almacenar el resultado
    resultado = []

    #Ordenamos las monedas de mayor a menor
    monedas.sort(reverse=True)

    #Iteramos sobre las monedas y vamos restando el monto hasta que sea menor que la moneda actual
    for moneda in monedas:
        while monto >= moneda:
            monto -= moneda             #Restamos el valor de la moneda al total
            resultado.append(moneda)    #Agregamos la moneda al resultado
    return resultado


#Valores de entrada
monto_cambio = 63
sistema_monedas = [1, 2, 5]

# Ejecutamos la función
vuelto = cambio_monedas(monto_cambio, sistema_monedas)

# Imprimimos el resultado de manera clara
print("1. ALGORITMO DE CAMBIO DE MONEDA")
print(f"Monto a cambiar: {monto_cambio}")
print(f"Monedas utilizadas: {vuelto}")