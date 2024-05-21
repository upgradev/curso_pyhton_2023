class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = None

        self.set_preco(preco)

    def get_preco(self):
        return self._preco

    def set_preco(self, valor):
        if valor >= 0:
            self._preco = valor
        else:
            print("Preço deve ser não negativo")

    def aplicar_desconto(self, desconto_percentual):
        novo_preco = self._preco * (1 - desconto_percentual / 100)
        self.set_preco(novo_preco)


p1 = Produto(nome="Camiseta", preco=50)
print(f"Preço atual de {p1._nome}: R$ {p1.get_preco()}")
p1.set_preco(60)
print(f"Novo preço de {p1._nome}: R$ {p1.get_preco()}")

p1.set_preco(-10)

p1.aplicar_desconto(10)
print(f"Preço de {p1._nome} após desconto R$ {p1.get_preco()}")


print("Exercício -------------------------------------")


class Pet:
    def __init__(self) -> None:
        self._nome = ""
        self._idade = 0
        self._peso = 0.0

    def get_nome(self):
        return self._nome

    def set_nome(self, novo_nome):
        if isinstance(novo_nome,  str) and novo_nome != "":
            self._nome = novo_nome
        else:
            print("Nome inválido")

    def get_idade(self):
        return self._idade

    def set_idade(self, idade):
        if isinstance(idade,  int) and idade >= 0:
            self._idade = idade
        else:
            print("Idade inválido")

    def exibir_informacao(self):
        print(f"Nome: {self._nome}")
        print(f"Idade: {self._idade}")
        print(f"Peso: {self._peso} Kg")

    def get_peso(self):
        return self._peso

    def set_peso(self, peso):
        if isinstance(peso,  float) and peso >= 0:
            self._peso = peso
        else:
            print("Peso inválido")


meu_pet = Pet()
meu_pet.set_nome("Buddy")
meu_pet.set_idade(12)
meu_pet.set_peso(9.2)
meu_pet.exibir_informacao()

print("\n------------------------------------------------")
meu_pet.set_nome("Totó")
meu_pet.set_idade(7)
meu_pet.set_peso(5.9)
meu_pet.exibir_informacao()