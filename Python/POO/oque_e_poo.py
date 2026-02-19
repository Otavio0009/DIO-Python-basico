'''O que é Programação Orientada a Objetos (POO)?
A Programação Orientada a Objetos (POO) é um paradigma de programação que organiza o código em torno de objetos, que são instâncias de classes.
Uma classe é um molde ou uma estrutura que define as características e comportamentos de um objeto.
A POO é baseada em quatro pilares principais: encapsulamento, herança, polimorfismo e abstração. Esses pilares permitem que os programadores criem
código mais modular, reutilizável e fácil de manter. A POO é amplamente utilizada em muitas linguagens de programação, incluindo Python,
Java, C++, e muitas outras. Em Python, a POO é uma parte fundamental da linguagem e é amplamente utilizada para criar aplicativos complexos e
sistemas de software. 
Em resumo, a POO é uma abordagem de programação que se concentra em objetos e classes para organizar o código, promovendo a modularidade e a
reutilização. 
Parâmetros de função: Positional-only, Keyword-only e Mixed
Em Python, os parâmetros de função podem ser classificados em três categorias: positional-only, keyword-only, e mixed. Esses tipos de parâmetros
permitem que os desenvolvedores controlem como os argumentos são passados para as funções, melhorando a clareza e a flexibilidade do código.
- Positional-only parameters: São parâmetros que só podem ser passados por posição, ou seja, sem usar o nome do parâmetro.
Eles são definidos usando uma barra (/) na definição da função. Por exemplo:
- Keyword-only parameters: São parâmetros que só podem ser passados por nome, ou seja, usando o nome do parâmetro.
Eles são definidos usando um asterisco (*) na definição da função. Por exemplo:
- Mixed parameters: São parâmetros que podem ser passados tanto por posição quanto por nome.
Eles são definidos usando uma combinação de barra (/) e asterisco (*) na definição da função. Por exemplo:

Esses tipos de parâmetros ajudam a tornar o código mais legível e a evitar erros, garantindo que os argumentos sejam passados de maneira consistente e clara.'''

# Exemplos de parâmetros de função: Positional-only, Keyword-only e Mixed

nome = "Alice"
sobrenome = "Smith"

def saudacao(nome, sobrenome):
    print(f"Olá, {nome} {sobrenome}! Bem-vindo ao curso de Python.")

saudacao(nome, sobrenome)  # Passando por posição
saudacao(nome="Alice", sobrenome="Smith")  # Passando por nome
saudacao("Alice", sobrenome="Smith")  # Passando por posição e nome

# Outro exemplo com mais parâmetros para ilustrar melhor os tipos de parâmetros:

def criar_carro(modelo, ano, placa, marca, motor, combustivel):
    
    print(f"Carro criado: {marca} {modelo} ({ano}) - Placa: {placa} - Motor: {motor} - Combustível: {combustivel}")
    
criar_carro("Dodge Charger Demon", 2026, "ABC-1234", "Dodge", "6.2L V8 Supercharged HEMI", "Gasolina")
criar_carro(modelo="RS Q8", ano=2026, placa="ABC-4321", marca="Audi", motor="V8 4.0 TFSI biturbo", combustivel="Gasolina")
