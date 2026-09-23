
# Lêr o conteúdo de um arquivo TXT, extrair os nomes, separar os nomes dos email. Guardar o resultado em 2 linhas (arrays): formandos e emails

import subprocess
subprocess.run('cls', shell=True)

aqt = 'formandos.txt'

## 1. Leitura dos nomes existentes no arquivo:
nome_arquivo = []

with open(aqt,'r', encoding='utf-8') as f:
    for linha in f:
        texto = linha.strip()
        if len(texto) > 25: nome_arquivo.append(texto.lower())

# print(nome_arquivo, '\n')
## 2. Separação entre o nome e o e-mail

formandos = []
endereco_email = []

for k in range(len(nome_arquivo)):

    nome = nome_arquivo[k]
    nome_completo = ''

    for i in range(len(nome)):
        if nome[i] == '-': break
        nome_completo += nome[i]

    formandos.append(nome_completo.strip())
    posicao = i + 1

    email = ''

    for i in range(posicao, len(nome)): email += nome[i]

    endereco_email.append(email.strip())

print(formandos)
print(endereco_email)