-- 1. Criar a tabela de Clientes (Gaveta 1)
CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,             -- Código único gerado automaticamente
    nome VARCHAR(100) NOT NULL,        -- Nome do cliente (texto)
    cpf VARCHAR(11) UNIQUE NOT NULL,   -- CPF único (não pode ter dois iguais)
    email VARCHAR(100) UNIQUE NOT NULL,-- E-mail do cliente
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Criar a tabela de Contas Bancárias (Gaveta 2)
CREATE TABLE contas (
    id SERIAL PRIMARY KEY,             -- Código único da conta
    numero_conta VARCHAR(20) UNIQUE NOT NULL,
    saldo NUMERIC(15, 2) DEFAULT 0.00, -- Guarda dinheiro com centavos (ex: 1500.50)
    cliente_id INT NOT NULL,           -- Chave Estrangeira (aponta para quem é o dono na tabela clientes)
    
    -- Ligação entre as duas gavetas (Relacionamento)
    CONSTRAINT fk_cliente FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON DELETE CASCADE
);