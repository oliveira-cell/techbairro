# Registro de testes da TechBairro
Versão testada: 3.3.2 · Data: 26/10/26 · Responsável: Ayla Nanci Neri De Oliveira
Sistema operacional e versão do Python:3.12.0
| ID | Requisito | Passos e dados | Esperado | Obtido | Status |
| ID | Requisito | Passos e dados | Esperado | Obtido | Status |
|---|---|---|---|---|---|
| CT01 | RF01 | Preencher Nome="Ana Silva", Endereço="Rua das Flores, 123", Telefone="61999999999", E-mail="ana@email.com" e submeter. | Cliente cadastrado com sucesso e persistido no banco de dados. | Cliente cadastrado com sucesso e persistido no banco de dados. | Passou |
| CT02 | RF01 | Deixar Nome="" e Endereço="" vazios, preencher o restante e submeter. | Exibir mensagem de erro de campos obrigatórios não preenchidos. | Exibida a mensagem: "Erro: Nome e Endereço são obrigatórios." | Passou |
| CT03 | RF02 | Inserir telefone com espaços: "61 9999 0000" e submeter. | O sistema deve tratar a formatação (remover espaços) e salvar corretamente. | Espaços removidos automaticamente e número salvo como "6199990000". | Passou |
| CT04 | RF03 | Inserir e-mail sem ponto no domínio: "ana@email" e submeter. | Exibir mensagem de erro informando formato de e-mail inválido. | Exibida a mensagem: "Erro: E-mail inválido. Verifique o formato." | Passou |
| CT05 | RF05 | Selecionar um cliente existente, alterar o telefone para "61888888888" e salvar. | Dados atualizados com sucesso e refletidos na listagem. | Dados atualizados com sucesso. | Passou |
| CT06 | RF06 | Acionar exclusão: responder "Não" na confirmação; em seguida, repetir e responder "Sim". | Na 1ª tentativa, cancelar exclusão e manter o registro. Na 2ª, excluir o registro. | Comportamento correto: cancelou na primeira vez e excluiu na segunda. | Passou |
