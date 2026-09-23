

idade = 0

try: idade = float(input('\n Indique a idade do atleta: '))
except: ''

## Solução 1: com IF

if idade < 5: msg = 'Não possui idade suficiente'
else:
    if idade < 8: msg = 'Infaltil A'
    else:
        if idade < 12: msg= 'Infaltil B'
        else: 
            if idade < 15: msg = 'Juvenil A'
            else:
                if idade < 18: msg = 'Junenil B'
                else: msg = 'Adulto'

print('\n (if) Escalão: ', msg)

## Solução 2: com MATCH

msg = ''
match idade:
    case idade if idade < 5 : msg = 'Não tem idade'
    case idade if idade < 8 : msg = 'Infaltil A'
    case idade if idade < 12: msg = 'Infaltil B'
    case idade if idade < 15: msg = 'Juvenil A'
    case idade if idade < 18: msg = 'Junenil B'
    case _                  : msg = 'Adulto'

print('\n (match) Escalão: ', msg)

