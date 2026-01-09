'''listas'''
# Listas em Python são mutáveis e podem conter elementos de diferentes tipos.

# Exemplo de criação de uma lista:
lista = [1, 2, 3, 4, 5]
print("Lista:", lista)

# Acessando elementos da lista:
print("Primeiro elemento:", lista[0])
print("Último elemento:", lista[-1])

# Modificando elementos da lista:
lista[0] = 10
print("Lista modificada:", lista)

# Adicionando elementos à lista:
lista.append(6)
print("Lista com novo elemento:", lista)

# Removendo elementos da lista:
lista.remove(10)
print("Lista após remoção:", lista)

# Iterando sobre a lista:
for elemento in lista:
    print("Elemento da lista:", elemento)



'''Metodos de listas'''

# append() - Adiciona um elemento ao final da lista
'''Exemplo:'''
minha_lista = [1, 2, 3]
minha_lista.append(4)
print("Lista após append:", minha_lista)  # Saída: [1, 2, 3, 4]

# insert() - Adiciona um elemento em uma posição específica
'''Exemplo:'''
minha_lista.insert(1, 5)
print("Lista após insert:", minha_lista)  # Saída: [1, 5, 2, 3, 4]

# remove() - Remove o primeiro elemento com o valor especificado
'''Exemplo:'''
minha_lista.remove(2)
print("Lista após remove:", minha_lista)  # Saída: [1, 5, 3, 4]

# pop() - Remove o elemento em uma posição específica e retorna seu valor
'''Exemplo:'''
removido = minha_lista.pop(2)
print("Elemento removido com pop:", removido)  # Saída: 3
print("Lista após pop:", minha_lista)  # Saída: [1, 5, 4]

# sort() - Ordena os elementos da lista
'''Exemplo:'''
minha_lista.sort()
print("Lista após sort:", minha_lista)  # Saída: [1, 4, 5]
#------------------------------------------------------------------------------#

'''Parâmetros opcionais do sort():'''
# Sort(reverse=True) - Ordena os elementos da lista em ordem decrescente
'''Exemplo:'''
minha_lista.sort(reverse=True)
print("Lista após sort(reverse=True):", minha_lista)  # Saída: [5, 4, 1]

# Sort(reverse=False) - Ordena os elementos da lista em ordem crescente
'''Exemplo:'''
minha_lista.sort(reverse=False)
print("Lista após sort(reverse=False):", minha_lista)  # Saída: [1, 4, 5]

# Sort(key=len) - Ordena os elementos da lista com base no comprimento dos elementos
'''Exemplo:'''
minha_lista = ['banana', 'abacaxi', 'laranja']
minha_lista.sort(key=len)
print("Lista após sort(key=len):", minha_lista)  # Saída: ['banana', 'laranja', 'abacaxi']

# Sort(key=lambda) - Ordena os elementos da lista com base em uma função lambda personalizada
'''Exemplo:'''
minha_lista = ['banana', 'abacaxi', 'laranja']
minha_lista.sort(key=lambda x: x[-1])  # Ordena com base na última letra
print("Lista após sort(key=lambda):", minha_lista)  # Saída: ['banana', 'laranja', 'abacaxi']

# Sort(key=str.lower) - Ordena os elementos da lista ignorando maiúsculas e minúsculas
'''Exemplo:'''
minha_lista = ['Banana', 'abacaxi', 'Laranja']
minha_lista.sort(key=str.lower)
print("Lista após sort(key=str.lower):", minha_lista)  # Saída: ['abacaxi', 'Banana', 'Laranja']

# Sort(key=str.upper) - Ordena os elementos da lista ignorando maiúsculas e minúsculas
'''Exemplo:'''
minha_lista = ['banana', 'Abacaxi', 'laranja']
minha_lista.sort(key=str.upper)
print("Lista após sort(key=str.upper):", minha_lista)  # Saída: ['Abacaxi', 'banana', 'laranja']

# Sort(key=None) - Ordena os elementos da lista usando a ordem padrão
'''Exemplo:'''
minha_lista = [3, 1, 4, 2]
minha_lista.sort(key=None)
print("Lista após sort(key=None):", minha_lista)  # Saída: [1, 2, 3, 4]

# Sort() com números negativos - Ordena os elementos da lista com números negativos
'''Exemplo:'''
minha_lista = [3, -1, 4, -2]
minha_lista.sort()
print("Lista após sort() com números negativos:", minha_lista)  # Saída: [-2, -1, 3, 4]

#-------------------------------------------------------------------------------------#

# reverse() - Inverte a ordem dos elementos da lista
'''Exemplo:'''
minha_lista.reverse()
print("Lista após reverse:", minha_lista)  # Saída: [5, 4, 1]

# count() - Retorna o número de ocorrências de um elemento na lista
'''Exemplo:'''
ocorrencias = minha_lista.count(4)
print("Número de ocorrências de 4:", ocorrencias)  # Saída: 1

# index() - Retorna o índice do primeiro elemento com o valor especificado
'''Exemplo:'''
indice = minha_lista.index(5)
print("Índice de 5 na lista:", indice)  # Saída: 0

# clear() - Remove todos os elementos da lista
'''Exemplo:'''
minha_lista.clear()
print("Lista após clear:", minha_lista)  # Saída: []

#copy() - Retorna uma cópia superficial da lista
'''Exemplo:'''
minha_lista = [1, 2, 3]
copia_lista = minha_lista.copy()
print("Cópia da lista:", copia_lista)  # Saída: [1, 2, 3]

# extend() - Adiciona os elementos de uma lista ao final de outra lista
'''Exemplo:'''
outra_lista = [4, 5, 6]
minha_lista.extend(outra_lista)
print("Lista após extend:", minha_lista)  # Saída: [1, 2, 3, 4, 5, 6]

# Len() - Retorna o número de elementos na lista
'''Exemplo:'''
tamanho = len(minha_lista)
print("Tamanho da lista:", tamanho)  # Saída: 6

#Sorted() - Retorna uma nova lista ordenada a partir dos elementos da lista original
'''Exemplo:'''
lista_ordenada = sorted(minha_lista)
print("Lista ordenada com sorted():", lista_ordenada)  # Saída: [1, 2, 3, 4, 5, 6]

#-------------------------------------------------------------------------------------#

'''parametros opcionais do sorted():'''
# Sorted(reverse=True) - Retorna uma nova lista ordenada em ordem decrescente
'''Exemplo:'''
lista_ordenada_desc = sorted(minha_lista, reverse=True)
print("Lista ordenada com sorted(reverse=True):", lista_ordenada_desc)  # Saída: [6, 5, 4, 3, 2, 1]

# Sorted(reverse=False) - Retorna uma nova lista ordenada em ordem crescente
'''Exemplo:'''
lista_ordenada_asc = sorted(minha_lista, reverse=False)
print("Lista ordenada com sorted(reverse=False):", lista_ordenada_asc)  # Saída: [1, 2, 3, 4, 5, 6]

# Sorted(key=len) - Retorna uma nova lista ordenada com base no comprimento dos elementos
'''Exemplo:'''
lista_strings = ['banana', 'abacaxi', 'laranja']
lista_ordenada_len = sorted(lista_strings, key=len)
print("Lista ordenada com sorted(key=len):", lista_ordenada_len)  # Saída: ['banana', 'laranja', 'abacaxi']

# Sorted(key=lambda) - Retorna uma nova lista ordenada com base em uma função lambda personalizada
'''Exemplo:'''
lista_strings = ['banana', 'abacaxi', 'laranja']
lista_ordenada_lambda = sorted(lista_strings, key=lambda x: x[-1])
print("Lista ordenada com sorted(key=lambda):", lista_ordenada_lambda)  # Saída: ['banana', 'laranja', 'abacaxi']

#-------------------------------------------------------------------------------------#

'''O perador de fatiamento em listas'''
# Fatiamento básico
'''Exemplo:'''
minha_lista = [1, 2, 3, 4, 5]
fatiamento = minha_lista[1:4]
print("Fatiamento da lista (1:4):", fatiamento)  # Saída: [2, 3, 4]
# Fatiamento com passo
'''Exemplo:'''
fatiamento_passo = minha_lista[0:5:2]
print("Fatiamento da lista com passo (0:5:2):", fatiamento_passo)  # Saída: [1, 3, 5]
# Fatiamento reverso
'''Exemplo:'''
fatiamento_reverso = minha_lista[::-1]
print("Fatiamento reverso da lista:", fatiamento_reverso)  # Saída: [5, 4, 3, 2, 1]
# Fatiamento até o final
'''Exemplo:'''
fatiamento_ate_final = minha_lista[2:]
print("Fatiamento da lista até o final (2:):", fatiamento_ate_final)  # Saída: [3, 4, 5]
# Fatiamento desde o início
'''Exemplo:'''
fatiamento_desde_inicio = minha_lista[:3]
print("Fatiamento da lista desde o início (:3):", fatiamento_desde_inicio)  # Saída: [1, 2, 3]
# Fatiamento completo
'''Exemplo:'''
fatiamento_completo = minha_lista[:]
print("Fatiamento completo da lista:", fatiamento_completo)  # Saída: [1, 2, 3, 4, 5]
# Fatiamento com índices negativos
'''Exemplo:'''
fatiamento_negativo = minha_lista[-4:-1]
print("Fatiamento da lista com índices negativos (-4:-1):", fatiamento_negativo)  # Saída: [2, 3, 4]
# Fatiamento com passo negativo
'''Exemplo:'''
fatiamento_passo_negativo = minha_lista[4:1:-1]
print("Fatiamento da lista com passo negativo (4:1:-1):", fatiamento_passo_negativo)  # Saída: [5, 4, 3]
# Fatiamento para copiar a lista
'''Exemplo:'''
copia_lista = minha_lista[:]
print("Cópia da lista usando fatiamento:", copia_lista)  # Saída: [1, 2, 3, 4, 5]
# Fatiamento para modificar parte da lista
'''Exemplo:'''
minha_lista[1:4] = [20, 30, 40]
print("Lista após modificação com fatiamento:", minha_lista)  # Saída: [1, 20, 30, 40, 5]
# Fatiamento para remover parte da lista
'''Exemplo:'''
minha_lista[1:4] = []
print("Lista após remoção com fatiamento:", minha_lista)  # Saída: [1, 5]
# Fatiamento para inserir elementos na lista
'''Exemplo:'''
minha_lista[1:1] = [2, 3, 4]
print("Lista após inserção com fatiamento:", minha_lista)  # Saída: [1, 2, 3, 4, 5]
#-------------------------------------------------------------------------------------#

'''O perador de concatenação em listas'''
# Concatenação básica
'''Exemplo:'''
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_concatenada = lista1 + lista2
print("Lista concatenada:", lista_concatenada)  # Saída: [1, 2, 3, 4, 5, 6]
# Concatenação com repetição
'''Exemplo:'''
lista_repetida = lista1 * 2
print("Lista repetida:", lista_repetida)  # Saída: [1, 2, 3, 1, 2, 3]
# Concatenação com extend()
'''Exemplo:'''
lista1.extend(lista2)
print("Lista1 após extend:", lista1)  # Saída: [1, 2, 3, 4, 5, 6]
# Concatenação com append()
'''Exemplo:'''
for elemento in lista2:
    lista1.append(elemento)
print("Lista1 após append em loop:", lista1)  # Saída: [1, 2, 3, 4, 5, 6, 4, 5, 6]
#-------------------------------------------------------------------------------------#

'''O perador de repetição em listas'''
# Repetição básica
'''Exemplo:'''
lista_original = [1, 2, 3]
lista_repetida = lista_original * 3
print("Lista repetida:", lista_repetida)  # Saída: [1, 2, 3, 1, 2, 3, 1, 2, 3]
# Repetição com loop
'''Exemplo:'''
lista_vazia = []
for _ in range(3):
    lista_vazia.extend(lista_original)
print("Lista repetida com loop:", lista_vazia)  # Saída: [1, 2, 3, 1, 2, 3, 1, 2, 3]
#-------------------------------------------------------------------------------------#

'''O perador de verificação de pertença em listas'''
# Verificação básica com in
'''Exemplo:'''
minha_lista = [1, 2, 3, 4, 5]
existe_tres = 3 in minha_lista
print("3 está na lista?", existe_tres)  # Saída: True
# Verificação básica com not in
'''Exemplo:'''
existe_seis = 6 not in minha_lista
print("6 não está na lista?", existe_seis)  # Saída: True
# Verificação com loop
'''Exemplo:'''
for elemento in [3, 6]:
    if elemento in minha_lista:
        print(f"{elemento} está na lista.")
    else:
        print(f"{elemento} não está na lista.")
#-------------------------------------------------------------------------------------#

'''O perador de iteração em listas'''
# Iteração básica com for
'''Exemplo:'''
minha_lista = [1, 2, 3, 4, 5]
for elemento in minha_lista:
    print("Elemento da lista:", elemento)
# Iteração com índice usando range()
'''Exemplo:'''
for i in range(len(minha_lista)):
    print(f"Elemento na posição {i}:", minha_lista[i])
# Iteração com enumerate()
'''Exemplo:'''
for indice, elemento in enumerate(minha_lista):
    print(f"Elemento na posição {indice}:", elemento)
#-------------------------------------------------------------------------------------#

'''O peração de listas'''
# Acessando elementos específicos
'''Exemplo:'''
minha_lista = [10, 20, 30, 40, 50]
elemento = minha_lista[2]
print("Elemento na posição 2:", elemento)  # Saída: 30
# Modificando elementos específicos
'''Exemplo:'''
minha_lista[2] = 35
print("Lista após modificação:", minha_lista)  # Saída: [10, 20, 35, 40, 50]
# Adicionando elementos específicos
'''Exemplo:'''
minha_lista.insert(2, 25)
print("Lista após inserção:", minha_lista)  # Saída: [10, 20, 25, 35, 40, 50]
# Removendo elementos específicos
'''Exemplo:'''
minha_lista.pop(3)
print("Lista após remoção:", minha_lista)  # Saída: [10, 20, 25, 40, 50]
#-------------------------------------------------------------------------------------#

'''Operações com listas'''
# Soma de listas
'''Exemplo:'''
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
soma_listas = [a + b for a, b in zip(lista1, lista2)]
print("Soma de listas:", soma_listas)  # Saída: [5, 7, 9]
# Produto de listas
'''Exemplo:'''
produto_listas = [a * b for a, b in zip(lista1, lista2)]
print("Produto de listas:", produto_listas)  # Saída: [4, 10, 18]
# Concatenação de listas
'''Exemplo:'''
concat_listas = lista1 + lista2
print("Concatenação de listas:", concat_listas)  # Saída: [1, 2, 3, 4, 5, 6]
# Interseção de listas
'''Exemplo:'''
intersecao_listas = [item for item in lista1 if item in lista2]
print("Interseção de listas:", intersecao_listas)  # Saída: []
# Diferença de listas
'''Exemplo:'''
diferenca_listas = [item for item in lista1 if item not in lista2]
print("Diferença de listas:", diferenca_listas)  # Saída: [1, 2, 3]
#-------------------------------------------------------------------------------------#

'''O peração com listas aninhadas'''
# Acessando elementos específicos em listas aninhadas
'''Exemplo:'''
lista_aninhada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
elemento = lista_aninhada[1][2]
print("Elemento na posição (1,2):", elemento)  # Saída: 6
# Modificando elementos específicos em listas aninhadas
'''Exemplo:'''
lista_aninhada[1][2] = 60
print("Lista aninhada após modificação:", lista_aninhada)  # Saída: [[1, 2, 3], [4, 5, 60], [7, 8, 9]]
# Iterando sobre listas aninhadas
'''Exemplo:'''
for sublista in lista_aninhada:
    for elemento in sublista:
        print("Elemento da lista aninhada:", elemento)  
#-------------------------------------------------------------------------------------#

'''O perações com listas aninhadas'''
# Soma de listas aninhadas
'''Exemplo:'''
lista1 = [[1, 2], [3, 4]]
lista2 = [[5, 6], [7, 8]]
soma_listas_aninhadas = [[a + b for a, b in zip(sub1, sub2)] for sub1, sub2 in zip(lista1, lista2)]
print("Soma de listas aninhadas:", soma_listas_aninhadas)  # Saída: [[6, 8], [10, 12]]
# Produto de listas aninhadas
'''Exemplo:'''
produto_listas_aninhadas = [[a * b for a, b in zip(sub1, sub2)] for sub1, sub2 in zip(lista1, lista2)]
print("Produto de listas aninhadas:", produto_listas_aninhadas)  # Saída: [[5, 12], [21, 32]]
#-------------------------------------------------------------------------------------#