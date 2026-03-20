# Study Time Control (Controle de Tempo de Estudo)

Este projeto é uma ferramenta de linha de comando (CLI) desenvolvida em **Python** integrada ao **MySQL**. O objetivo é permitir que estudantes gerenciem o tempo dedicado a cada disciplina, mantendo um histórico acumulado de horas e sessões de estudo de forma persistente e segura.

# Funcionalidades

O sistema é modularizado em funções específicas para cada tarefa:

1.  **Registro de Estudos ("novo_estudo"):**
    Calcula a duração total em minutos. Verifica se a disciplina já existe. Se sim, atualiza o tempo acumulado e incrementa o contador. Se não, cria um novo registro. Possui tratamento para evitar cálculos de tempo negativos.
2.  **Visualização de Histórico ("mostra_historico`):**
    Consulta o banco de dados e exibe os dados estruturados no console.
3.  **Exportação de Dados (`salvar_arquivo`):**
    Gera relatórios em `.txt`.
    *Lógica Anti-Sobrescrita:* Verifica a existência de arquivos anteriores e gera novos nomes numerados (ex: `historico_estudos_1.txt`) para evitar perda de dados.
    
5.  **Segurança e Boas Práticas:**
    * Estrutura preparada para configuração de credenciais sem exposição de senhas reais.
    * Arquivo ".gitignore" configurado para não subir arquivos temporários ou relatórios pessoais.

## Tecnologias Utilizadas

* **Python 3.9**
* **MySQL Connector/Python**: Driver oficial para integração com o banco.
* **OS Module**: Manipulação de arquivos e caminhos do sistema.

## Como Configurar e Rodar

### 1. Requisitos
Instale o driver do MySQL para Python:
pip install mysql-connector-python


### 2. Banco de Dados
Crie o schema no seu MySQL:

CREATE DATABASE reg_tempo_estudo;
USE reg_tempo_estudo;

CREATE TABLE estudo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    disciplina VARCHAR(100) NOT NULL,
    tempo INT DEFAULT 0,
    historico INT DEFAULT 0
);

### 3. Configuração de Acesso
No arquivo `main.py`, localize as variáveis de conexão e insira suas credenciais locais:

# Edite estas linhas com seus dados:
host="localhost", 
user="root", 
password="SUA_SENHA_AQUI", 
database="reg_tempo_estudo"

### 4. Execução
python main.py

## 📂 Estrutura de Arquivos do Repositório

* "main.py": Código fonte principal com as funções de lógica e interface.
* ".gitignore": Impede o versionamento de arquivos ".txt" gerados e pastas de cache ("__pycache__").
* "README.md": Documentação do projeto.
