# Estágio 1: Build da Aplicação com Maven/Java 21
FROM eclipse-temurin:21-jdk-alpine AS builder
WORKDIR /app
COPY . .
RUN javac -d bin src/main/java/com/fintech/model/Cliente.java \
            src/main/java/com/fintech/repository/ClienteRepository.java \
            src/main/java/com/fintech/Main.java

# Estágio 2: Imagem final leve (JRE 21)
FROM eclipse-temurin:21-jre-alpine
WORKDIR /app
COPY --from=builder /app/bin /app/bin
CMD ["java", "-cp", "bin", "com.fintech.Main"]