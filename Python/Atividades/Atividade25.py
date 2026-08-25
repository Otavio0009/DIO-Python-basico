precoDaVenda = float(input("Qual foi o valor total da compra: "))
print("Escolha entre as opições de pagamento: ")
print('''
1 - À vista: 15% de desconto
2 - Cartão de débito: 10% de desconto
3 - Cartão de crédito: 5% de desconto''')

opicoes = int(input("Qual foi a forma de pagamento escolhida: "))

if opicoes == 1:
    percentual = precoDaVenda * .15 / 100
    desconto = precoDaVenda - percentual

    print(f"O preço era {precoDaVenda:.2f}, e paçou a custar {desconto:.2f}")

elif opicoes == 2:
    percentual = precoDaVenda * .10 / 100
    desconto = precoDaVenda - percentual

    print(f"O valor da venda era {percentual:.2f}, paçou a custar {desconto:.2f}")

elif opicoes == 3:
    percentual = precoDaVenda * .05 / 100
    desconto = precoDaVenda - percentual

    print(f"O valor da venda era {precoDaVenda:.2f}, e paçou a custar {desconto:.2f}")

else:
    print("Opição não encotrada")
