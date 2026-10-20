# ============================================================
# IMPORTAR PLANILHA ANTIGA (Aula 16)
# ============================================================
#
# Simula a importação dos clientes que a TechBairro guardava
# numa planilha antiga, antes de ter o sistema.
#
# ATENÇÃO: este script grava DIRETO no banco, com INSERT,
# sem passar pela tela e sem passar pelas validações do salvar().
#
# Rode este arquivo UMA vez, com a TechBairro fechada.
# Importa o módulo do SQLite
import sqlite3

# Importa o módulo os, para montar o caminho do banco
import os

# ============================================================
# CAMINHO DO BANCO
# ==========================================================

# Mesmo banco usado pela TechBairro:
# o arquivo techbairro.db, na mesma pasta deste script
PASTA_DOS_SCRIPTS = os.path.dirname(os.path.abspath(__file__))
PASTA_DO_PROJETO = os.path.dirname(PASTA_DOS_SCRIPTS)
CAMINHO_DO_BANCO = os.path.join(PASTA_DO_PROJETO, "techbairro.db")
# ============================================================
# DADOS DA PLANILHA ANTIGA
# ============================================================
# Cada tupla é uma linha da planilha:
# (nome, telefone, email, endereco)
clientes_da_planilha = [
    ("Carlos Pereira", "61988887777", "carlos@email.com", "Quadra 3 Casa 10"),
    ("Beatriz Lima", "61977776666", "bia@email.com", "Rua 5 Casa 2"),
    ("Diego Martins", "61966665555", "diego@email", "Rua 8 Casa 1"),
    ("Eduarda Rocha", "61955554444", "eduarda@email.com", ""),
    ("Fábio Nunes", "6194444ABCD", "fabio@email.com", "Rua 9 Casa 4"),
    ("Gabriela Souza", "61988887777", "gabi@email.com", "Rua 2 Casa 7"),
    ("Helena Dias", "61933332222", "helena@email.com", "Rua 7 Casa 3"),
]

# ============================================================
# IMPORTAÇÃO
# ============================================================
conexao = sqlite3.connect(CAMINHO_DO_BANCO)
# Garante que a tabela existe (mesma estrutura da Aula 14)
conexao.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT,
        email TEXT,
        endereco TEXT
)
""")
# executemany roda o mesmo INSERT uma vez para cada tupla da lista
conexao.executemany(
    "INSERT INTO clientes (nome, telefone, email, endereco) VALUES (?, ?, ?, ?)",
    clientes_da_planilha,
)
conexao.commit()
conexao.close()
print(f"{len(clientes_da_planilha)} clientes importados para {CAMINHO_DO_BANCO}")
