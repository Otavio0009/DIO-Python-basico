numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))

print('''1. Média ponderada, com pesos 2 e 3, respectivamente
2. Quadrado da soma dos 2 números
3. Cubo do menor número''')

opicao = int(input("Escolha uma opção: "))

if opicao == 1:
    meidaPoderada = (numero1 * 2 + numero2 * 3) / (3 + 2)
    print(f"{meidaPoderada:.2f}")

elif opicao == 2:
    soma = numero1 + numero2
    quadrado = pow(soma, 2)
    print(f"{quadrado:.2f}")

elif opicao == 3:

    if numero1 > numero2:
        cubo = pow(numero2, 3)
        print(f"{cubo:.2f}")

    elif numero2 > numero1:
        cubo = pow(numero1, 3)
        print(f"{cubo:.2f}")

else:
    print("Opção inválida")