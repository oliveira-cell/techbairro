## Em desenvolvimento### Adicionado- Código publicado no GitHub, com histórico de versões.
# Changelog da TechBairro

# Changelog

## v3.3.0 (Aula 20)

### Adicionado
- Botão "Salvar edição" durante a alteração de clientes.
- Cancelamento de edição com mensagem específica.
- Edição de clientes por duplo clique na lista de consulta.

### Corrigido
- Correção da seleção de clientes para editar e excluir com segurança.
- Verificação do retorno do banco de dados ao atualizar um cliente.
- Verificação do retorno do banco de dados ao excluir um cliente.
- Aviso quando o cliente já não existe no banco de dados.
- Proteção contra a seleção de linhas de aviso, como "Nenhum cliente cadastrado".

## v3.2.1 (Aula 18)

### Alterado
- O número da versão passou a ficar em um único lugar.

### Adicionado
- Script scripts/gerar_pacote.py, que gera o pacote da versão.
- Arquivo COMO_EXECUTAR.txt, com as instruções para executar a TechBairro.

## v3.2.0
...

## v3.2 (Aula 16)
### Alterado
- O banco agora é aberto pelo caminho completo (os.path + __file__), sempre na pasta do projeto, não importa de onde o programa seja executado.

### Adicionado
- Mensagem "Banco em uso" no terminal, mostrando qual arquivo de banco está sendo usado.

## v3.1 (Aula 15)
### Corrigido
- A função atualizar() agora executa o commit no banco de dados.
- A validação de e-mail passou a exigir um ponto (.) após o símbolo @.
- Correção na consulta de busca por ID para tratar valores não numéricos.
- Ajuste no layout da tela de cadastro para evitar sobreposição de botões.
- Correção do erro ao tentar excluir um cliente sem nenhum item selecionado.

## v3.0 (Aula 14)
### Alterado
- O GerenciadorClientes deixou de guardar os clientes numa lista em memória e passou a gravar no banco SQLite techbairro.db.
- As operações de editar e excluir clientes foram alteradas para identificar os registros diretamente pelo id do banco.
- A busca e listagem principal passaram a consultar os dados via SQL SELECT na tabela clientes.

### Adicionado
- Criação e inicialização automática da tabela `clientes` no banco SQLite caso não exista.

## v2.0 (Aulas 11 e 12)
### Adicionado
- Orientação a Objetos no projeto, introduzindo as classes `Cliente` e `GerenciadorClientes`.
- Nova tela gráfica de Consulta de Clientes com tabela/listagem visual de registros.

## Antes da v2.0 (Aulas 5 a 10)
- Desenvolvimento do protótipo inicial com interface gráfica (Tkinter), contendo formulário de cadastro, tratamento de eventos nos botões e validação básica de campos obrigatórios.

