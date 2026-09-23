
arq = '35_valores.txt'

with open(arq, 'r', encoding='utf-8') as f:
    for linha in f:
        try:
            valor = int(linha.strip()) * 3 
            print(valor)
        except: ''

        