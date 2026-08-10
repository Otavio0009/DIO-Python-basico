nomeDoCorretor = input("Qual é o seu nome: ")
quantosImoveisVendidos = int(input("Qunatos imoveis foram vendidos: "))
valorTotalVendididos = float(input("Qual foi o valor total de suas vendidas: "))


comissaoFixa = quantosImoveisVendidos * 200
comissaoPercentual = valorTotalVendididos * 0.05
salarioFinal = 1500 + comissaoFixa + comissaoPercentual

print(f"Corretor: {nomeDoCorretor}")
print("Salário Base: R$ 1500.00")
print(f"Comissão por imóveis vendidos ({quantosImoveisVendidos}): R$ {comissaoFixa:.2f}")
print(f"Comissão sobre vendas (5%): R$ {comissaoPercentual:.2f}")
print(f"Salário Final: R$ {salarioFinal:.2f}")