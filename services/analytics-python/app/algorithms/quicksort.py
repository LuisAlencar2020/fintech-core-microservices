# Implementação manuel de QuickSort para ordenação de transações financeiras
# Estrutura de Dados e Algoritmos - Complexidade Média: 0 (n log n)
from turtle import left


def quicksort_transacoes(transacoes):
    """ Ordena uma lista de transações (dicionários) pelo valor em ordem crescente utilizando o algoritmo QuickSort."""

    if len(transacoes) <= 1:
        return transacoes
    pivot = transacoes[len(transacoes) // 2]
    menor = [x for x in transacoes if x < pivot]
    igual = [x for x in transacoes if x == pivot]
    maior = [x for x in transacoes if x > pivot]
    return quicksort_transacoes(menor) + igual + quicksort_transacoes(maior)