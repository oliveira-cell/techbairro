import sqlite3
import os

PASTA_DOS_SCRIPTS = os.path.dirname(os.path.abspath(__file__))
PASTA_DO_PROJETO = os.path.dirname(PASTA_DOS_SCRIPTS)
CAMINHO_DO_BANCO = os.path.join(PASTA_DO_PROJETO, "techbairro.db")

# isolation_level=None: nós mesmos controlamos a transação
conexao = sqlite3.connect(CAMINHO_DO_BANCO, isolation_level=None)

# BEGIN EXCLUSIVE: pega a trava exclusiva do banco
conexao.execute("BEGIN EXCLUSIVE")


input("Banco TRAVADO. Teste a TechBairro agora e aperte Enter aqui para liberar...")

# Desfaz a transação (não alteramos nada) e libera a trava
conexao.execute("ROLLBACK")
conexao.close()
print("Banco liberado.")
