import adivinhacao
import soma2numeros

print("""Escolha um jogo
[1] Adivinhação
[2] Soma 2 números""")

escolha = int(input('Qual jogo quer brincar agora? '))

if escolha == 1:
    print('Jogando adivinhação')
    adivinhacao.jogar()
elif escolha == 2:
    print('Jogo de Somar 2 números')
    soma2numeros.soma()
