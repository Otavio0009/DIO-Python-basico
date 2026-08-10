from math import sqrt

x1 = float(input("Qual é o valor do ponto X1: "))
x2 = float(input("Qual é o valor do ponto X2: "))
y1 = float(input("Qual é o valor do ponto Y1: "))
y2 = float(input("Qual é o valor do ponto Y2: "))

distacia = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

print(f"A distancia entre os pontos P1 e P2 são de {distacia:.2f}")