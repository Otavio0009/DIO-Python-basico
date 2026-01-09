'''Manipulação de strings'''
texto = "Hola, Mundo!"
print("Texto original:", texto)
print("Texto em maiúsculas:", texto.upper())
print("Texto em minúsculas:", texto.lower())
print("Texto dividido:", texto.split(", "))
print("Texto substituído:", texto.replace("Mundo", "Python"))
print("Comprimento do texto:", len(texto))

'''Fatiamento de strings'''
mensagem = "Olá, Mundo!"

# Pega do índice 0 até o 4 (exclusivo), resultando em "Olá"
print(mensagem[0:3]) # Saída: Olá

# Pega do índice 4 até o final, resultando em "Mundo!"
print(mensagem[4:]) # Saída: Mundo!

# Pega do início até o índice 4 (exclusivo), resultando em "Olá,"
print(mensagem[:4]) # Saída: Olá,

# Pega os últimos 5 caracteres
print(mensagem[-5:]) # Saída: Mundo!

# Inverte a string
print(mensagem[::-1]) # Saída: !odnuM ,álO

# Pega do índice 0 ao 9, pulando de 2 em 2 caracteres (passo 2)
print(mensagem[0:10:2]) # Saída: OáMdo
