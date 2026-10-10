# fintech-core-microservices

# 🚀 Fintech Open API & Microservices Hub
> **Plano de Estudo Prático de TI | Ecossistema Bancário & Microsserviços** 

---

## 📌 Visão Geral do Projeto
O **Fintech Open API & Microservices Hub** é uma plataforma distribuída de simulação bancária para processamento de transações financeiras em tempo real, auditoria e inteligência de risco/score creditício. 

O objetivo primário deste repositório é aplicar, em um ecossistema real e versionado no GitHub, todos os tópicos do edital de Tecnologia da Informação.

---

## 🏗️ Arquitetura do Sistema

```text
                               ┌──────────────────────────┐
                               │   Frontend Dashboard     │
                               │  (JS / TS + React/Vue)   │
                               └────────────┬─────────────┘
                                            │ HTTP / REST / JWT
                                            ▼
                               ┌──────────────────────────┐
                               │       API Gateway        │
                               └───────┬──────────┬───────┘
                                       │          │
                     ┌─────────────────┘          └─────────────────┐
                     ▼                                              ▼
    ┌──────────────────────────────────┐          ┌──────────────────────────────────┐
    │       auth-service-java          │          │        analytics-python          │
    │  (Java 21 / Spring / Virtual)    │          │  (Python 3.9 / Algoritmos / ML)  │
    └────────────────┬─────────────────┘          └────────────────┬─────────────────┘
                     │                                             │
                     ▼                                             ▼
       ┌──────────────────────────┐                  ┌──────────────────────────┐
       │   PostgreSQL (Relacional)│                  │     Redis (NoSQL Cache)  │
       │   Modelo $1FN, 2FN, 3FN$ │                  │     Chave-Valor Rápido   │
       └──────────────────────────┘                  └──────────────────────────┘




