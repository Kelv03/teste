import random
import time

def bubble_sort(arr):
    n = len(arr)
    # Percorre todos os elementos da lista
    for i in range(n):
        # A flag troca é usada para otimização. Se não houver trocas em uma passada, a lista está ordenada.
        #troca = False
        # O último i elementos já estão ordenados, então não precisamos considerá-los
        for j in range(0, n - i - 1):
            # Troca se o elemento encontrado for maior que o próximo elemento
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                troca = True
        # Se nenhuma troca foi feita, a lista está ordenada
        #if not troca:
        #    break
    return arr

# Exemplo de uso
lista = [random.randint(0, 100000) for _ in range(10000)]
#lista = [64, 34, 25, 12, 22, 11, 90]
#print("Lista original:", lista)
inicio = time.time()
lista_ordenada = bubble_sort(lista)
fim = time.time()
#print("Lista ordenada:", lista_ordenada)


tempo_total = fim - inicio
print(f"Tempo total para ordenar a lista de 10.000 elementos: {tempo_total} segundos")