import os
import redis
from algorithms.quicksort import quicksort_transacoes

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

def conectar_redis():
    try:
        return redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, decode_responses=True)
    except Exception as e:
        print(f"⚠️ Erro ao conectar ao Redis: {e}")
        return None

def analisar_score_credito(cliente_nome, cliente_id, transacoes):
    print(f"\n📊 Analisando histórico para: {cliente_nome} (ID: {cliente_id})")
    
    transacoes_ordenadas = quicksort_transacoes(transacoes)
    
    if (total := sum(t['valor'] for t in transacoes)) > 1000.0:
        score = "ALTO (VIP)"
    elif total > 500.0:
        score = "MÉDIO"
    else:
        score = "BAIXO"

    print(f"⭐ Score Calculado: {score}")

    # Gravação no Banco NoSQL (Redis)
    if r := conectar_redis():
        chave_cache = f"score_cliente:{cliente_id}"
        r.set(chave_cache, score, ex=3600)
        print(f"⚡ [Redis NoSQL] Chave '{chave_cache}' salva com sucesso no Cache!")

    return score

if __name__ == "__main__":
    historico_testes = [
        {"id": 101, "valor": 1500.00},
        {"id": 102, "valor": 800.00},
        {"id": 103, "valor": 2000.00},
        {"id": 104, "valor": 300.00}
    ]
    analisar_score_credito("João Silva", 1, historico_testes)