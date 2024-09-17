produtos = {1: ['Monitor LED 24"', 599.99, 1],
            2: ['Teclado wireless', 49.26, 1],
            3: ['Mouse wireless', 19.9, 1],
            4: ['Cartucho colorido', 54, 2]}

total = 0

for cod, prod in produtos.items():
    subtotal = produtos[cod][1] * produtos[cod][2]
    print(f"{prod[0]}: R$ {subtotal:.2f}")
    total += subtotal

print(20 * "-")
print(F"Total: R$ {total:.2f}")

# OUTRA FORMA DE FAZER, COM DADOS FORNECIDOS!

produtos = {}

while True:
    cod = int(input("Código: "))
    nome = input("Nome: ")
    preco = float(input("R$: "))
    qtde = int(input("Qtde: "))

    prod = []

    prod.append(nome)
    prod.append(preco)
    prod.append(qtde)
    produtos.update({cod: prod})

    resp = input("Deseja continuar [S|N]? ").strip().upper()

    if resp == "N":
        break

total = 0

for cod, prod in produtos.items():
    subtotal = produtos[cod][1] * produtos[cod][2]
    print(f"{prod[0]}: R$ {subtotal:.2f}")
    total += subtotal

print(20 * "-")
print(f"Total: R$ {total:.2f}")