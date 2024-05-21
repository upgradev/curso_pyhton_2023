class Estudante:
    def __init__(self, nome, idade, nota) -> None:
        self.nome = nome
        self.idade = idade
        self.nota = nota

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_idade(self):
        return self.idade

    def set_idade(self, idade):
        self.idade = idade

    def get_nota(self):
        return self.nota

    def set_nota(self, nota):
        self.nota = nota


def menu():
    estudantes = []

    while True:
        print("1. Adicionar estudante")
        print("2. Atualizar nota")
        print("3. Visualizar estudante")
        print("4. Listar Estudantes")
        print("5. Sair")

        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            nome = input("Digite o nome do estudante: ")
            idade = int(input("Digite a idade do estudante: "))
            nota = float(input("Digite a nota do estudante: "))

            novo_estudante = Estudante(nome=nome, idade=idade, nota=nota)
            estudantes.append(novo_estudante)

            print(f"Estudante {nome} adicionado com sucesso!")

        elif escolha == "2":
            nome = input("Digite o nome do estudante para atualizar a nota: ")

            for estudante in estudantes:
                if estudante.get_nome() == nome:
                    nova_nota = float(
                        input("Digite a nova nota do estudante: "))
                    estudante.set_nota(nova_nota)
                    print(f"Nota do estudante {
                          estudante.get_nome()} atualizada com sucesso")
                    break
            else:
                print("Estudante não encontrado")

        elif escolha == "3":
            nome = input(
                "Digite o nome do estudante para visualizar informações: ")

            for estudante in estudantes:
                if estudante.get_nome() == nome:
                    print(f"Nome do estudante {estudante.get_nome()}, Idade: {
                          estudante.get_idade()}, Nota: {estudante.get_nota()} ")
                    break
            else:
                print("Estudante não encontrado")

        elif escolha == "4":
            print("Listando todos os estudantes")
            for estudante in estudantes:
                print(f"Nome do estudante {estudante.get_nome()}, Idade: {
                      estudante.get_idade()}, Nota: {estudante.get_nota()} ")

        elif escolha == "5":
            print("Saindo do sistema")
            break
        else:
            print("Esolha incorreta")
            break


menu()
