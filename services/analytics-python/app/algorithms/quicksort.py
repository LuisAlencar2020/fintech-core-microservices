# Implementação manuel de QuickSort para ordenação de transações financeiras
# Estrutura de Dados e Algoritmos - Complexidade Média: 0 (n log n)
def quicksort_transacoes(transacoes):
    """ Ordena uma lista de transações (dicionários) pelo valor em ordem crescente utilizando o algoritmo QuickSort."""

    if len(transacoes) <= 1:
        return transacoes
    
        pivot = transacoes[len(transacoes) // 2]
        left = [x for x in transacoes if x < pivot]
        middle = [x for x in transacoes if x == pivot]
        right = [x for x in transacoes if x > pivot]
        return quicksort_transacoes(left) + middle + quicksort_transacoes   (right)

    return quicksort_transacoes(menores) + iguais + quicksort_transacoes(maiores)