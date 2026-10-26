# Importa a biblioteca Tkinter
import tkinter as tk

# Importa o messagebox para exibir mensagens e confirmações
from tkinter import messagebox

# Importa o módulo do SQLite
import sqlite3

# Usado para montar o caminho completo do banco
import os

from cliente import Cliente
from banco import GerenciadorClientes
from validacao import ValidadorCliente

# ============================================================
# VERSÃO
# ============================================================

VERSAO = "3.3.2"


# ============================================================
# CAMINHO DO BANCO
# ============================================================

PASTA_DO_PROJETO = os.path.dirname(os.path.abspath(__file__))
CAMINHO_BANCO = os.path.join(PASTA_DO_PROJETO, "techbairro.db")

print(f"Banco em uso: {CAMINHO_BANCO}")


# ============================================================
# OBJETO GERENCIADOR
# ============================================================

gerenciador = GerenciadorClientes(CAMINHO_BANCO)
validador = ValidadorCliente()

# Guarda o id do cliente que está sendo editado
id_em_edicao = None


# ============================================================
# JANELA PRINCIPAL
# ============================================================

janela = tk.Tk()

janela.title("TechBairro — Cadastro de Cliente")
janela.geometry("480x460")
janela.resizable(False, False)


# ============================================================
# CABEÇALHO DA INTERFACE
# ============================================================

cabecalho = tk.Frame(janela, bg="#2c3e50")
cabecalho.pack(side="top", fill="x")

tk.Label(
    cabecalho,
    text="Cadastro de Cliente",
    fg="white",
    bg="#2c3e50",
    font=("Arial", 14, "bold"),
    pady=12,
).pack()


# ============================================================
# FORMULÁRIO
# ============================================================

form = tk.Frame(janela)
form.pack(pady=20)

campos = ["Nome", "Telefone", "E-mail", "Endereço"]
entradas = {}

for i, campo in enumerate(campos):

    tk.Label(form, text=f"{campo}:").grid(row=i, column=0, sticky="e", padx=5, pady=6)

    entrada = tk.Entry(form, width=30)
    entrada.grid(row=i, column=1, padx=5, pady=6)

    entradas[campo] = entrada


# ============================================================
# STATUS
# ============================================================

status = tk.Label(
    janela,
    text="Nenhum cliente cadastrado ainda",
    fg="gray",
    wraplength=440,
    justify="left",
)

status.pack(pady=(0, 5))


# ============================================================
# CONTADOR DE CLIENTES
# ============================================================

contador = tk.Label(janela, text=f"Clientes cadastrados: {gerenciador.total()}")

contador.pack()


# ============================================================
# ATUALIZAR CONTADOR
# ============================================================


def atualizar_contador():

    contador.config(text=f"Clientes cadastrados: {gerenciador.total()}")


# ============================================================
# LIMPAR CAMPOS
# ============================================================


def limpar_campos():

    global id_em_edicao

    # Percorre todos os campos
    for entrada in entradas.values():

        # Apaga o conteúdo do campo
        entrada.delete(0, tk.END)

    # Sai do modo de edição
    id_em_edicao = None

    # O botão volta a ser Salvar
    botao_salvar.config(text="Salvar")


# ============================================================
# SALVAR
# ============================================================


def salvar():

    global id_em_edicao

    # Pega os valores digitados nos campos
    valores = {campo: entradas[campo].get().strip() for campo in campos}

    # Cria um objeto Cliente
    cliente = Cliente(
        valores["Nome"], valores["Telefone"], valores["E-mail"], valores["Endereço"]
    )

    # Valida os dados do cliente
    erro = validador.validar(cliente)

    if erro:

        status.config(text=erro, fg="red")
        return

    # Salva ou atualiza o cliente no banco
    try:

        if id_em_edicao is not None:

            # Atualiza o cliente que está sendo editado
            gerenciador.atualizar(id_em_edicao, cliente)

            status.config(text="Cliente atualizado com sucesso!", fg="green")

        else:

            # Adiciona um novo cliente
            gerenciador.adicionar(cliente)

            status.config(text="Cliente cadastrado com sucesso!", fg="green")

    except sqlite3.Error as erro:

        messagebox.showerror(
            "Erro no banco", f"Não foi possível salvar o cliente.\n{erro}"
        )

        return

    # Limpa os campos e sai do modo de edição
    limpar_campos()

    # Atualiza o contador
    atualizar_contador()


# ============================================================
# CANCELAR
# ============================================================


def cancelar():

    # Verifica se estava editando um cliente
    estava_editando = id_em_edicao is not None

    # Limpa os campos
    limpar_campos()

    # Atualiza a mensagem de status
    if estava_editando:

        status.config(text="Edição cancelada. Nada foi alterado.", fg="gray")

    else:

        status.config(text="Formulário limpo", fg="gray")


# ============================================================
# CONSULTA DE CLIENTES
# ============================================================


def abrir_consulta():

    # Cria uma nova janela
    consulta = tk.Toplevel(janela)

    consulta.title("Consulta de Clientes")
    consulta.geometry("500x380")
    consulta.resizable(False, False)

    # ========================================================
    # LISTBOX
    # ========================================================

    lista = tk.Listbox(consulta, width=65, height=12)
    lista.pack(padx=10, pady=10)

    # ========================================================
    # BARRA DE ROLAGEM
    # ========================================================

    scrollbar = tk.Scrollbar(consulta)
    scrollbar.pack(side="right", fill="y", pady=10)

    lista.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=lista.yview)

    # Guarda os clientes na mesma ordem das linhas
    clientes_na_tela = []

    # ========================================================
    # ATUALIZAR LISTA
    # ========================================================

    def atualizar_lista():

        # Remove os itens antigos
        lista.delete(0, tk.END)
        clientes_na_tela.clear()

        # Busca os clientes no banco
        try:

            clientes_cadastrados = gerenciador.listar()

        except sqlite3.Error as erro:

            messagebox.showerror(
                "Erro no banco", f"Não foi possível consultar os clientes.\n{erro}"
            )

            return

        # Verifica se existem clientes
        if not clientes_cadastrados:

            lista.insert(tk.END, "Nenhum cliente cadastrado")
            return

        # Exibe os clientes
        for cliente in clientes_cadastrados:

            lista.insert(tk.END, cliente.resumo())
            clientes_na_tela.append(cliente)

    # ========================================================
    # CLIENTE SELECIONADO
    # ========================================================

    def cliente_selecionado(acao):

        # Descobre qual linha foi selecionada
        selecionado = lista.curselection()

        # Verifica se existe uma seleção válida
        if not selecionado or selecionado[0] >= len(clientes_na_tela):

            messagebox.showwarning("Atenção", f"Selecione um cliente antes de {acao}.")

            return None

        # Retorna o cliente correspondente à linha
        return clientes_na_tela[selecionado[0]]

    # ========================================================
    # EDITAR CLIENTE
    # ========================================================

    def editar_cliente():

        global id_em_edicao

        # Pega o cliente selecionado na tela
        cliente = cliente_selecionado("editar")

        if cliente is None:
            return

        # Guarda o id fixo do cliente
        id_em_edicao = cliente.id

        # Preenche os campos do formulário
        entradas["Nome"].delete(0, tk.END)
        entradas["Nome"].insert(0, cliente.nome)

        entradas["Telefone"].delete(0, tk.END)
        entradas["Telefone"].insert(0, cliente.telefone)

        entradas["E-mail"].delete(0, tk.END)
        entradas["E-mail"].insert(0, cliente.email)

        entradas["Endereço"].delete(0, tk.END)
        entradas["Endereço"].insert(0, cliente.endereco)

        # Informa que o cliente está sendo editado
        status.config(text=f"Editando cliente: {cliente.nome}", fg="blue")

        # Altera o texto do botão
        botao_salvar.config(text="Salvar edição")

        # Fecha a consulta
        consulta.destroy()

    # ========================================================
    # EXCLUIR CLIENTE
    # ========================================================

    def excluir_cliente():

        # Pega o cliente selecionado na tela
        cliente = cliente_selecionado("excluir")

        if cliente is None:
            return

        # Confirma a exclusão
        confirmar = messagebox.askyesno(
            "Confirmar exclusão",
            f"Tem certeza que deseja excluir o cadastro de "
            f"{cliente.nome}?\n\n"
            f"Essa ação não pode ser desfeita.",
            parent=consulta,
        )

        # Só exclui se o usuário confirmar
        if confirmar:

            try:

                # Remove o cliente pelo id
                removeu = gerenciador.remover(cliente.id)

            except sqlite3.Error as erro:

                messagebox.showerror(
                    "Erro no banco",
                    f"Não foi possível excluir o cliente.\n{erro}",
                    parent=consulta,
                )

                return

            # Verifica se o cliente foi encontrado
            if not removeu:

                messagebox.showwarning(
                    "Cliente não encontrado",
                    f"{cliente.nome} já não está mais no banco.",
                    parent=consulta,
                )

                atualizar_lista()
                return

            # Atualiza a lista e o contador
            atualizar_lista()
            atualizar_contador()

            # Atualiza a mensagem de status
            status.config(
                text=f"Cliente '{cliente.nome}' excluído com sucesso!", fg="green"
            )

    # ========================================================
    # BOTÕES DA CONSULTA
    # ========================================================

    botoes_consulta = tk.Frame(consulta)
    botoes_consulta.pack(pady=10)

    # Botão Editar
    tk.Button(
        botoes_consulta, text="Editar selecionado", width=18, command=editar_cliente
    ).grid(row=0, column=0, padx=5)

    # Botão Excluir
    tk.Button(
        botoes_consulta, text="Excluir selecionado", width=18, command=excluir_cliente
    ).grid(row=0, column=1, padx=5)

    # Duplo clique numa linha abre a edição
    lista.bind("<Double-Button-1>", lambda evento: editar_cliente())

    # Preenche a lista ao abrir a consulta
    atualizar_lista()


# ============================================================
# BOTÕES DA JANELA PRINCIPAL
# ============================================================

botoes = tk.Frame(janela)
botoes.pack(pady=10)

# Botão Salvar
botao_salvar = tk.Button(botoes, text="Salvar", width=13, command=salvar)

botao_salvar.grid(row=0, column=0, padx=5)

# Botão Cancelar
tk.Button(botoes, text="Cancelar", width=12, command=cancelar).grid(
    row=0, column=1, padx=5
)

# Botão Consultar
tk.Button(botoes, text="Consultar", width=12, command=abrir_consulta).grid(
    row=0, column=2, padx=5
)


# ============================================================
# VERSÃO
# ============================================================

tk.Label(janela, text=f"v{VERSAO}", fg="gray").place(relx=0.97, rely=0.97, anchor="se")


# ============================================================
# INICIALIZAÇÃO
# ============================================================

janela.mainloop()
