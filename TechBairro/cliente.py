# ============================================================
# CLIENTE (Aula 21)
# ============================================================
#
# Responsabilidade: representar os dados de um cliente.
# Este arquivo não sabe nada de janela nem de banco.


# A classe Cliente representa um cliente dentro do sistema
class Cliente:

    # Método construtor
    def __init__(self, nome, telefone, email, endereco, id=None):

        # Armazena os dados do cliente
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    # Retorna os dados do cliente em uma única String
    def resumo(self):
        return f"{self.nome} | {self.telefone} | {self.email} | {self.endereco}"

    # Retorna as iniciais do nome
    def iniciais(self):

        # Divide o nome em partes
        partes = self.nome.split()

        # Pega a primeira letra de cada parte
        return "".join(parte[0].upper() for parte in partes if parte)
