# ============================================================
# GERAR PACOTE DA VERSÃO (Aula 18)
# ============================================================
#
# Monta o arquivo .zip da versão que será publicada,
# deixando de fora o que NÃO deve ser distribuído.

# Importa o módulo os, para montar caminhos e percorrer pastas
import os

# Importa o módulo zipfile, para criar o arquivo .zip
# (os dois já vêm com o Python)
import zipfile

# ============================================================
# CONFIGURAÇÃO DO PACOTE
# ============================================================

# Este script fica na pasta scripts/;
# o projeto é a pasta de cima (igual aos outros scripts)
PASTA_DOS_SCRIPTS = os.path.dirname(os.path.abspath(__file__))
PASTA_DO_PROJETO = os.path.dirname(PASTA_DOS_SCRIPTS)

# Versão que será publicada
# (tem que ser a MESMA da constante VERSAO do techbairro.py)
VERSAO = "3.3.2"  # COMPLETE: a mesma versão do techbairro.py

# Pastas que NÃO entram no pacote
PASTAS_FORA = ["dist", "__pycache__"]  # COMPLETE: duas pastas

# Tipos de arquivo que NÃO entram no pacote
EXTENSOES_FORA = [".db", ".pyc"]  # COMPLETE: dois tipos de arquivo

# O pacote é salvo na pasta dist/ do projeto
PASTA_DIST = os.path.join(PASTA_DO_PROJETO, "dist")
os.makedirs(PASTA_DIST, exist_ok=True)

# O nome do pacote leva a versão
NOME_PACOTE = f"TechBairro-{VERSAO}"
CAMINHO_PACOTE = os.path.join(PASTA_DIST, NOME_PACOTE + ".zip")


# ============================================================
# MONTAGEM DO PACOTE
# ============================================================

print(f"Gerando {NOME_PACOTE}.zip")
print()

incluidos = 0
deixados_de_fora = 0

# Abre o .zip para escrita (ZIP_DEFLATED = compactado)
with zipfile.ZipFile(CAMINHO_PACOTE, "w", zipfile.ZIP_DEFLATED) as pacote:

    # os.walk percorre a pasta do projeto e todas as subpastas
    for pasta_atual, subpastas, arquivos in os.walk(PASTA_DO_PROJETO):

        for nome in arquivos:

            # Caminho completo e caminho a partir da pasta do projeto
            caminho = os.path.join(pasta_atual, nome)
            relativo = os.path.relpath(caminho, PASTA_DO_PROJETO)

            # Confere se o arquivo está dentro de uma pasta que fica de fora
            dentro_de_pasta_fora = False

            for parte in relativo.split(os.sep):
                if parte in PASTAS_FORA:
                    dentro_de_pasta_fora = True

            # Pega a extensão do arquivo (.py, .db, .md...)
            extensao = os.path.splitext(nome)[1]

            if dentro_de_pasta_fora or extensao in EXTENSOES_FORA:

                print(f"  fora      {relativo}")
                deixados_de_fora += 1

            else:

                # Dentro do .zip, tudo fica numa pasta com o nome do pacote
                pacote.write(caminho, os.path.join(NOME_PACOTE, relativo))

                print(f"  incluído  {relativo}")
                incluidos += 1


print()
print(f"Arquivos incluídos: {incluidos}")
print(f"Arquivos deixados de fora: {deixados_de_fora}")
print(f"Pacote salvo em: {CAMINHO_PACOTE}")
