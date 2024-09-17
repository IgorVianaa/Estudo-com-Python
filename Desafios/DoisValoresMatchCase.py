num1 = int(input('Diga um número: '))
num2 = int(input('Diga outro número: '))
menu = 0

while menu != 5:
    print('''
[1] Somar
[2] Multiplicar
[3] Maior ou Menor
[4] Novos Números
[5] Sair o programa
''')

    menu = int(input('O que deseja fazer com os números citados? '))
    match menu:
        case 1:
            soma = num1 + num2
            print(f'A soma de {num1} + {num2} = {soma}')
        case 2:
            multiplicacao = num1 * num2
            print(f'A multiplicação de {num1} x {num2} = {multiplicacao}')
        case 3:
            if num1 > num2:
                print(f'O {num1} é maior que {num2}!')
            elif num2 > num1:
                print(f'O {num2} é maior que {num1}!')
            else:
                print('Não existe valor maior, os dois são iguais!')
        case 4:
            print('Diga novos números')
            num1 = int(input('Diga novo número: '))
            num2 = int(input('Diga um outro número: '))
        case 5:
            print('Ok, terminamos por aqui!')
            exit()
        case _:
            print('Opção inválida, digite novamente a sua opção!')
