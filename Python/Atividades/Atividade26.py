peso, altura = map(float, input("Qual é oseu peso e altura para calcularmos o imc: ").split())

imc = peso / pow(altura, 2)

if 0 < imc < 18.5:
    print("Abaixo do peso")

elif imc >= 18.5 and imc < 25:
    print("Peso normal")

elif imc >= 25 and imc < 30:
    print("Sobrepeso")

elif imc >= 30 and imc < 35:
    print("Obesidade grau 1")

elif imc >= 35 and imc < 40:
    print("Obesidade grau 2")

elif imc >= 40:
    print("Obesidade grau 3")