def soma():

    while True:
        num1 = int(input('Me diga um número: '))
        num2 = int(input('me diga outro número pra ser somado: '))

        total = num1 + num2

        print(f'O total de {num1} + {num2} = {total}')

        resposta = ' '
        while resposta not in 'SN':
            resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resposta == 'N':
            break

    print(f'Ok, você decidiu parar e já tem as somas que pediu! Obrigado.')
