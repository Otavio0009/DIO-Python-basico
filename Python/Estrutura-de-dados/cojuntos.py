'''Conjuntos'''
'''coleção não ordenada de itens únicos (sem duplicatas), mutável, que suporta operações matemáticas como união,
interseção e diferença, sendo ideal para eliminar duplicatas e realizar verificações eficientes de pertencimento.
São definidos com chaves {} ou usando a função set(), e um conjunto vazio deve ser criado com set() para não ser confundido com um dicionário vazio {}.'''

#Exemplo

# Criando um conjunto
numeros = {1, 2, 3, 2, 4, 1}
print(numeros) # Saída: {1, 2, 3, 4} (duplicatas removidas)

# Verificando pertencimento (muito rápido)
print(3 in numeros) # Saída: True

# Operações de conjunto
outro_conjunto = {3, 4, 5, 6}
uniao = numeros | outro_conjunto # Ou numeros.union(outro_conjunto)
print(uniao) # Saída: {1, 2, 3, 4, 5, 6}

intersecao = numeros & outro_conjunto # Ou numeros.intersection(outro_conjunto)
print(intersecao) # Saída: {3, 4}

# Outa forma de criação

meu_conjunto = set((1, 2, 3, 4)) # "set" é a palavra chave para criar um conjunto
print(meu_conjunto)

'''Acessando dados'''

'''Conjuntos em python não suportam indexação e nem fatiamento, caso queira acessar os seus valores é necessário
converter o conjuto para lista'''

#Exemplo

numero = {1, 2, 3, 4, 5, 6, 7, 8, 9}

numero = list(numero) # para acessar um o index do conjuto transforma ele em uma lista

print(numero[-1])

'''Interando'''

# A forma mais comum de pecorrer um conjuto é usando for

carros = set(("Audi", "Dodge", "Dodge Ram"))

for carro in carros:
    print(carro)

# Às vezes é necessário saber qual o índice do objeto dentr do laço for. Para isso podemos usar a função enumerate

# Exemplo

for indece, carro in enumerate(carros):
    print(indece, carro)

'''Métodos'''

# .union
'''Exemplo'''
conjunto_01 = set((9, 18, 27))
conjunto_02 = set((36, 45, 54))

uniao = conjunto_02.union(conjunto_01) # a união pode ser "|"

print(uniao)

# .intersection

conjunto_01 = {9, 18, 27}
conjunto_02 = {9, 36, 54}

intersecao = conjunto_01.intersection(conjunto_02) # a interseção pode ser "&"

print(intersecao)

# .difference

conjunto_01 = set((18, 9, 45))
conjunto_02 = {9, 45, 81}

diferenca = conjunto_02.difference(conjunto_01)

print(diferenca)

diferenca = conjunto_01.difference(conjunto_02)

print(diferenca)

# .symmertic_difference

conjunto_01 = {1, 2, 3}
conjunto_02 = set((2, 3, 4))

diferenca_simetrica = conjunto_02.symmetric_difference(conjunto_01)

print(diferenca_simetrica)

# .issubset (a representação de um sub-conjunto)

conjunto_01 = set((1, 2, 3))
conjunto_02 = set((4, 1, 2, 5, 6, 3))

issbset = conjunto_01.issubset(conjunto_02)
print(issbset)

issbset = conjunto_02.issubset(conjunto_01)
print(issbset)

# .isdisjoint (a representação de conjutos dijuntos)

conjunto_01 = {1, 2, 3, 4, 5}
conjunto_02 = {6, 7, 8, 9}
conjunto_03 = {1, 0}

isdisjoint = conjunto_01.isdisjoint(conjunto_02)
print(isdisjoint)

isdisjoint = conjunto_01.isdisjoint(conjunto_03)
print(isdisjoint)

# .add (adiciona valores dentro do conjunto)

sorteio = {1, 23}

sorteio.add(25) # {1, 23, 25}
sorteio.add(42) # {1, 23, 25, 42}
sorteio.add(45) # {1, 23, 25, 42, 45}
sorteio.add(25) # {1, 23, 25, 42, 45} (Não muda pois já tem 25)

print(sorteio)

# .clear (lipa o conjuto)

sorteio.clear()

print(sorteio)

# .copy (copia o conjuto)

sorteio = {1, 23}

sorteio.copy()

print(sorteio)

# .discard (discarta algunvalor do conjunto)

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros.discard(0)
numeros.discard(1)

print(numeros)

# .pop (remove os numeros de forma ordenada, do primeiro atá o ultimo)

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros.pop() # 0
numeros.pop() # 1
numeros.pop() # 2

print(numeros)

# .remove (removeo os valores que forem colocados nele)

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros.remove(3) # 3

print(numeros)

# .len (conta a quantidades de termos dentro de um conjunto)

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

print(len(numeros))

# in (verifincado se o elemento está dentro da conjunto)

print(9 in numeros)
print(18 in numeros)

