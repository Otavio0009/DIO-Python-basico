print('''**** TABELA VERDADE ****
1. Operador AND
2. Operador OR
3. Operador NOT
**************************''')

opcao = int(input("Digite um opção: "))

if opcao == 3:
    bit = int(input("Informe o um Bit(0/1): "))

    resultado = 1 if bit == 0 else 0

    print(f"Resultado de NOT {bit} = {resultado}")

elif opcao == 2:
    bit1 = int(input("Informe o 1º bit (0/1): "))
    bit2 = int(input("Informe o 2º bi t(0/1): "))

    resultado = bit1 | bit2

    print(f"Resultado de {bit1} OR {bit2} = {resultado}")

elif opcao == 1:
    bit1 = int(input("Informe o 1º bit (0 ou 1): "))
    bit2 = int(input("Informe o 2º bit (0 ou 1): "))

    resultado = bit1 & bit2

    print(f"Resultado de {bit1} AND {bit2} = {resultado}")