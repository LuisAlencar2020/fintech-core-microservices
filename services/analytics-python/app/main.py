import os
from algorithms.quicksort import quisort_transacoes

def analisar_score_credito(cliente_nome, transacoes):
    print(f"Analisando score de crédito para o cliente: {cliente_nome}")

    # 1. Aplicando o algoritmo QuickSort para ordenar as transações
    transacoes_ordenadas = quisort_transacoes(transacoes)
    print(f"Transações ordenadas por valor: {transacoes_ordenadas}") 
    for t in transacoes_ordenadas:
        print(f"    - ID : {t['id']}, Valor: R${t['valor']:.2f}")

    # 2. Uso de Walrus Operator (=:) recurso do python 3.9=
    # atribui o total da soma a variável 'total' e faz chegar no mesmo comando 'if'
    if (total := sum(t['valor'] for t in transacoes_ordenadas)) > 1000.0:
        score = "Alto (VIP)"
    elif (total := sum(t['valor'] for t in transacoes_ordenadas)) > 500.0:
        score = "MÉDIO"
    else:
        score = "BAIXO"

        print(f"💰 Total movimentado : R${total:.2f}")# Ordena as transações pelo valor utilizando QuickSort
        print(f"⭐ Score de crédito calculado: {score}\n")
    return score
    
if __name__ == "__main__":
    # Dados de teste de transações desordenadas
    historico_testes = [
        {"id": 101, "valor": 1500.0},
        {"id": 102, "valor": 800.0},
        {"id": 103, "valor": 2000.0},
        {"id": 104, "valor": 300.0}
    ]

    analisar_score_credito("João Silva", historico_testes)