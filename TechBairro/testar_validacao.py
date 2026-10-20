from cliente import Cliente
from validacao import ValidadorCliente

validador = ValidadorCliente()

# Teste 1: cliente válido
cliente = Cliente("João", "11999999999", "joao@gmail.com", "Rua das Flores")

erro = validador.validar(cliente)

if not erro:
    print("CT01 - Cliente válido: PASSOU")
else:
    print("CT01 - Cliente válido: FALHOU")
    print(erro)

# Teste 2: nome vazio
cliente = Cliente("", "11999999999", "joao@gmail.com", "Rua das Flores")

erro = validador.validar(cliente)

if erro:
    print("CT02 - Nome vazio: PASSOU")
else:
    print("CT02 - Nome vazio: FALHOU")

# Teste 3: telefone com letras
cliente = Cliente("João", "11999ABC", "joao@gmail.com", "Rua das Flores")

erro = validador.validar(cliente)

if erro:
    print("CT03 - Telefone inválido: PASSOU")
else:
    print("CT03 - Telefone inválido: FALHOU")

# Teste 4: e-mail inválido
cliente = Cliente("João", "11999999999", "joao", "Rua das Flores")

erro = validador.validar(cliente)

if erro:
    print("CT04 - E-mail inválido: PASSOU")
else:
    print("CT04 - E-mail inválido: FALHOU")
