# EJERCICIO 2: PROMEDIO DE NOTAS
# Pregunta de análisis: ¿Qué ventajas tiene Python para resolver operaciones matemáticas?
# Respuesta: Python tiene una sintaxis muy clara, limpia y parecida al lenguaje matemático común. 
# No requiere declarar tipos de variables explícitamente para los cálculos y maneja enteros 
# de tamaño arbitrario de forma nativa. Además, incluye operadores matemáticos directos (como // para 
# división entera o ** para potencia) y cuenta con potentes bibliotecas estándar (como 'math') para cálculos más complejos.

def calcular_promedio():
    notas = []
    
    print("Ingrese 4 notas:")
    for i in range(4):
        while True:
            try:
                nota = float(input(f"Nota {i+1}: "))
                if 0 <= nota <= 20: # Asumiendo escala de notas de 0 a 20
                    notas.append(nota)
                    break
                else:
                    print("Por favor, ingrese una nota válida (entre 0 y 20).")
            except ValueError:
                print("Error: Ingrese un valor numérico.")
                
    # Calcular promedio final
    promedio = sum(notas) / len(notas)
    
    # Determinar condición
    if promedio >= 11:
        condicion = "Aprobado"
    else:
        condicion = "Desaprobado"
        
    # Mostrar resultados
    print("\nResultados:")
    print(f"Promedio final: {promedio:.2f}")
    print(f"Condición: {condicion}")

if __name__ == "__main__":
    calcular_promedio()
