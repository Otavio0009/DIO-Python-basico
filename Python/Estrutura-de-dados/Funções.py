'''Funções em Python são blocos de código reutilizáveis que executam uma tarefa específica.
Elas permitem organizar o código em partes menores e mais legíveis, facilitando a manutenção e a reutilização do código.
As funções são definidas usando a palavra-chave def, seguida pelo nome da função e parênteses ().
Dentro dos parênteses, podemos definir parâmetros que a função pode receber.
O código dentro da função é indentado para indicar que pertence à função.
As funções podem retornar valores usando a palavra-chave return. Se uma função não tiver um return, ela retornará None por padrão.'''

'''Exemplo de função simples:'''

def saudacao():

    print("Olá! Bem-vindo ao curso de Python.")
    
saudacao()

'''Exemplo de função com parâmetros:'''

def saudacao_personalizada(nome):

    print(f"Olá, {nome}! Bem-vindo ao curso de Python.")

saudacao_personalizada("Maria")

'''Exemplo de função com retorno:'''

def soma(a, b):

    return a + b

resultado = soma(5, 3)

print("Resultado da soma:", resultado)

'''Exemplo de função com parâmetros padrão:'''
def saudacao_com_parametro(nome="Visitante"):

    print(f"Olá, {nome}! Bem-vindo ao curso de Python.")

saudacao_com_parametro()  # Usando o valor padrão
saudacao_com_parametro("Otávio")  # Sobrescrevendo o valor padrão

'''Exemplo de função com múltiplos parâmetros:'''

def calcular_area_retangulo(base, altura):

    return base * altura

area = calcular_area_retangulo(5, 3)

print("Área do retângulo:", area)

# Retornando valores

'''Para retornar um valor de uma função, usamos a palavra-chave return seguida do valor que queremos retornar.
O valor retornado pode ser de qualquer tipo, como números, strings, listas, dicionários ou até mesmo outras funções.
Todas as funções em Python retornam um valor, mesmo que seja None por padrão. Diferente de outras linguagens,
em Python, pode retornar múltiplos valores.'''

def calcular_total(numeros):

    return sum(numeros)

def retonar_antecessor_sucessor(numero):

    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

calcular_total([9, 18, 27])  # Retorna 15
retonar_antecessor_sucessor(10)  # Retorna (9, 11)

def func_3():

    print("Hello World!")

print(func_3())  # Retorna None, pois a função não tem um return explícito

# Argumentos nomeados

'''Em Python, podemos passar argumentos para uma função usando o nome do parâmetro, em vez de apenas a posição.
Isso é especialmente útil quando uma função tem muitos parâmetros ou quando queremos tornar o código mais legível.
Ao usar argumentos nomeados, podemos especificar quais valores correspondem a quais parâmetros, independentemente da ordem em que são definidos na função.
Isso torna o código mais claro e fácil de entender.'''

# Exemplo de função com argumentos nomeados
def criar_usuario(nome, idade, email):
    return {
        "nome": nome,
        "idade": idade,
        "email": email
    }

usuario1 = criar_usuario(nome="Alice", idade=30, email="alice@example.com")
usuario2 = criar_usuario(nome="Bob", idade=25, email="bob@example.com")

print(usuario1)
print(usuario2)

# Exemplo 2

def salvar_carro(marca, modelo, ano, placa):

    print(f"Carro salvo: {marca} {modelo} ({ano}) - Placa: {placa}")

salvar_carro("Auidi", "RS Q8", 2026, "ABC-1234")
salvar_carro(modelo="RS Q8", marca="Auidi", placa="ABC-1234", ano=2026)
salvar_carro(**{"marca": "Auidi", "modelo": "RS Q8", "ano": 2026, "placa": "ABC-1234"})

#Args e Kwargs

'''Em Python, *args e **kwargs são usados para permitir que uma função aceite um número variável de argumentos.
*args é usado para passar uma quantidade variável de argumentos posicionais para uma função. Ele coleta os argumentos em uma tupla. Por exemplo: '''

def soma(*args):

    return sum(args)

print(soma(1, 2, 3))  # Retorna 6
print(soma(4, 5))     # Retorna 9

'''**kwargs é usado para passar uma quantidade variável de argumentos nomeados para uma função. Ele coleta os argumentos em um dicionário. Por exemplo:'''

def criar_usuario(**kwargs):

    return kwargs

usuario = criar_usuario(nome="Alice", idade=30, email="alice@example.com")
print(usuario)  # Retorna {'nome': 'Alice', 'idade': 30, 'email': 'alice@example.com'}

# Parametros especiais

''' Por padrão, argumentos podem ser passados para uma função Python tanto por posição quanto por nome.
Para uma melhor legibilidade e desempenho, faz sentido restringir a forma como os argumentos são passados para uma função,
assim um desenvolverdor precisa apenas olhar para a definição da função para determinar se os itens são passados por posição, posição e nome, ou por nome. Python tem uma sintaxe especial para isso: '''

# Positional-only parameters

def criar_carro_2(modelo, ano, placa, / , marca, motor, combustivel):
    
    print(f"Carro criado: {marca} {modelo} ({ano}) - Placa: {placa} - Motor: {motor} - Combustível: {combustivel}")

criar_carro_2("Dodge Charger Demon", 2026, "ABC-1234", marca="Dodge", motor="6.2L V8 Supercharged HEMI", combustivel="Gasolina")
criar_carro_2(modelo="RS Q8", ano=2026, placa="ABC-4321", marca="Audi", motor="V8 4.0 TFSI biturbo", combustivel="Gasolina")

# Keyword-only parameters

def criar_carro_3(modelo, ano, placa, *, marca, motor, combustivel):
    
    print(f"Carro criado: {marca} {modelo} ({ano}) - Placa: {placa} - Motor: {motor} - Combustível: {combustivel}")

criar_carro_3("Dodge Charger Demon", 2026, "ABC-1234", marca="Dodge", motor="6.2L V8 Supercharged HEMI", combustivel="Gasolina")
criar_carro_3(modelo="RS Q8", ano=2026, placa="ABC-4321", marca="Audi", motor="V8 4.0 TFSI biturbo", combustivel="Gasolina")

# Mixed parameters

def criar_carro_4(modelo, ano, placa, / , *, marca, motor, combustivel):
    
    print(f"Carro criado: {marca} {modelo} ({ano}) - Placa: {placa} - Motor: {motor} - Combustível: {combustivel}")

criar_carro_4("Dodge Charger Demon", 2026, "ABC-1234", marca="Dodge", motor="6.2L V8 Supercharged HEMI", combustivel="Gasolina")
criar_carro_4(modelo="RS Q8", ano=2026, placa="ABC-4321", marca="Audi", motor="V8 4.0 TFSI biturbo", combustivel="Gasolina")

# Obejetos de primeira classe

'''Em Python, funções são objetos de primeira classe, o que significa que elas podem ser tratadas como qualquer outro objeto.
Isso inclui a capacidade de atribuir funções a variáveis, passá-las como argumentos para outras funções, e retorná-las de outras funções.
Essa característica torna as funções em Python extremamente flexíveis e poderosas, permitindo a criação de código mais modular e reutilizável. Por exemplo: '''

def saudacao():

    print("Olá! Bem-vindo ao curso de Python.")

# Atribuindo a função a uma variável

saudacao_alias = saudacao

saudacao_alias()  # Chama a função através do alias

# Passando a função como argumento para outra função

def executar_saudacao(funcao):
    funcao()

executar_saudacao(saudacao)

# Retornando uma função de outra função

def criar_saudacao(nome):
    
    def saudacao():
        print(f"Olá, {nome}! Bem-vindo ao curso de Python.")
    
    return saudacao
saudacao_maria = criar_saudacao("Maria")
saudacao_maria()  # Chama a função retornada, que é a saudação personalizada para Maria

# Soma

def soma(a, b):
    
    return a + b

def exibir_resultado(funcao, a, b):
    
    resultado = funcao(a, b)
    print(f"O resultado da soma é: {resultado}")

exibir_resultado(soma, 9, 27)  # Passa a função soma como argumento para exibir_resultado

# Escopo local e global

'''Em Python, o escopo de uma variável determina onde ela pode ser acessada no código. Existem dois tipos principais de escopo: local e global.
- Escopo local: Variáveis definidas dentro de uma função são consideradas locais e só podem ser acessadas dentro dessa função. Elas não são visíveis fora da função.
- Escopo global: Variáveis definidas fora de qualquer função são consideradas globais e podem ser acessadas de qualquer lugar no código, incluindo dentro de funções. No entanto, para modificar uma variável global dentro de uma função, é necessário usar a palavra-chave global.'''

# Exemplo de escopo local

def minha_funcao():

    variavel_local = "Eu sou uma variável local"
    
    print(variavel_local)
minha_funcao()  # Imprime a variável local

# print(variavel_local)  # Isso causará um erro, pois variavel_local não é acessível fora da função

# Exemplo de escopo global

variavel_global = "Eu sou uma variável global"

def minha_funcao_global():

    print(variavel_global) # Acessa a variável global

minha_funcao_global()  # Imprime a variável global

# Modificando uma variável global dentro de uma função

contador = 0
def incrementar_contador():

    global contador  # Indica que queremos usar a variável global contador
    contador += 1

incrementar_contador()
print(contador)  # Imprime 1, mostrando que a variável global foi modificada

