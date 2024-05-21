class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def exibir_info(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")


class Estudante(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def estudar(self):
        print(f"{self.nome} esta estudando")


class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina

    def ensinar(self):
        print(f"{self.nome} está ensinando {self.disciplina}")

# Criação objetos


pessoa = Pessoa(nome="Maria", idade=40)
estudante = Estudante(nome="Joao", idade=20, matricula="12345")
professor = Professor(nome="Maria", idade=34, disciplina="Matemática")

pessoa.exibir_info()
estudante.exibir_info()
estudante.estudar()
professor.exibir_info()
professor.ensinar()


print("\nExercicio ---------------------")


class Animal:
    def __init__(self) -> None:
        pass

    def fazer_som(self):
        print("O Animal faz o som")


class Cachorro(Animal):
    def fazer_som(self):
        print("O cachorro faz woof-woof")

    def latir(self):
        print("Woof-woof")


class Gato(Animal):
    def fazer_som(self):
        print("O gato faz miau")

    def miar(self):
        print("Miau")


animal = Animal()
animal.fazer_som()

cachorro = Cachorro()
cachorro.fazer_som()
cachorro.latir()

gato = Gato()
gato.fazer_som()
gato.miar()
