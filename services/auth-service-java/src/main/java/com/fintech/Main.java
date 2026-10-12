package com.fintech;

import com.fintech.model.Cliente;
import com.fintech.repository.ClienteRepository;

import java.util.concurrent.ExecutionException;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class Main {
    public static void main(String[] args) throws InterruptedException, ExecutionException {
        ClienteRepository repository = new ClienteRepository();

        System.out.println("Iniciando cadastro de clientes com virtual threads (Java 21)...");

        try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
            Future<?> joao = executor.submit(() -> {
                Cliente cliente = repository.salvar("Joao Silva", "12345678901", "joao@email.com");
                processarNotificacao(cliente);
            });
            Future<?> maria = executor.submit(() -> {
                Cliente cliente = repository.salvar("Maria Santos", "98765432100", "maria@email.com");
                processarNotificacao(cliente);
            });

            // get() propaga falhas das tarefas para que o processo nao indique sucesso indevidamente.
            joao.get();
            maria.get();
        }

        System.out.println("Cadastro e notificacoes concluidos.");
    }

    private static void processarNotificacao(Object obj) {
        if (obj instanceof Cliente c) {
            System.out.println("E-mail de boas-vindas enviado para: " + c.email());
        }
    }
}
