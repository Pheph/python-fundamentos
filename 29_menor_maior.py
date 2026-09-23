
# Solução 1. numero = -1

# n = 3
# maior = ''

# for i in range(n):

#     numero = -1

#     try: numero = int(input('\n Indique um números inteiros: '))
#     except:''

#     if numero >= 0 and numero <= 100:
#         if i == 0: maior = numero
#         if numero > maior : maior = numero

# print ('\n O maior valor é: '+ str(maior))


# Solução 2. com while True

maior = '---'
i = 0 

while True: 

    numero = -1

    try: numero = int(input('\n Indique um números inteiros: '))
    except:''

    if numero >= 0 and numero <= 100:
        if i == 0: menor = numero
        if i == 0: maior = numero
        if numero < menor : menor = numero
        if numero > maior : maior = numero
        i += 1

    if i>= 3: break

print ('\n O menor valor é: '+ str(menor))
print ('\n O maior valor é: '+ str(maior))
