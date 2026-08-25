altura1, altura2, altura3 = map(float, input("Digite altura de cada um dos três: ").split())

maior = 0
meio = 0
menor = 0

if altura1 > altura2 > altura3:
    maior = altura1
    meio = altura2
    menor = altura3

    print(maior)
    print(meio)
    print(menor)

elif altura1 > altura3 > altura2:
    maior = altura1
    meio = altura3
    menor = altura2

    print(maior)
    print(meio)
    print(menor)

elif altura2 > altura1 > altura3:
    maior = altura2
    meio = altura1
    menor = altura3

    print(maior)
    print(meio)
    print(menor)

elif altura2 > altura3 > altura1:
    maior = altura2
    meio = altura3
    menor = altura1

    print(maior)
    print(meio)
    print(menor)

elif altura3 > altura1 > altura2:
    maior = altura3
    meio = altura1
    menor = altura2

    print(maior)
    print(meio)
    print(menor)

elif altura3 > altura2 > altura1:
    maior = altura3
    meio = altura2
    menor = altura1

    print(maior)
    print(meio)
    print(menor)

else:
    print("Há, pelo menos, 2 pessoas com a mesma estatura.")