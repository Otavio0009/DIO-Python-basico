'''Um dicionário é um conjunto não-ordenado de pares chaves:valores, onde as caves são únicas em uma dada instância do dicionario.
Dicionário são delimitados por chaves: {}, e contém uma lista de psres cahve:valor separada por vírgulas.'''

# Exemplo

pessoa = {"nome": "Otávio", "idade": 19}
print(pessoa)

pessoa = dict(nome="Otávio", idade=19)
print(pessoa)

pessoa["telefone"] = "9999-8163" # Acresentado um dado e valor
print(pessoa)

'''Acessando dados'''

dados = {"nome": "Otávio", "idade": 19, "telefone": "9999-8163"}

print(dados["nome"])
print(dados["idade"])
print(dados["telefone"])

# Mundando dados

dados["nome"] = "Neto"
dados["idade"] = 20
dados["telefone"] = "8888-6381"

print(dados)

'''Dicionários aninhados'''

'''Dicionários podem armanezar qualquer tipo de objeto Python como valor, desde que a chave para esse valor um objeto imutável como (str e numeros)'''

# Exemplo

contatos = {
    "otavineto@gmail.com":{"nome": "Otávio Neto", "telefone": "9999-8163"},
    "lindalvacirne@gmail.com": {"nome": "Lindauva", "telefone": "8998-6381"},
    "otaviofilho@gmail.com": {"nome": "Otávio Filho", "telefone": "9889-1836"},
    "hudsoncirnedocarmo@gmail.com": {"nome": "Hudson", "telefone": "8888-3618"}
}

print(contatos["otavineto@gmail.com"]["telefone"])

'''Interando'''

'''A forma mais comum para percorrer os dados de um dicionario é utilizando o comado for.'''

for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)

'''Metodos'''

# .clear (lipa o dicionario)

contatos = {
    "otavineto@gmail.com":{"nome": "Otávio Neto", "telefone": "9999-8163"},
    "lindalvacirne@gmail.com": {"nome": "Lindauva", "telefone": "8998-6381"},
    "otaviofilho@gmail.com": {"nome": "Otávio Filho", "telefone": "9889-1836"},
    "hudsoncirnedocarmo@gmail.com": {"nome": "Hudson", "telefone": "8888-3618"}
}

contatos.clear()

print(contatos)

# .copy (copia o dicinario)

contatos = {
    "otavineto@gmail.com":{"nome": "Otávio Neto", "telefone": "9999-8163"},
    "lindalvacirne@gmail.com": {"nome": "Lindauva", "telefone": "8998-6381"},
    "otaviofilho@gmail.com": {"nome": "Otávio Filho", "telefone": "9889-1836"},
    "hudsoncirnedocarmo@gmail.com": {"nome": "Hudson", "telefone": "8888-3618"}
}

copia = contatos.copy()
copia["otavioneto@gmail.com"] = {"nome": "Tavin"}

print(copia["otavioneto@gmail.com"])

print(contatos["otavineto@gmail.com"])

# .fromkeys (cria chaves)

print(dict.fromkeys(["nome", "telefone"]))


print(dict.fromkeys(["nome", "telefone"], "vazio"))

# .get (acesa valores dentro deum dicionario)

contatos = {
    "otavioneto@gmail.com":{"nome": "Otávio Neto", "telefone": "9999-8163"}
}

print(contatos.get("chave"))
print(contatos.get("chave", {}))
print(contatos.get("otavioneto@gmail.com", {}))

# .items (gera uma lista de tuplas)

print(contatos.items())

# .keys (retorna apenas o valor da chave do dicionario)

print(contatos.keys())

# .pop (remove a chave)

resultado = contatos.pop("otavioneto@gmail.com")
print(resultado)

resultado = contatos.pop("otavioneto@gmail.com", {}) # "{}" está informando que esse valor não existe mais
print(resultado)

# .popitem (removi os itens na sequencia inversa)

contatos = {
    "otavineto@gmail.com":{"nome": "Otávio Neto", "telefone": "9999-8163"},
    "lindalvacirne@gmail.com": {"nome": "Lindauva", "telefone": "8998-6381"},
    "otaviofilho@gmail.com": {"nome": "Otávio Filho", "telefone": "9889-1836"},
    "hudsoncirnedocarmo@gmail.com": {"nome": "Hudson", "telefone": "8888-3618"}
}

contatos.popitem() # remove ("hudsoncirnedocarmo@gmail.com": {"nome": "Hudson", "telefone": "8888-3618"})
print(contatos)

# .setdefaut (troca ou adiciona chaves)

contatos = {"nome": "Otávio Neto", "telefone": "9999-8163"}

contatos.setdefault("nome", "Neto")
print(contatos)

contatos.setdefault("idade", 20)
print(contatos)

# .update (atualiza dicionario com outro dicionario)

contatos = {
    "otavioneto@gmail.com":{"nome": "Otávio Neto", "telefone": "9999-8163"}
}

contatos.update({ "otavioneto@gmail.com": {"nome": "Tavin"}})# atualiza o dicinario, que vai ficar "otavioneto@gmail.com": {"nome": "Tavin"}
print(contatos)

contatos.update({"hudsoncirnedocarmo@gmail.com": {"nome": "Hudson", "telefone": "8888-3618"}})

# vai unir os dois dicionarios e dicionario tem que ter parametros distinto

print(contatos)

# values() (retorna todos os valores do dicionario)

contatos = {
    "otavineto@gmail.com":{"nome": "Otávio Neto", "telefone": "9999-8163"},
    "lindalvacirne@gmail.com": {"nome": "Lindauva", "telefone": "8998-6381"},
    "otaviofilho@gmail.com": {"nome": "Otávio Filho", "telefone": "9889-1836"},
    "hudsoncirnedocarmo@gmail.com": {"nome": "Hudson", "telefone": "8888-3618"}
}

print(contatos.values())

# in (verifica se o valor esta dentro do dicionario)

print("otavineto@gmail.com" in contatos) # True
print("idade" in contatos["lindalvacirne@gmail.com"]) # False
print("cpf" in contatos["otaviofilho@gmail.com"]) # False
print("hudsoncirnedocarmo@gmail.com" in contatos) # True

# .del() excluir valores que você escoler

del contatos["otaviofilho@gmail.com"]["telefone"]
print(contatos)

del contatos["lindalvacirne@gmail.com"]
print(contatos)
