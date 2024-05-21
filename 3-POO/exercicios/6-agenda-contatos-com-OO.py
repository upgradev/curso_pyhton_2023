class Contato:
    def __init__(self, nome, telefone, email) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email


class Agenda:
    def __init__(self) -> None:
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)

    def remover_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                self.contatos.remove(contato)
                return True
        return False

    def listar_contatos(self):
        return self.contatos

    def buscar_contatos(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                return contato
        return None


def menu():
    agenda = Agenda()
    while True:
        print("\nEscolha uma das opções ")
        print("1. Adiconar um novo contato: ")
        print("2. Remover um contato: ")
        print("3. Listar todos os contatos: ")
        print("4. Buscar um contato pelo nome: ")
        print("5. Sair ")

        escolha = input("Digite a opção: ")

        if escolha == "1":
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            email = input("Digite o email do contato: ")

            novo_contato = Contato(nome=nome, telefone=telefone, email=email)
            agenda.adicionar_contato(contato=novo_contato)
            print("Contato adicionado com sucesso!")

        elif escolha == "2":
            nome = input("Digite o nome do contato a ser removido: ")

            if agenda.remover_contato(nome):
                print("Contato removido com sucesso.")
            else:
                print("Contato não encontrado")

        elif escolha == "3":
            print("Listando contatos.........")

            for contato in agenda.listar_contatos():
                print(f"Nome: {contato.nome}, Telefone: {
                      contato.telefone}, Email: {contato.email}")

        elif escolha == "4":
            nome = input("Digite o nome do contato a ser encontrado: ")
            contato = agenda.buscar_contatos(nome=nome)

            if contato:
                print(f"Nome: {contato.nome}, Telefone: {
                      contato.telefone}, Email: {contato.email}")
            else:
                print("Contato não encontrado")

        elif escolha == "5":
            print("Obrigado por usar o programa de agenda!")
            break
        else:
            print("Opção invalida")


if __name__ == "__main__":
    menu()
