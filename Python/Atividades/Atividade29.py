menorPreco = float('inf')
nomeMenorPreco = ""
soma = 0


for i in range(5):
    nome = input("Qual é o nome do medicamento: ")
    preco = float(input("Qual é o preço do medicamento: "))

    soma += preco

    if preco < menorPreco:
        menorPreco = preco
        nomeMenorPreco = nome


media = soma / 5

print(f"O medicamento mais barato é {nomeMenorPreco}, e o seu valor é de {menorPreco:.2f}R$")
print(f"Media de preços: {media:.2f}R$")