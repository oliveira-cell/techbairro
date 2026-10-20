# ============================================================
# BANCO (Aula 21)
# ============================================================
#
# Responsabilidade: toda a comunicação com o banco SQLite.
# Este arquivo não sabe nada de janela.

import sqlite3
import os
from cliente import Cliente


class GerenciadorClientes:

    def __init__(self, caminho_banco="techbairro.db"):

        self.caminho_banco = caminho_banco
        self.criar_tabela()

    # Abre uma conexão com o banco
    def conectar(self):

        return sqlite3.connect(self.caminho_banco)

    # Cria a tabela de clientes
    def criar_tabela(self):

        conexao = self.conectar()

        conexao.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT,
                email TEXT,
                endereco TEXT
            )
        """)

        conexao.commit()
        conexao.close()

    # Cadastra um novo cliente
    def adicionar(self, cliente):

        conexao = self.conectar()

        cursor = conexao.execute(
            "INSERT INTO clientes (nome, telefone, email, endereco) VALUES (?, ?, ?, ?)",
            (cliente.nome, cliente.telefone, cliente.email, cliente.endereco),
        )

        conexao.commit()
        cliente.id = cursor.lastrowid
        conexao.close()

    # Consulta os clientes cadastrados
    def listar(self):

        conexao = self.conectar()

        linhas = conexao.execute(
            "SELECT id, nome, telefone, email, endereco FROM clientes ORDER BY nome"
        ).fetchall()

        conexao.close()

        return [
            Cliente(nome, telefone, email, endereco, id)
            for (id, nome, telefone, email, endereco) in linhas
        ]

    # Atualiza um cliente existente
    def atualizar(self, id_cliente, novo_cliente):

        conexao = self.conectar()

        cursor = conexao.execute(
            "UPDATE clientes SET nome = ?, telefone = ?, email = ?, endereco = ? WHERE id = ?",
            (
                novo_cliente.nome,
                novo_cliente.telefone,
                novo_cliente.email,
                novo_cliente.endereco,
                id_cliente,
            ),
        )

        conexao.commit()
        conexao.close()

        return cursor.rowcount == 1

    # Exclui um cliente
    def remover(self, id_cliente):

        conexao = self.conectar()

        cursor = conexao.execute("DELETE FROM clientes WHERE id = ?", (id_cliente,))

        conexao.commit()
        conexao.close()

        return cursor.rowcount == 1

    # Retorna a quantidade de clientes
    def total(self):

        conexao = self.conectar()

        quantidade = conexao.execute("SELECT COUNT(*) FROM clientes").fetchone()[0]

        conexao.close()

        return quantidade


# ============================================================
# OBJETO GERENCIADOR
# ============================================================

# Define o caminho do banco na pasta do projeto
PASTA_DO_PROJETO = os.path.dirname(os.path.abspath(__file__))
CAMINHO_BANCO = os.path.join(PASTA_DO_PROJETO, "techbairro.db")

print(f"Banco em uso: {CAMINHO_BANCO}")

gerenciador = GerenciadorClientes(CAMINHO_BANCO)
