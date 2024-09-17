maior = 0
homens = 0
mulheres_menor_20 = 0

while True:
    idade = int(input('Qual sua idade? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o seu sexo [M/F]: ')).strip().upper()[0]

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

    if idade > 18:
        maior += + 1

    if sexo == 'M':
        homens += + 1

    if sexo == 'F':
        if idade < 20:
            mulheres_menor_20 += + 1

    if resposta == 'N':
        break

print(f'Tem {maior} maior que 18 anos.')
print(f'Foram cadastrados {homens} do sexo Masculino.')
print(f'Tem {mulheres_menor_20} do sexo feminino menor que 20 anos.')





