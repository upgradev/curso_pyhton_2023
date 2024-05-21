class Animal:
    def falar(self):
        print("O animal esta falando")


class Cachorro(Animal):

    def falar(self):
        super().falar()
        print("O cachorro diz: au au")


animal = Animal()
animal.falar()

cachorro = Cachorro()
cachorro.falar()


print("\n Exercicio ---------------------------")


class Veiculo:
    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        print(f"Veiculo da marca {self.marca}, modelo {self.modelo}")


class Carro(Veiculo):

    def __init__(self, marca, modelo, cor) -> None:
        super().__init__(marca, modelo)
        self.cor = cor

    def exibir_info(self):
        super().exibir_info()
        print(f"Cor do carro: {self.cor}")

veiculo = Veiculo(marca="Ford", modelo="Mustang")
veiculo.exibir_info()

carro = Carro(marca="Honda", modelo="Honda civic", cor="Preto")
carro.exibir_info()