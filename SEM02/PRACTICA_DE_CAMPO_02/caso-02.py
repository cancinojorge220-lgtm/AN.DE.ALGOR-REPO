
# Complejidad O(n2)

def existeDuplicados(numeros):
    duplicado = False
    for i in range(len(numeros)):
        for j in range(i+1,len(numeros)):
            if(numeros[i] == numeros[j]):
                duplicado = True
                break
    return duplicado

print(existeDuplicados([4,8,15,16,23,42,8]))
