import random
import time

def selection_sort(arr):
    n = len(arr)
    # Percorre todos os elementos da lista
    for i in range(n):
        # Encontra o menor elemento na sublista não ordenada
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Troca o menor elemento encontrado com o primeiro elemento da sublista não ordenada
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Gerar uma lista de 10.000 elementos aleatórios
lista = [random.randint(0, 100000) for _ in range(10000)]

# Calcular o tempo para ordenar
inicio = time.time()
lista_ordenada = selection_sort(lista)
fim = time.time()

tempo_total = fim - inicio
print(f"Tempo total para ordenar a lista de 10.000 elementos com Selection Sort: {tempo_total} segundos")