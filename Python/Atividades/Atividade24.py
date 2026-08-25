from math import sqrt

a, b, c = map(float, input("informe os valores de A, B e C: ").split())

delta = pow(-b, 2) -4*a*c

if delta > 0:
    x1 = -b + sqrt(delta) / 2*a
    print(x1)

    x2 = -b - sqrt(delta) / 2*a
    print(x2)

elif delta == 0:
    x = -b / 2*a
    print(x)

else:
    print("Não existem raízes reais")