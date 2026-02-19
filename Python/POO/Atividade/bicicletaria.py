class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.marcha = 1

    def buzinar(self):
        print("Buzinando: Biiiiii!")

    def parar(self):
        print("A bicicleta parou.")

    def acelerar(self):
        print("A bicicleta acelerou.")

    def get_cor(self):
        return self.cor
    
    def trocar_marcha(self, nov_marcha):
        print("Trocando marcha...")

        def _trocar_marcha():
            if nov_marcha > self.marcha:
                print("Marcha trocada")
            else:
                print("Marcha não foi trocada")


    '''def __str__(self):
        return f"Bicicleta: modelo={self.modelo} ano={self.ano} - Cor: {self.cor} - Valor: R${self.valor}"'''
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
    

caloi = Bicicleta("Vermelha", "Caloi 10", 2022, 1500.00)


print(f"Cor: {caloi.cor}")
print(f"Modelo: {caloi.modelo}")
print(f"Ano: {caloi.ano}")
print(f"Valor: R${caloi.valor}")

caloi.buzinar()
caloi.parar()
caloi.acelerar()
caloi.trocar_marcha(2)

caloi2 = Bicicleta("Azul", "Caloi 20", 2023, 2000.00)
Bicicleta.buzinar(caloi2) # Também pode ser chamado caloi2.buzinar()
Bicicleta.parar(caloi2) # Também pode ser chamado caloi2.parar()
Bicicleta.acelerar(caloi2) # Também pode ser chamado caloi2.acelerar()


print(f"Cor: {caloi2.get_cor()}")


print(caloi) # Saída: Bicicleta: modelo=Caloi 10 ano=2022 - Cor: Vermelha - Valor: R$1500.0
print(caloi2) # Saída: Bicicleta: modelo=Caloi 20 ano=2023 - Cor: Azul - Valor: R$2000.0