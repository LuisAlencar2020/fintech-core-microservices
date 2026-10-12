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




# 🚀 Fintech Open API & Microservices Hub
> **Plano de Estudo Prático de TI | Ecossistema Bancário**

---

## 📌 O que é este projeto?
Este projeto é um sistema para aprender como os bancos de verdade funcionam por dentro!

---

## 🧩 O que tem dentro da caixa?
* 🐍 **Python 3.9:** Para fazer cálculos rápidos e matemáticos.
* ☕ **Java 21:** Para guardar e organizar o dinheiro com segurança.
* 🌐 **JavaScript:** Para fazer as telinhas coloridas que o cliente vê.
* 🗄️ **Banco de Dados (PostgreSQL):** A gavetinha onde guardamos o nome das pessoas.
* 🐳 **Docker:** As caixas invisíveis que transportam os programas.

---

## 🎯 Lista de Tarefas (O que vamos construir)
- [x] Criar a caixa no GitHub e colar a placa README.md
- [x] Desenhar o banco de dados das continhas
- [ ] Fazer o código em Java para criar um cliente
- [ ] Fazer o código em Python para calcular o score

---
*Projeto criado para estudos de TI.*