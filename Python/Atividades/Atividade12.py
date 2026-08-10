import math

numero1, numero2 = map(float, input("Digite dois valores: ").split())

cuboDoSegundoNumero = numero2 ** 3
mediaGeometrica = math.sqrt(numero1 * numero2)

print(f"O cubo do segundo número é {cuboDoSegundoNumero:.2f} e a media geométrica é {mediaGeometrica:.2f}")