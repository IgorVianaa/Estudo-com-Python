def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def main():

    peso = float(input("Digite o seu peso em quilogramas: "))
    altura = float(input("Digite a sua altura em metros: "))

    imc = calcular_imc(peso, altura)

    print(f"Seu IMC é: {imc:.2f}")

    if imc < 18.5:
        print("Você está abaixo do peso.")
    elif 18.5 <= imc < 24.9:
        print("Seu peso está normal.")
    elif 25 <= imc < 29.9:
        print("Você está com sobrepeso.")
    elif 30 <= imc < 34.9:
        print("Você está na categoria de obesidade grau 1.")
    elif 35 <= imc < 39.9:
        print("Você está na categoria de obesidade grau 2.")
    else:
        print("Você está na categoria de obesidade grau 3.")

if __name__ == "__main__":
    main()
