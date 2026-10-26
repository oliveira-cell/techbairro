# Manual de uso da TechBairro

## A tela principal
A tela principal exibe os campos para digitar as informações do cliente (Nome, Telefone, E-mail e Endereço), os botões de ação (Cadastrar, Consultar, Alterar, Excluir), a lista visual de registros cadastrados e uma barra de mensagens na parte inferior que avisa o status de cada operação.

## Cadastrar um cliente
1. Preencha os campos Nome, Telefone, E-mail e Endereço com os dados do morador.
2. Clique no botão **Cadastrar**.
3. Confira se a mensagem de sucesso apareceu na barra inferior.

## Consultar os clientes cadastrados
1. Digite o nome ou parte do nome no campo de busca ou clique na lista de clientes.
2. Visualize os dados detalhados na tela.

## Alterar os dados de um cliente
1. Selecione o cliente desejado na lista.
2. Modifique as informações diretamente nos campos de texto.
3. Clique no botão **Alterar**.

## Excluir um cliente
1. Selecione o cliente que deseja remover na lista da tela.
2. Clique no botão **Excluir**.
3. Confirme a exclusão na mensagem de aviso.

## Regras de preenchimento
| Campo | Obrigatório? | Regra |
|---|---|---|
| Nome | Sim | Deve conter o nome completo do morador. |
| Telefone | Sim | Digitar apenas números com DDD. |
| E-mail | Não | Deve conter um formato de e-mail válido (ex: nome@email.com). |
| Endereço | Sim | Informar rua, número e bairro. |

## Mensagens do sistema
| Mensagem | O que significa | O que fazer |
|---|---|---|
| Cliente cadastrado com sucesso! | O registro foi salvo no banco. | Nenhum, o processo terminou. |
| Preencha todos os campos obrigatórios. | Faltou preencher Nome, Telefone ou Endereço. | Preencha os campos em branco e tente novamente. |
| Telefone inválido. | O campo de telefone contém letras ou formato errado. | Digite apenas os números do telefone com DDD. |
| Erro ao conectar ao banco de dados. | Houve falha na leitura do arquivo local. | Verifique se o arquivo `techbairro.db` está na pasta correta. |
| Cliente não encontrado na busca. | O nome pesquisado não está cadastrado. | Verifique a grafia ou cadastre um novo cliente. |
| Operação cancelada. | Ação interrompida pelo usuário. | Retome o procedimento desejado. |

## Dúvidas frequentes
**O que fazer se o programa fechar sozinho?**
Abra novamente executando o arquivo do sistema. Se o problema persistir, avise o voluntário técnico da associação.

**Os dados dos moradores ficam seguros?**
Sim, os dados ficam salvos apenas no computador da associação em um arquivo local seguro e protegido.

**Como faço para guardar uma cópia dos dados?**
Basta copiar o arquivo de banco de dados da associação para um pendrive com a ajuda do suporte técnico.
