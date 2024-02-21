def mostrar_menu():
    print("\nMENU")
    print("1. Adicionar Contato")
    print("2. Alterar Contato")
    print("3. Remover Contato")
    print("4. Listar Contatos")
    print("5. Sair")


def adicionar_contato(contatos):

    nome = input("\nDigite o nome do contato: ")
    telefone = input("\nDigite o número do telefone: ")

    contatos[nome] = telefone
    print("contato adicionado")


def alterar_contato(contatos):
    nome_atual = input("Digite o nome do contato que deseja alterar: ")

    if nome_atual in contatos:
        novo_nome = input(
            "\nDigite o novo nome para o contato (deixe em branco para manter o atual): ")
        novo_telefone = input(
            "\nDigite o novo número de telefone (deixe em branco para manter o atual): ")

        if novo_nome:
            if novo_nome in contatos:
                print(
                    "\nO nome informado já esta em uso, por favor tente um nome diferente")
                return
           
            contatos[novo_nome] = contatos[nome_atual]
            del contatos[nome_atual]
        else:
            novo_nome = nome_atual

        if novo_telefone:
            contatos[novo_nome] = novo_telefone

        print("Contato Atualizados com sucesso.")
    else:
        print("Contato Não Encontrado.")

def remover_contato(contatos):
    nome = input("Digite o nome do contato que deseja remover: ")
    
    if nome in contatos:
        del contatos[nome]
        print("\nContato removido com sucesso.")
    else:
        print("\nContato não encontrado")

def listar_contatos(contatos):

    if not contatos:
        print("\nNenhum Contato Registrado.")
        return
    for nome, telefone in contatos.items():
        print(f"\nNome: {nome}")
        print(f"Telefone: {telefone}")


def main():
    contatos = {}

    while True:
        mostrar_menu()

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_contato(contatos)
            print(contatos)
        if escolha == "2":
            alterar_contato(contatos)
            print(contatos)
        if escolha == "3":
            remover_contato(contatos)
        if escolha == "4":
            listar_contatos(contatos)
        elif escolha == "5":
            break


main()
