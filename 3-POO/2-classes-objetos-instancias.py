class Carro:
    def __init__(self, marca, modelo, cor) -> None:
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 10
        # print(f"Velocidade atual: {self.velocidade} Km/h")

    def frear(self):
        self.velocidade -= 10
        if self.velocidade < 0:
            self.velocidade = 0
        print(f"Velocidade atual: {self.velocidade} Km/h")

    def exibir_info(self):
        print(
            f"Marca: {self.marca}, Modelo: {self.modelo}, Cor: {self.cor}, Velocidade: {self.velocidade} Km/h")


lista_carros = []

while True:

    print("\n--- Menu ---")
    print("1. Adicionaro novo carro.")
    print("2. Exibir informações dos carros.")
    print("3. Acelerar um carro.")
    print("4. Frear um carro.")
    print("5. Sair.")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        marca = input("Digite a marca do carro: ")
        modelo = input("Digite o modelo do carro: ")
        cor = input("Digite a cor do carro: ")

        novo_carro = Carro(marca, modelo, cor)
        lista_carros.append(novo_carro)

    elif escolha == "2":
        if lista_carros:
            for carro in lista_carros:
                carro.exibir_info()
        else:
            print("Nenum carro adicionado ainda. ")

    elif escolha == "3":
        modelo = input("Digite o modelo do carro que você quer acelerar: ")
        for carro in lista_carros:
            if carro.modelo == modelo:
                carro.acelerar()
                print("Achou")
                break
        else:
            print("Modelo não encontrado")

    elif escolha == "4":
        modelo = input("Digite o modelo do carro que você quer frear: ")
        for carro in lista_carros:
            if carro.modelo == modelo:
                carro.frear()
                print("Achou")
                break
        else:
            print("Modelo não encontrado")

    elif escolha == "5":
        print("Saindo do programa")
        break
    else:
        print("Opção invalida tente novamente")


# Instanciando objetos
# carro1 = Carro("Toyota", "Corolla", "Branco")
# carro1.exibir_info()
# carro1.acelerar()
# carro1.acelerar()
# carro1.acelerar()
# carro1.frear()
# carro1.frear()
# carro1.frear()
# print()
# carro2 = Carro("Ford", "Fiesta", "Azul")
# carro2.exibir_info()
# carro2.acelerar()
# carro2.acelerar()
# carro2.frear()
