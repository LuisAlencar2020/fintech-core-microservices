-- Ver todas as contas com o nome do dono junto (usando JOIN)
SELECT c.nome, ct.numero_conta, ct.saldo 
FROM clientes c
JOIN contas ct ON c.id = ct.cliente_id;

-- Ver todas as contas com o nome do dono junto (usando JOIN)
SELECT c.nome, ct.numero_conta, ct.saldo 
FROM clientes c
JOIN contas ct ON c.id = ct.cliente_id;

-- Adicionando R$ 500 ao saldo da conta 1001-9
UPDATE contas 
SET saldo = saldo + 500.00 
WHERE numero_conta = '1001-9';

-- Remover uma conta do banco
DELETE FROM contas WHERE numero_conta = '1001-9';