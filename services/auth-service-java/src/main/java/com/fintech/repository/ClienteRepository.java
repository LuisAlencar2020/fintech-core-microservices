package com.fintech.repository;

import com.fintech.model.Cliente;
import java.time.LocalDateTime;
import java.util.concurrent.atomic.AtomicLong;

public class ClienteRepository {
    private final AtomicLong proximoId = new AtomicLong(1);

    // Simula o salvamento no PostgreSQL; os dados permanecem apenas em memoria.
    public Cliente salvar(String nome, String cpf, String email) {
        Cliente clienteSalvo = new Cliente(
            proximoId.getAndIncrement(), nome, cpf, email, LocalDateTime.now()
        );

        System.out.println("[PostgreSQL simulado] Cliente cadastrado com ID " + clienteSalvo.id());
        return clienteSalvo;
    }
}
