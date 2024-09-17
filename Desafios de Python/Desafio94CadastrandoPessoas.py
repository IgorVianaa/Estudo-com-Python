dados_dic = {}
dados_lista = []
mulheres = 0
soma_idade = 0

while True:
    dados_dic['nome'] = str(input('Nome: '))
    dados_dic['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    dados_dic['idade'] = int(input('Idade: '))

    dados_lista.append(dados_dic.copy())

    soma_idade = soma_idade + dados_dic['idade']
    media = soma_idade/len(dados_lista)

    if dados_dic['sexo'] in 'Ff':
        mulheres += +1
    
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if resposta == "N":
        break

print(dados_dic)
print(dados_lista)

print('=' *30)

print(f'Foram cadastradas {len(dados_lista)} pessoas!') #Quantidade de pessoas Cadastradas
print(f'A média de idade dos cadastrados é de {media:.2f} anos!')
print(f'Contém {mulheres} mulheres!')
