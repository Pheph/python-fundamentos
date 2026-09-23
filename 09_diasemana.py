
# Entrada de valores 
#valordia = 1

valordia = int(input('\n Indique um número compreendido entre 1 a 7: '))

# Processamento
if valordia == 1:
    diasemana = 'Segunda-feira'
else:
    if valordia == 2:
        diasemana = 'Terça-feira'
    else:
        if valordia == 3:
            diasemana = 'Quarta-feira'
        else:
            if valordia == 4:
                diasemana = 'Quinta-feira'
            else:
                 if valordia == 5:
                     diasemana = 'Sexta-feira'
                 else:
                    if valordia == 6:
                        diasemana = 'Sábado'
                    else:
                        diasemana = 'Domingo'
    



# Saída 
print('\n Hoje é', diasemana.lower(),',que corresponde a dia com o número ', valordia)

