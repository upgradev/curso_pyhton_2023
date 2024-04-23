class Jogador:
    def __init__(self, nome, posicao, numero_camisa, gosl=0) -> None:
        self.nome = nome
        self.posicao = posicao
        self.numero_camisa = numero_camisa
        self.gols = gosl


# Instanciando jogador
jogador1 = Jogador("Roberto", "Atacante", 9)
jogador2 = Jogador("Carlos", "Goleiro", 1)

print(f"{jogador1.nome} é um {jogador1.posicao} e usa a camisa número {jogador1.numero_camisa}")
print(f"{jogador2.nome} é um {jogador2.posicao} e usa a camisa número {jogador2.numero_camisa}")

jogador1.gols += 1
jogador1.gols += 1
jogador1.gols += 1
jogador1.gols += 1
jogador1.gols += 1
print(f"{jogador1.nome} marcou {jogador1.gols} gols.")
print()
print("Exercício")
# EXERCICIO FRUTAS EM UMA MERCEARIA #######################


class Fruta:
    def __init__(self, nome, preco_kilo, qtde_estoque) -> None:
        self.nome = nome
        self.preco_kilo = preco_kilo
        self.qtde_estoque = qtde_estoque

    def exibir_informacao(self):
        print(f"Nome da Fruta: {self.nome}")
        print(f"Preço por kilo: {self.preco_kilo:.2f}")
        print(f"Quantidade em estoque: {self.qtde_estoque}Kg")
        print()


fruta1 = Fruta("Maça", 10.00, 20)
fruta2 = Fruta("banana", 5.23, 10)
fruta1.exibir_informacao()
fruta2.exibir_informacao()
