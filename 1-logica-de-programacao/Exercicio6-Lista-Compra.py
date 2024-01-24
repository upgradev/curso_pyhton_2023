lista_compra = []
while True:
    print("Menu:")
    print("1. Adicionar item a lista ")
    print("2. Remover item da lista ")
    print("3. Exibir lista de compra ")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        item = input("Digite o item que deseja incluir: ")
        lista_compra.append(item)
        print("Item adicionado a lista \n")
    elif opcao == "2":
        if len(lista_compra) == 0:
            print("Alista esta vazia")
        else:
            item = input("Digite o item que deseja remover: ")
            if item in lista_compra:
                lista_compra.remove(item)
                print("Item removido da lista \n")
            else:
                print("Item não esta na lista \n")
    elif opcao == "3":
        print(lista_compra)
        print()
    elif opcao == "4":
        print("Saindo da lista!")
        break
    else:
        print("Opção invalida")
