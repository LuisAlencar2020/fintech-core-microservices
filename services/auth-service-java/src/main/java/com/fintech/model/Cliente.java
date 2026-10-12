package com.fintech.model;

import java.time.LocalDateTime;

/**
 * Record para representação imutável do Cliente (recurso moderno do Java SE 21).
 */
public record Cliente(
    Long id,
    String nome,
    String cpf,
    String email,
    LocalDateTime criadoEm
) {
    // Validação compacta no construtor
    public Cliente {
        if (cpf == null || !cpf.matches("\\d{11}")) {
            throw new IllegalArgumentException("CPF inválido! Deve conter exatamente 11 dígitos.");
        }
        if (email == null || !email.contains("@")) {
            throw new IllegalArgumentException("E-mail inválido!");
        }
    }
}
