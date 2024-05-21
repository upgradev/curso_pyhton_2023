class ManipuladorDeLista:
    def __init__(self) -> None:
        self.lista = []

    def adicionar_elemento(self, elemento):
        try:
            self.lista.append(elemento)
        except ValueError:
            print("Digite um valor correto.")

    def remover_elemento(self, elemento):
        try:
            if elemento in self.lista:
                self.lista.remove(elemento)
                print("Elemento removido da lista")
        except ValueError:
            print("Elemento nao encontrado")

    def encontrar_maior(self):
        if self.lista:
            return max(self.lista)
        else:
            return "A lista esta vazia"

    def encontrar_menor(self):
        if self.lista:
            return min(self.lista)
        else:
            return "A lista esta vazia"

    def media(self):
        if self.lista:
            return sum(self.lista)/len(self.lista)
        else:
            return "A lista esta vazia"

    def mostrar_lista(self):
        return self.lista


def menu():
    manipulador = ManipuladorDeLista()

    while True:
        print("Escolha uma opção: ")
        print("1. Adicionar Elemento: ")
        print("2. Remover Elemento: ")
        print("3. Encontrar Maior Elemento: ")
        print("4. Encontrar Menor Elemento: ")
        print("5. Calcular Média: ")
        print("6. Mostrar Lista: ")
        print("7. Sair: ")

        escolha = input("Digite o número da sua escolha: ")

        if escolha == "1":

            elemento = int(
                input("Digite o elemento que você quer adicionar: "))
            manipulador.adicionar_elemento(elemento=elemento)

        if escolha == "2":

            elemento = int(
                input("Digite o elemento que você quer remover: "))
            manipulador.remover_elemento(elemento=elemento)

        elif escolha == "3":
            print(f"O maior elemento é {manipulador.encontrar_maior()}")

        elif escolha == "4":
            print(f"O menor elemento é {manipulador.encontrar_menor()}")

        elif escolha == "5":
            print(f"A média dos elementos da lista é {manipulador.media()}")

        elif escolha == "6":
            print(f"A lista atual é {manipulador.mostrar_lista()}")

        elif escolha == "7":
            print("Saindo do programa.")
            break
        else:
            print("Escolha inválida tente novamente.")


if __name__ == "__main__":
    menu()
