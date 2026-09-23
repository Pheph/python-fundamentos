

media = 0
n = 3

print()

## 2. Leitura das notas

soma = 0

for i in range(n):
   nota = 0
   try: nota = float(input('Indique a '+ str(i+1) +' nota: '))
   except: ''

   soma += nota

media = soma/n

## 1. Processamento (solução para o problema)

if media <= 7.5: msg = 'Reprovado'
else:
    if media < 9.5: msg = 'Exame de recuperação'
    else: msg = 'Aprovado'
    
print('O formando foi', msg)
