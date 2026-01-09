'''Matrizes'''
# Matrizes em Python são listas de listas, permitindo a criação de estruturas bidimensionais.
# Exemplo de criação de uma matriz:
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matriz:", matriz)

# Acessando elementos da matriz:
print("Elemento na posição (0,0):", matriz[0][0])
print("Elemento na posição (1,2):", matriz[1][2])
print("Elemento na posição (2,1):", matriz[2][1])

# Modificando elementos da matriz:
matriz[0][0] = 10
print("Matriz modificada:", matriz)

# Iterando sobre a matriz:
for linha in matriz:
    for elemento in linha:
        print("Elemento da matriz:", elemento)  

# Metodos de matrizes:

# append() - Adiciona uma nova linha à matriz
'''Exemplo:'''
matriz.append([10, 11, 12])
print("Matriz após append:", matriz)

# pop() - Remove a última linha da matriz
'''Exemplo:'''
removida = matriz.pop()
print("Linha removida com pop:", removida)
print("Matriz após pop:", matriz)

# O perador len() - Retorna o número de linhas na matriz
'''Exemplo:'''
num_linhas = len(matriz)
print("Número de linhas na matriz:", num_linhas)

# O perador len() - Retorna o número de colunas na matriz
'''Exemplo:'''
num_colunas = len(matriz[0])
print("Número de colunas na matriz:", num_colunas)

# O peração com matrizes - Acessando elementos específicos
'''Exemplo:'''
elemento = matriz[1][1]
print("Elemento na posição (1,1):", elemento)

# O peração com matrizes - Modificando elementos específicos
'''Exemplo:'''
matriz[1][1] = 55
print("Matriz após modificação:", matriz)

# O peração com matrizes - Iterando sobre a matriz
'''Exemplo:'''
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f"Elemento na posição ({i},{j}):", matriz[i][j])
#-------------------------------------------------------------------------------------#

# O perações com matrizes - Soma de matrizes
'''Exemplo:'''
matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matriz2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]
soma_matrizes = [[matriz1[i][j] + matriz2[i][j] for j in range(len(matriz1[0]))] for i in range(len(matriz1))]
print("Soma de matrizes:", soma_matrizes)

# Operações com matrizes - Subtração de matrizes
'''Exemplo:'''
subtracao_matrizes = [[matriz1[i][j] - matriz2[i][j] for j in range(len(matriz1[0]))] for i in range(len(matriz1))]
print("Subtração de matrizes:", subtracao_matrizes)

# Operações com matrizes - Divisão de matrizes
'''Exemplo:'''
divisao_matrizes = [[matriz1[i][j] / matriz2[i][j] for j in range(len(matriz1[0]))] for i in range(len(matriz1))]
print("Divisão de matrizes:", divisao_matrizes)

# Operações com matrizes - Transposição de matrizes
'''Exemplo:'''
transposicao_matriz = [[matriz1[j][i] for j in range(len(matriz1))] for i in range(len(matriz1[0]))]
print("Transposição de matriz:", transposicao_matriz)

# Operações com matrizes - Multiplicação por escalar
'''Exemplo:'''
escalar = 2
multiplicacao_escalar = [[matriz1[i][j] * escalar for j in range(len(matriz1[0]))] for i in range(len(matriz1))]
print("Multiplicação por escalar:", multiplicacao_escalar)

# Operações com matrizes - Determinante de matrizes 2x2
'''Exemplo:'''
matriz_2x2 = [
    [4, 6],
    [3, 8]
]
determinante = matriz_2x2[0][0] * matriz_2x2[1][1] - matriz_2x2[0][1] * matriz_2x2[1][0]
print("Determinante da matriz 2x2:", determinante)

# Operações com matrizes - Determinante de matrizes 3x3
'''Exemplo:'''
matriz_3x3 = [
    [6, 1, 1],
    [4, -2, 5],
    [2, 8, 7]
]
determinante_3x3 = (matriz_3x3[0][0] * (matriz_3x3[1][1] * matriz_3x3[2][2] - matriz_3x3[1][2] * matriz_3x3[2][1]) -
                    matriz_3x3[0][1] * (matriz_3x3[1][0] * matriz_3x3[2][2] - matriz_3x3[1][2] * matriz_3x3[2][0]) +
                    matriz_3x3[0][2] * (matriz_3x3[1][0] * matriz_3x3[2][1] - matriz_3x3[1][1] * matriz_3x3[2][0]))
print("Determinante da matriz 3x3:", determinante_3x3)

# O perações com matrizes - Produto de matrizes
'''Exemplo:'''
produto_matrizes = [[sum(matriz1[i][k] * matriz2[k][j] for k in range(len(matriz1[0]))) for j in range(len(matriz2[0]))] for i in range(len(matriz1))]
print("Produto de matrizes:", produto_matrizes)

#-------------------------------------------------------------------------------------#