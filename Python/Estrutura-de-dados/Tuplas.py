'''Tuplas'''

# Tuplas em Python são imutáveis e podem conter elementos de diferentes tipos. E são definidas usando parênteses () ou nada.
# Outra forma de criar uma tupla é usando a função tuple(), no final de cada tupla acresenta-se um ",".

'''Exemplo de criação de uma tupla:'''
tupla = (1, 2, 3, 4, 5,)
print("Tupla:", tupla)

tupla2 = 1, 2, 3, 4, 5,
print("Tupla2:", tupla2)

tupla3 = tuple([1, 2, 3, 4, 5])
print("Tupla3:", tupla3)

tupla4 = tuple("Hola")
print("Tupla4:", tupla4)

tupla5 = ("Python",)
print("Tupla5:", tupla5)

'''Acessando elementos da tupla:'''

print("Primeiro elemento da tupla:", tupla[0])
print("Último elemento da tupla:", tupla[-1])
print("Elementos da tupla:", tupla[1:4])

'''Tuplas aninhadas:'''
tupla_aninhada = ((1, 2), (3, 4), (5, 6))
print("Tupla aninhada:", tupla_aninhada)

'''Acessando elementos da tupla aninhada:'''
print("Primeiro elemento da tupla aninhada:", tupla_aninhada[0])
print("Segundo elemento do segundo elemento da tupla aninhada:", tupla_aninhada[1][1])
print("Elementos do terceiro elemento da tupla aninhada:", tupla_aninhada[2][:])

'''Acessando elementos de uma tuplas aninhadas'''

for subtupla in tupla_aninhada:
    for elemento in subtupla:
        print("Elemento da tupla aninhada:", elemento)

'''Metodos de tuplas'''

# count() - Retorna o número de ocorrências de um elemento na tupla
'''Exemplo:'''
minha_tupla = (1, 2, 3, 2, 4, 2)
ocorrencias = minha_tupla.count(2)
print("Número de ocorrências de 2 na tupla:", ocorrencias)  # Saída: 3

# index() - Retorna o índice do primeiro elemento com o valor especificado
'''Exemplo:'''
indice = minha_tupla.index(3)
print("Índice de 3 na tupla:", indice)  # Saída: 2

# len() - Retorna o número de elementos na tupla
'''Exemplo:'''
tamanho = len(minha_tupla)
print("Tamanho da tupla:", tamanho)  # Saída: 6

'''Operador de fatiamento em tuplas'''
# Fatiamento básico
'''Exemplo:'''
minha_tupla = (1, 2, 3, 4,  5)
fatiamento = minha_tupla[1:4]
print("Fatiamento da tupla (1:4):", fatiamento)  # Saída: (2, 3, 4)

# Fatiamento com passo
'''Exemplo:'''
fatiamento_passo = minha_tupla[0:5:2]
print("Fatiamento da tupla com passo (0:5:2):", fatiamento_passo)  # Saída: (1, 3, 5)

# Fatiamento reverso
'''Exemplo:'''
fatiamento_reverso = minha_tupla[::-1]
print("Fatiamento reverso da tupla:", fatiamento_reverso)  # Saída: (5, 4, 3, 2, 1)

# Fatiamento até o final
'''Exemplo:'''
fatiamento_ate_final = minha_tupla[2:]
print("Fatiamento da tupla até o final (2:):", fatiamento_ate_final)  # Saída: (3, 4, 5)

# Fatiamento desde o início
'''Exemplo:'''
fatiamento_desde_inicio = minha_tupla[:3]
print("Fatiamento da tupla desde o início (:3):", fatiamento_desde_inicio)  # Saída: (1, 2, 3)

# Fatiamento completo
'''Exemplo:'''
fatiamento_completo = minha_tupla[:]
print("Fatiamento completo da tupla:", fatiamento_completo)  # Saída: (1, 2, 3, 4, 5)

# Fatiamento com índices negativos
'''Exemplo:'''
fatiamento_negativo = minha_tupla[-4:-1]
print("Fatiamento da tupla com índices negativos (-4:-1):", fatiamento_negativo)  # Saída: (2, 3, 4)

# Fatiamento com passo negativo
'''Exemplo:'''
fatiamento_passo_negativo = minha_tupla[4:1:-1]
print("Fatiamento da tupla com passo negativo (4:1:-1):", fatiamento_passo_negativo)  # Saída: (5, 4, 3)

# Fatiamento para copiar a tupla
'''Exemplo:'''
copia_tupla = minha_tupla[:]
print("Cópia da tupla usando fatiamento:", copia_tupla)  # Saída: (1, 2, 3, 4, 5)

# Fatiamento para modificar parte da tupla (tuplas são imutáveis, então criamos uma nova tupla)
'''Exemplo:'''
nova_tupla = minha_tupla[:1] + (20, 30, 40) + minha_tupla[4:]
print("Tupla após modificação com fatiamento:", nova_tupla)  # Saída: (1, 20, 30, 40, 5)

# Fatiamento para remover parte da tupla (tuplas são imutáveis, então criamos uma nova tupla)
'''Exemplo:'''
nova_tupla_removida = minha_tupla[:1] + minha_tupla[4:]
print("Tupla após remoção com fatiamento:", nova_tupla_removida)  # Saída: (1, 5)
# Fatiamento para inserir elementos na tupla (tuplas são imutáveis, então criamos uma nova tupla)
'''Exemplo:'''
nova_tupla_inserida = minha_tupla[:1] + (2,7, 3, 4) + minha_tupla[1:]
print("Tupla após inserção com fatiamento:", nova_tupla_inserida)  # Saída: (1, 2,7, 3, 4, 2, 3, 4, 5)

'''Operador de concatenação em tuplas'''
# Concatenação básica
'''Exemplo:'''
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_concatenada = tupla1 + tupla2
print("Tupla concatenada:", tupla_concatenada)  # Saída: (1, 2, 3, 4, 5, 6)
# Concatenação com repetição
'''Exemplo:'''
tupla_repetida = tupla1 * 2
print("Tupla repetida:", tupla_repetida)  # Saída: (1, 2, 3, 1, 2, 3)

'''Interação de Tuplas'''

'''Exemplo'''
carros = ("Audi", "Dodg", "Dodg Ram",)

for carro in carros:
    print(carro)

'''Exemplo 2'''
for indice, carro in enumerate(carros):
    print(f"{indice}:{carro}")