#Ejemplo 01: Distribución de Billetes en un Cajero Automático

def entregar_dinero(cantidad,billetes):
    resultado = []
    for billete in billetes:
        while cantidad >= billete:            
            cantidad -= billete
            resultado.append(billete)
            print(f"- Entregar billete de {billete}")
    return resultado

#Valor a Retirar
MontoRetirar = 380
#Disponibilidad de Billetes en el Cajero
billetes = [200, 100, 50, 20, 10] 

print(f"Cantidad a retirar: {MontoRetirar}")
print(f"Cantidad de Billetes a entregar: {len(entregar_dinero(MontoRetirar, billetes))}")

