from random import randint

# Escreva um programa que leia a velocidade do carro
# Se ele ultrapassar 80km/h. Aplique uma multa
# A multa vai custar R$ 7,00 por cada km/h acima do limite

print('Sargento: Qual foi a velocidade daquele carro?')
velocidade = randint(40, 180)
print(f'- Eu: Ele passou na velocidade de {velocidade}km/h')

if velocidade >80:
    print('Sargento: Pode aplicar a multa')
    multa = (velocidade - 80) * 7.43
    print(f'- Eu: Pelos cálculos, a multa vai ficar no valor de R$ {multa}')

else:
    print('Sargento: Ok, está na velocidade permitida')