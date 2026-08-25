a, b = map(int, input("Digite dois números: ").split())

if a < b:
    soma = 0

    for i in range(a, b):
        soma += i

        print(soma + 1)
else:
    print("ERRO!")