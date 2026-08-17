numeroParPositivo = int(input("Digite um numero inteiro e positivo: "))

if numeroParPositivo % 2 == 0:
    quadrado = pow(numeroParPositivo, 2)
    print(quadrado)

else:
    cubo = pow(numeroParPositivo, 3)
    print(cubo)