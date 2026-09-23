



arq = '35_valores_txt.py'

## 1. solução todo o arquivo

with open(arq, 'r', encoding='utf-8') as f:
    conteudo = f.read()
    print(conteudo)
 

## 2. solução linha por linha 


with open(arq, 'r', encoding='utf-8') as f:
    linha = f.readlines()
    print(linha)


## 3. solução linha a linha com ciclo (loop)

arq = '35_valores_txt.py'

with open(arq, 'r', encoding='utf-8') as f:
    for linha in f:
        print(linha.strip())
