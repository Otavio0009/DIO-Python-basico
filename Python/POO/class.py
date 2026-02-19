'''Classas são moldes para criar objetos, definindo um conjunto de atributos e métodos que os objetos criados a partir da classe terão.
Em Python, as classes são definidas usando a palavra-chave "class". A seguir, um exemplo básico de uma classe chamada "Carro":'''
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

def exibir_informacoes(self):
    print(f"Carro: {self.marca} {self.modelo} ({self.ano})")

# Criando um objeto a partir da classe Carro

meu_carro = Carro("Toyota", "Corolla", 2020)
meu_carro.exibir_informacoes()  # Saída: Carro: Toyota Corolla (2020)

'''No exemplo acima, a classe "Carro" tem um método especial chamado "__init__", que é o construtor da classe.
Ele é chamado automaticamente quando um novo objeto é criado a partir da classe e é usado para inicializar os atributos do objeto.
O método "exibir_informacoes" é um método regular que exibe as informações do carro. Para criar um objeto a partir da classe,
basta chamar a classe como se fosse uma função, passando os argumentos necessários para o construtor.
Depois disso, podemos chamar os métodos do objeto para realizar ações ou acessar seus atributos.
As classes são fundamentais para a programação orientada a objetos (POO) e permitem organizar o código de forma mais modular e reutilizável.
Elas também permitem a criação de hierarquias de classes, onde uma classe pode herdar atributos e métodos de outra classe,
facilitando a reutilização de código e a criação de estruturas mais complexas. Além disso, as classes em Python suportam encapsulamento,
permitindo que os atributos e métodos sejam protegidos contra acesso direto, e polimorfismo,
permitindo que objetos de diferentes classes sejam tratados de forma uniforme. Essas características tornam as classes uma ferramenta poderosa
para a construção de programas mais organizados e eficientes.'''

# Exemplo de herança em classes
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_informacoes(self):
        print(f"Veículo: {self.marca} {self.modelo}")

class Carro(Veiculo):

    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo)  # Chama o construtor da classe pai (Veiculo)
        self.ano = ano

    def exibir_informacoes(self):
        super().exibir_informacoes()  # Chama o método da classe pai (Veiculo)
        print(f"Ano: {self.ano}")

# Criando um objeto a partir da classe Carro:
meu_carro = Carro("Honda", "Civic", 2021)
meu_carro.exibir_informacoes()

# Saída:
# Veículo: Honda Civic
# Ano: 2021


'''No exemplo acima, a classe "Carro" herda da classe "Veiculo", o que significa que ela tem acesso aos atributos e métodos da classe pai.
O método "super()" é usado para chamar o construtor e os métodos da classe pai, permitindo que a classe filha (Carro) reutilize o código da
classe pai (Veiculo) e adicione suas próprias funcionalidades. Isso é um exemplo de herança, um dos pilares da programação orientada a objetos.
A herança permite criar hierarquias de classes, onde uma classe pode ser especializada a partir de outra, facilitando a reutilização de código
e a criação de estruturas mais complexas. No exemplo, a classe "Carro" é uma especialização da classe "Veiculo", adicionando o atributo "ano"
e sobrescrevendo o método "exibir_informacoes" para incluir informações adicionais sobre o ano do carro.
Isso demonstra como a herança pode ser usada para criar classes mais específicas a partir de classes mais genéricas, promovendo a
reutilização de código e a organização do programa. Além disso, a herança também permite o polimorfismo, onde objetos de diferentes classes
podem ser tratados de forma uniforme, desde que compartilhem a mesma interface (métodos). Isso torna o código mais flexível e fácil de manter.
Em resumo, as classes são uma parte fundamental da programação orientada a objetos em Python, permitindo a criação de objetos com atributos e
métodos, e a herança é um recurso poderoso que permite criar hierarquias de classes e promover a reutilização de código, tornando os programas
mais organizados e eficientes.'''