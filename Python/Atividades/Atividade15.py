from math import sqrt
x1, y1 = map(float, input("Digite os pontos x1 e y1: ").split())
x2, y2 = map(float, input("Digite os pontos x2 e y2: ").split())
x3, y3 = map(float, input("Digite os pontos x3 e y3: ").split())

L1 = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
L2 = sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
L3 = sqrt((x3 - x2) ** 2 + (x3 - y2) ** 2)

cond1 = True
cond2 = True
cond3 = True

if L1 == L2 == L3:
    cond1 = False

if L1 > (L2 + L3) or L2 > (L1 + L3) or L3 > (L1 + L2):
    cond2 = False

if L1 <= (L2 + L3) or L2 <= (L1 +L3) or L3 <= (L1 + L2):
    cond3 = False

if cond1 == False or cond2 == False or cond3 == False:
    trinagulo = True

    print("\nNenhum triângulo formado \nMotivo(s): ")

    if cond1 == False:
        print("Pelo menos um dos lados é igual a 0")

    if cond2 == False:
        print("Pelo menos um dos lados é maior que a soma dos outros 2")

    if cond3 == False:
        print("Pelo monos um dos lados é menor ou igual ao módulo da diferença")

elif L1 == L2 == L3:
    print("\nTriângulo equilatero")

elif L1 != L2 and L1 != L3 and L2 != L3:
    print("\nTriângulo escaleno")

else:
    print("\nTriângulo isóceles")

if trinagulo:

    print(f"Medida do lado 1: {L1:.2f}")
    print(f"Medida do lado 2: {L2:.2f}")
    print(f"Medida do lado 3: {L3:.2f}")