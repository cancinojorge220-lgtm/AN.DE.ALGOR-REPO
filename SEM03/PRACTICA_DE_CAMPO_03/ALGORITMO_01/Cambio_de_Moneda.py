#01 ALGORITMO DE CAMBIO DE MONEDA

def cambio_monedas(monto, monedas):
    
    #Usamos centimos en lugar de centavos
    monto_centimos = round(monto * 100)

    #Convertimos la lista de monedas a centavos y ordenamos de mayor a menor
    monedas_centimos = [round(m * 100) for m in monedas]
    monedas_centimos.sort(reverse=True)
    
    resultado_centimos = []

    #Iteramos usando los valores en centavos
    for moneda in monedas_centimos:
        while monto_centimos >= moneda:
            monto_centimos -= moneda
            resultado_centimos.append(moneda)
            
    #Convertimos el resultado de vuelta a las monedas originales (decimales)
    resultado_final = [m / 100 for m in resultado_centimos]
    return resultado_final


#Valores de entrada
monto_cambio = 13.80 
sistema_monedas = [0.10, 0.20, 0.50, 1, 2, 5]

#Ejecutamos la función
vuelto = cambio_monedas(monto_cambio, sistema_monedas)

#Imprimimos el resultado de manera clara
print("1. ALGORITMO DE CAMBIO DE MONEDA")
print(f"Monto a cambiar: {monto_cambio}")
print(f"Monedas utilizadas: {vuelto}")
print(f"Total de monedas entregadas: {len(vuelto)}")