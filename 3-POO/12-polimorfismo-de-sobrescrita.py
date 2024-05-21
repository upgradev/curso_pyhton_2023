class Animal:
    def som(self):
        print("O animal faz um som")


class Cachorro(Animal):
    def som(self):
        print("O cachorro late")


class Gato(Animal):
    def som(self):
        print("O gato mia")


animal = Animal()

animal.som()
cachorro = Cachorro()
cachorro.som()

gato = Gato()
gato.som()

print("\n Exercicio ----------------------------")


class Veiculo:
    def mover(self):
        print("O veículo esta se movendo")


class Carro(Veiculo):
    def mover(self):
        print("O carro esta dirigindo na estrada")


class Barco(Veiculo):
    def mover(self):
        print("O barco esta navegando no mar")


class Aviao(Veiculo):
    def mover(self):
        print("O avião esta voando")


veiculo = Veiculo()
veiculo.mover()
carro = Carro()
carro.mover()
barco = Barco()
barco.mover()
aviao = Aviao()
aviao.mover()
