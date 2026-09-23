
#import os
#os.system('cls')

import subprocess
# from unittest import case

d200 = d100 = d50 = d20 = d10 = d5 = 10

msg = ''

while True:

    subprocess.run("cls", shell=True)

    preco = troco = 0 

    # 1. Menu de bebidas

    while True:
        print('\n MENU')
        print('\t 1. Café')
        print('\t 2. Chá')
        print('\t 3. Chocolate')

        print('\n\t', msg) 

        try: opcao = int(input('\n Escolha a sua bebida: '))
        except: opcao = -1 

        if (opcao > 0 and opcao <= 3) or opcao == 123: break


        print()

        # provísorio...  sair do programa

    # Administração da máquina de bebidas
#####################################################################

    if opcao == 123: 
        subprocess.run("cls", shell=True)

        

        while True:
            print('\n MENU ADMINISTRATIVO')


            print('\n\t 1. Ver o dinheiro em caixa')
            print('\t 2. Ver o dinheiro do moedeiro')

            print('\t 10. Desligar a maquina')
            print('\t 0. Voltar')

            try: opcao = int(input('\n Escolha uma opção: '))
            except: opcao = -1

            if (opcao >= 0 and opcao <= 10) : break    

        if opcao == 2:
            print('\n\t Moedas existentes no moedeiro:')
            print('\t 5 cêntimos: ', d5)
            print('\t 10 cêntimos: ', d10)
            print('\t 20 cêntimos: ', d20)
            print('\t 50 cêntimos: ', d50)
            print('\t 1 euro: ', d100)
            print('\t 2 euro: ', d200)

            input('\n \n Pressione ENTER para continuar ...')

        if opcao == 10: break

        opcao = 0

    ############################################################

    # 2. Escolher o preço do produto 

    match opcao:
        case 1: preco = 35
        case 2: preco = 45
        case 3: preco = 50

    print(' Preço do produto: ', preco,'cêntimos \n')

    # 3. Receber moedas válidas 

    dinheiro = 0

    while True and preco > 0:

        try: moeda = int(input('Introduza uma moeda válida: '))
        except: moeda = 0 

        if moeda == 5 or moeda == 10 or moeda == 20 or moeda == 50 or moeda == 100 or moeda ==200: 
            dinheiro += moeda 
            troco = preco - dinheiro

            if troco <= 0: break
            print('Em falta: ', troco, 'cêntimos \n')


    # 4. Devolução do troco em moedas

    troco *= -1
    
    print('Troco: ', troco, 'cêntimos \n')

    moeda_atual = 200
    m5 = m10 = m20 = m50 = m100 = m200 = 0

    if troco > 0:

        while True:

            print(troco, moeda_atual)

            temp = troco - moeda_atual


            # trocar moedas
            if temp < 0: 

                if moeda_atual == 200: moeda_atual = 100
                else:
                    if moeda_atual == 100: moeda_atual = 50
                    else:
                        if moeda_atual == 50: moeda_atual = 20
                        else:
                            if moeda_atual == 20: moeda_atual = 10
                            else: moeda_atual = 5

            else: 
                troco = troco - moeda_atual

                match moeda_atual:
                    case 200: 
                        if d200 > 0: 
                            d200 -= 1
                            m200 += 1
                    case 100: 
                        
                        if d100 > 0: 
                            d100 -= 1
                            m100 += 1
                    case 50: 
                        if d50 > 0: 
                            d50 -= 1
                            m50 += 1
                    case 20: 
                        if d20 > 0: 
                            d20 -= 1
                            m20 += 1

                    case 10: 
                        if d10 > 0: 
                            d10 -= 1
                            m10 += 1

                    case 5: 
                        if d5 > 0: 
                            d5 -= 1
                            m5 += 1

                if d200 == 0 or d100 == 0 or d50 == 0 or d20 == 0 or d10 == 0 or d5 == 0:
                    msg = '\n Faltam moedas para o troco! \n'
                        

            if troco == 0: break

        print(msg) 

    print('Moedas:')

    if m5>  0: print('\t  5 cêntimos:', m5)                   
    if m10> 0: print('\t  10 cêntimos:', m10)
    if m20> 0: print('\t  20 cêntimos:', m20)
    if m50> 0: print('\t  50 cêntimos:', m50)
    if m100>0: print('\t  1 euro:'     , m100)
    if m200>0: print('\t  2 euro:'     , m200)  

    input('\n \n Pressione ENTER para continuar ...')  




            

