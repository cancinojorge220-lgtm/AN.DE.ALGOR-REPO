# Complejidad O(n2)

def cantidadApariciones(arr):
    for i in range(len(arr)):
        contador = 0
        for j in range(len(arr)):
            if(arr[i]== arr[j]):
                contador += 1
        print(f"{arr[i]} aparece - {contador} veces")
    
cantidadApariciones([1,2,2,3,3,3,4])