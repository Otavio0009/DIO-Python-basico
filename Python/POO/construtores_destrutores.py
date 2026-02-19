'''Construtores e Destrutores em Python - O que são e como utilizá-los?
Construtores e destrutores são métodos especiais em Python que são usados para inicializar e limpar os objetos de uma classe, respectivamente.
O construtor é definido usando o método especial "__init__" e é chamado automaticamente quando um novo objeto é criado a partir da classe.
Ele é usado para inicializar os atributos do objeto e pode receber parâmetros para configurar o objeto de acordo com as necessidades do programador.
Por exemplo:'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Criando um objeto a partir da classe Pessoa

pessoa1 = Pessoa("Alice", 30)
print(pessoa1.nome)  # Saída: Alice
print(pessoa1.idade)  # Saída: 30

'''No exemplo acima, a classe "Pessoa" tem um construtor definido pelo método "__init__", que recebe os parâmetros "nome" e "idade"
para inicializar os atributos do objeto. Quando criamos um objeto "pessoa1" a partir da classe "Pessoa", o construtor é chamado automaticamente,
e os atributos "nome" e "idade" são configurados com os valores fornecidos.
O construtor é uma parte fundamental da programação orientada a objetos, pois permite que os objetos sejam criados e configurados de maneira
eficiente e organizada. Ele também pode ser usado para realizar outras tarefas de inicialização, como abrir arquivos, estabelecer conexões
de banco de dados ou configurar recursos necessários para o funcionamento do objeto.'''

'''O destrutor, por outro lado, é definido usando o método especial "__del__" e é chamado automaticamente quando um objeto é destruído ou
coletado pelo coletor de lixo do Python. Ele é usado para liberar recursos ou realizar ações de limpeza antes que o objeto seja completamente
removido da memória. Por exemplo:'''

class Arquivo:
    def __init__(self, nome):
        self.nome = nome
        self.arquivo = open(nome, 'w')

    def escrever(self, texto):
        self.arquivo.write(texto)

    def __del__(self):
        self.arquivo.close()

# Criando um objeto a partir da classe Arquivo

arquivo1 = Arquivo("exemplo.txt")
arquivo1.escrever("Olá, mundo!")
del arquivo1  # O destrutor é chamado automaticamente para fechar o arquivo

print("Arquivo criado e escrito com sucesso.")

'''No exemplo acima, a classe "Arquivo" tem um construtor que abre um arquivo para escrita e um destrutor que fecha o arquivo quando o
objeto é destruído. Quando criamos um objeto "arquivo1" a partir da classe "Arquivo", o construtor é chamado para abrir o arquivo
"exemplo.txt". Depois de escrever no arquivo, chamamos "del arquivo1" para destruir o objeto, o que aciona o destrutor e fecha o arquivo
corretamente. É importante notar que o uso do destrutor "__del__" em Python pode ser imprevisível,
pois a coleta de lixo é feita de forma automática e pode não ocorrer imediatamente quando um objeto é destruído.
Portanto, é recomendado usar o destrutor apenas para liberar recursos que precisam ser fechados explicitamente,
como arquivos ou conexões de banco de dados, e não para realizar outras tarefas de limpeza.'''

'''Em resumo, os construtores e destrutores são métodos especiais em Python que desempenham um papel crucial na criação e destruição de objetos.
O construtor "__init__" é usado para inicializar os atributos do objeto, enquanto o destrutor "__del__" é usado para liberar recursos ou realizar
ações de limpeza antes que o objeto seja completamente removido da memória. Ambos são fundamentais para a programação orientada a objetos e
ajudam a garantir que os objetos sejam criados e destruídos de maneira eficiente e organizada.'''

# Exemplo de uso de construtores e destrutores em uma classe de bicicleta


class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def __del__(self):
        print(f"A bicicleta {self.modelo} foi destruída.")

# Criando um objeto a partir da classe Bicicleta
bicicleta1 = Bicicleta("Vermelha", "Caloi 10", 2022, 1500.00)

print(f"Cor: {bicicleta1.cor}")
print(f"Modelo: {bicicleta1.modelo}")
print(f"Ano: {bicicleta1.ano}")
print(f"Valor: R${bicicleta1.valor}")
del bicicleta1  # O destrutor é chamado automaticamente para imprimir a mensagem de destruição da bicicleta

'''No exemplo acima, a classe "Bicicleta" tem um construtor que inicializa os atributos "cor", "modelo", "ano" e "valor" do objeto.
O destrutor é definido para imprimir uma mensagem quando a bicicleta é destruída. Quando criamos um objeto "bicicleta1" a partir da classe
"Bicicleta", o construtor é chamado para configurar os atributos do objeto.
Depois de imprimir as informações da bicicleta, chamamos "del bicicleta1" para destruir o objeto, o que aciona o destrutor e imprime a mensagem
indicando que a bicicleta foi destruída.
'''