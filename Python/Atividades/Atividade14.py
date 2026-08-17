print("************************************************")
print("      CÁLCULO DE GRANDEZAS ELÉTRICAS")
print("************************************************")
print("1. Tensão (em Volt)")
print("2. Resistência (em Ohm)")
print("3. Corrente (em Ampére)")
print("************************************************")
op = int(input("Qual grandeza deseja calcular? "))

if op == 1:

    R = float(input("Digite o vlaor da corrente (em Ohm): "))
    I = float(input("Digite o valor da corrente (em Ampére): "))

    U = R * I

    print(f"\nU = {U:.2f}")

elif op == 2:
   U = float(input("Digite o vlaor da corrente (em Volt): "))
   I = float(input("Digite o valor da corrente (em Ampére): "))

   R = U / I

   print(f"\nR = {R:.2f}")

elif op == 3:
    R = float(input("Digite o vlaor da corrente (em Ohm): "))
    U = float(input("Digite o vlaor da corrente (em Volt): "))

    I = U / R

    print(f"\nI = {I:.2f}")