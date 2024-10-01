from random import randint

def jogar():

    tentativas = 1

    while True:
        print('Computador vai colocar um número na mesa')
        numero_pc = randint(1, 5)
        print(f'Computador colocou: {numero_pc}')

        numero_humano = int(input('Agora sua vez, me diga um número: '))
        print(f'você colocou: {numero_humano}')

        if numero_pc == numero_humano:
            print('Você acertou')
            break
        else:
            if numero_pc > numero_humano:
                print('Errou, número do Computador foi maior')
                tentativas = tentativas + 1
            if numero_pc < numero_humano:
                print('Errou, número do Computador foi menor')
                tentativas = tentativas + 1

        resposta = ' '
        while resposta not in 'SN':
            resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resposta == 'N':
            break

    print(f'Ok, você finalizou sua partida com {tentativas} tentativas!')
