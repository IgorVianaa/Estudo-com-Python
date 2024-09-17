total_gasto = 0
maior_que_1000 = 0
mais_barato = 0
contador = 0
produto = ' '
while True:
    nome_produto = str(input('Qual o produto que deseja? '))
    valor_produto = float(input('Este produto é: R$ '))
    contador += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [Sim/Não] ')).strip().upper()[0]

    total_gasto += valor_produto

    if valor_produto > 1000:
        maior_que_1000 += +1

    if contador == 1:
        mais_barato = valor_produto
        produto = nome_produto
    else:
        if valor_produto < mais_barato:
            mais_barato = valor_produto
            produto = nome_produto

    if resposta == 'N':
        break

print(f'O total das compras foi de R$ {total_gasto} reais')
print(f'{maior_que_1000}, é a quantidade de produtos que custam maior que R$ 1.000,00 reais')
print(f'O {produto} é mais em conta das compras, e custou R$ {mais_barato} reais')