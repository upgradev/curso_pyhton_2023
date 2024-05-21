class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self._idade = idade
        self.__saldo = 0

    def mostrar_nome(self):
        return self.nome

    def mostrar_idade(self):
        return self._idade

    def _aumentar_idade(self):
        self._idade += 1

    def __aumentar_saldo(self, quantidade):
        self.__saldo += quantidade

    def depositar(self, quantidade):
        self.__aumentar_saldo(quantidade=quantidade)
        return self.__saldo


p = Pessoa(nome="Alice", idade=30)

print(f"{p.nome}")
print(f"{p._idade}")


# metodos publicos
print("--------------- metodos publicos")
print(p.mostrar_nome())
print(p.mostrar_nome())
print(p.mostrar_idade())
print(p.depositar(50))
print(p.depositar(50))

print("--------------- metodos protegidos")
p._aumentar_idade()
p._aumentar_idade()
print(p.mostrar_idade())

print("--------------- metodos privados")
p._Pessoa__aumentar_saldo(50)
print(p.depositar(0))