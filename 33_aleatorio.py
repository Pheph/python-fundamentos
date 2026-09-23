
import random 

a = random.randint(0,10)
print(a)

## Numa lista temperatura armazene 10 temperaturas compreendidas entre -10 e 20 graus. Imprima todos os valores

temperaturas = []

for i in range(10):
    a = random.randint(-10,20)
    temperaturas.append(a)


temperaturas.sort()

print( *temperaturas )