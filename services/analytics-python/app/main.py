import os
import redis
from algorithms.quicksort import quicksort_transacoes

# Conexão com container NoSQL Redis usando as variáveis do docker-compose
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

def conectar_redis():
    try :
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db = 0, decode_responses=True)
        return r
    except Exception as e:
        print(f"⚠️ Erro ao conectar ao Redis: {e}")
        return None

def analisar_score_credito(cliente_nome, cliente_id, transacoes):
    print(f"Analisando score de crédito para o cliente: {cliente_nome} (ID: {cliente_id})")
    
    transacoes_ordenadas = quicksort_transacoes(transacoes)

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

    analisar_score_credito("João Silva", 1, historico_testes)