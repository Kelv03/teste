import random
import time
#inserir o elemento na posição correta do "subarray" buscando um por um. 

def insertion_sort(arr):
    # Percorre da segunda posição até a última
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        # Move os elementos da arr[0..i-1], que são maiores que a chave, para uma posição à frente de sua posição atual
        while j >= 0 and chave < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave
    return arr

# Gerar uma lista de 10.000 elementos aleatórios
lista = [random.randint(0, 100000) for _ in range(10000)]

# Calcular o tempo para ordenar
inicio = time.time()
lista_ordenada = insertion_sort(lista)
fim = time.time()

tempo_total = fim - inicio
print(f"Tempo total para ordenar a lista de 10.000 elementos com Insertion Sort: {tempo_total} segundos")