primeiroTermo, quantidade, razao = map(int, input("Qual é o primeiro termo da PA, qual é qualtidade de termos e a sua razão: ").split())

atualTermo = primeiroTermo
print("Pa: ")

for i in range(quantidade):
    print(atualTermo, end="=> ")
    atualTermo += razao

print("FIM!")