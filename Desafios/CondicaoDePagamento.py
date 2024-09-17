print('Por um acaso você comprou um microondas!')

valor = float(input('Qual o valor do Microondas? '))

print("""Como você deseja pagar? 
[1] À vista no Dinheiro/Cheque: 10% de desconto
[2] À vista no Cartão: 5% de desconto
[3] Até 2x no cartão, preço normal
[4] 3x ou mais no cartão: 20% de juros""")
opcao = int(input('Qual a opção que deseja? '))

if opcao == 1:
    op1 = valor + (valor * 0.1)
    print(f'Valor a pagar é de R$ {op1} reais')
elif opcao == 2:
    op2 = valor + (valor * 0.05)
    print(f'Valor a pagar é de R$ {op2} reais')
elif opcao == 3:
    print(f'Valor a pagar é de R$ {valor} reais')
elif opcao == 4:
    op4 = valor + (valor * 0.2)
    quant_meses = int(input('Em quantas vezes você quer? '))
    parcela = op4 / quant_meses
    print(f'Sua compra será parcelada em {quant_meses}x de {parcela}')
    print(f'Sua compra de R$ {valor} vai custar R$ {op4} reais')
else:
    print('Você não optou por nenhuma opção!')