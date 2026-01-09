
'''Tipos de operadores'''
# Aritméticos:

# + (Soma)
# - (Subtração)
# * (Multiplicação)
# / (Divisão)
# % (Módulo)
# ** (Exponenciação)
# // (Divisão inteira)

#Comparação:

# == (Igual)
# != (Diferente)
# > (Maior que)
# < (Menor que)
# >= (Maior ou igual a)
# <= (Menor ou igual a)


'''Tipos de datos'''
# Int (Intero)
# Float (Decimal)
# Str (Texto)
# Bool (Booleano)
# List (Lista)
# Tuple (Tupla)
# Dict (Diccionario)
# Set (Conjunto)

'''Conversiones de tipos de dados'''
# Conversão de int
num_str = "123"
num_int = int(num_str)
print("Número convertido a entero:", num_int)

# Conversão de float
num_float = float(num_str)
print("Número convertido a flotante:", num_float)

# Conversão de str
num_str2 = str(num_int)
print("Número convertido a cadena:", num_str2)

# Conversão de bool
bool_val = bool(num_int)
print("Número convertido a booleano:", bool_val)

# Conversão de list
list_val = list(num_str)
print("Cadena convertida a lista:", list_val)

# Conversão de tuple
tuple_val = tuple(num_str)
print("Cadena convertida a tupla:", tuple_val)

# Conversão de dict
dict_val = dict.fromkeys(num_str, 0)
print("Cadena convertida a diccionario:", dict_val)

# Conversão de set
set_val = set(num_str)
print("Cadena convertida a conjunto:", set_val)


'''Entrada de datos'''
nome = input("Digite o seu nome: ")
print("Hola, " + nome + "!")

idade = int(input("Digite sua idade: "))
print("Tienes " + str(idade) + " años.")

altura = float(input("Digite sua altura em metros: "))
print("Tu altura é " + str(altura) + " metros.")


'''Comentarios'''
# Este é un comentario de uma só linha

'''
Este é um comentario
de múltiplas linhas
'''

"""Este é outro comentario
de múltiplas linhas
"""


'''Funções nativas de Python'''
# print()
# input()
# len()
# type()
# int()
# float()
# str()
# bool()
# list()
# tuple()
# dict()
# set()
# range()
# sum()
# min()
# max()
# abs()
# round()
# sorted()
# help()
# dir()
# id()
# isinstance()
# zip()
# enumerate()
# map()
# filter()
# reduce() (importar de functools)
# all()
# any()
# chr()
# ord()
# hex()
# bin()
# oct()
# eval()
# repr()
# format()
# open()
# exit()
# quit()
# vars()
# globals()
# locals()
# callable()
# memoryview()
# super()
# property()
# compile()
# hash()
# slice()
# reversed()
# __import__()
# breakpoint()
# callable()
# delattr()
# getattr()
# setattr()
# hasattr()
# compile()
# exec()
# iter()
# next()
# staticmethod()
# classmethod()
# frozenset()
# complex()
# memoryview()
# bytearray()
# bytes()
# ord()
# chr()
# pow()
# divmod()


'''Operadores lógicos'''
# and (E)
# or (OU)
# not (NÃO)


'''Operadores de atribuição'''
# = (Recebe)
# += (Soma e atribuição)
# -= (Subtração e atribuição)
# *= (Mutiplicação e atribuição)
# /= (Divisão e atribuição)
# %= (Módulo e atribuição)
# //= (Divisão inteira e atribuição)
# **= (Potencia e atribuição)
# &= (AND e atribuição)
# |= (OR e atribuição)
# ^= (XOR e atribuição)
# >>= (Deslocamento para  dereita e atribuição)
# <<= (Deslocamento para  esquerda e atribuição)


'''Operadores de pertença'''
# in (Em)
# not in (Não em)


'''Operadores de identidade'''
# is (Esta)
# is not (Não esta)


'''Operadores bit a bit'''
# & (AND bit a bit)
# | (OR bit a bit)
# ^ (XOR bit a bit)
# ~ (NOT bit a bit)
# << (Deslocamento para  esquerda)
# >> (Deslocamento para  dereita)