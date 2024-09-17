import random
import time


print("""Faça o computador pensar em um número entre 0 e 5. E peça para
o usuário tentar descobrir qual foi o número escolhido pelo computador""")

print('--' * 20)
print('O computador vai pensar em um número')
num = random.randint(1,5)
print('--' * 20)


print('Agora vou tentar adivinhar qual o número o computador pensou')
jogador = int(input('O número é: '))
print('--' * 20)

print('PROCESSANDO...')
time.sleep(3)

print('--' * 20)

if num == jogador:
    print('Você acertou')
else:
    print('Você errou')

