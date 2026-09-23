import subprocess
subprocess.run('cls',shell=True)

temp = []

## 1. Leitura e armazenamento das 6 temperaturas
for i in range(6):
    try:
        valor = int(input('Indique a '+ str(i+1) +' temperatura: '))
        temp.append(valor)
    except: ''

## 2. Determinação das mínima e da máxima
minima = min(temp)
maxima = max(temp)

## 3. Ordenar as temperaturas
temp.sort()

## 4. Impressão das temperaturas
print()

for i in range(len(temp)):

    texto = ''

    if temp[i] == minima: texto ='- Mínima'
    if temp[i] == maxima: texto ='- Máxima'

    print(' ', temp[i], 'graus', texto)

print(temp)
print('\n Mínima: ', minima)
print('\n Máxima: ', maxima)