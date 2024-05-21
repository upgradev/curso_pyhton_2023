class FormatadorDeClasse:
    def __init__(self, frase: str) -> None:
        self.frase = frase

    def para_maiuscula(self):
        self.frase = self.frase.upper()

    def para_minuscula(self):
        self.frase = self.frase.lower()

    def capitalizar(self):
        self.frase = self.frase.capitalize()

    def formato_titulo(self):
        self.frase = self.frase.title()

    def contar_vogais(self):
        vogais = 'aeiouáéíóúàèìòùãẽõĩõũ'
        contagem = 0
        frase_minuscula = self.frase.lower()
        for letra in frase_minuscula:
            if letra in vogais:
                contagem += 1

        return contagem

    def contar_consoantes(self):
        consoantes = 'bcdfghjklmnpkrstvwxyzç'
        contagem = 0
        frase_minuscula = self.frase.lower()
        for letra in frase_minuscula:
            if letra in consoantes:
                contagem += 1

        return contagem

    def procurar_palavra(self, palavra):
        return self.frase.lower().count(palavra.lower())

    def contar_letra_a(self):
        return self.frase.lower().count('a')

    def obter_frase(self):
        return self.frase


def menu():
    print("\nBem vindo ao formatador de frase! ")

    frase = input("Por favor digite uma frase: ")

    formatador = FormatadorDeClasse(frase)

    while True:
        print("\nEscolha uma opção para form,atar a sua frase: ")
        print("1. Converter para maiúsculas")
        print("2. Converter para minúsculas")
        print("3. Capitaliza a primeira letra da frase")
        print("4. Converte a primeira letra de cada palavra da frase para maiúscula")
        print("5. Conta e retorna o números de vogais na frase")
        print("6. Conta e retorna o números de consoantes na frase")
        print("7. Conta e retorna o números de ocorrências da letra 'a' na frase")
        print("8. Conta e retorna o números de ocorrências de uma palavra específica 'a' na frase")
        print("9. Retorna a frase atual")
        print("10. Sair")

        escolha = input("Digite o número da sua escolha: ")

        if escolha == "1":
            formatador.para_maiuscula()

        elif escolha == "2":
            formatador.para_minuscula()

        elif escolha == "3":
            formatador.capitalizar()

        elif escolha == "4":
            formatador.formato_titulo()

        elif escolha == "5":
            print(f"Total de vogais: {formatador.contar_vogais()}")

        elif escolha == "6":
            print(f"Total de consoantes: {formatador.contar_consoantes()}")

        elif escolha == "7":
            print(f"Total de ocorrências da letra 'a': {
                  formatador.contar_letra_a()}")

        elif escolha == "8":
            palavra = input("Digite a palavra que você quer pesquisar: ")
            contagem = formatador.procurar_palavra(palavra=palavra)
            if contagem > 0:
                print(f"Total de ocorrências da palavra {palavra}: {contagem}")
            else:
                print(f"A palavra não foi encontrada na frase")

        elif escolha == "9":
             print(f"Frase Atual: {formatador.obter_frase()}")
             continue

        elif escolha == "10":
            print("Saindo do programa!")
            break
        print("Frase Atual: ", formatador.obter_frase())


if __name__ == "__main__":
    menu()
