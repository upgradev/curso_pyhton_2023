class Calculadora:
    def somar(self, num1, num2, num3=None):
        if (num3 is None):
            return num1 + num2
        else:
            return num1 + num2 + num3


calc = Calculadora()
print(calc.somar(5, 3))
print(calc.somar(5, 3, 2))

print("\n Exercicio----------")


class Impressora:

    def imprimir(self, dado):
        if isinstance(dado, str):
            print(f"Imprimindo texto {dado}")

        elif isinstance(dado, list):
            print(f"Imprimindo lista de textos")
            for item in dado:
                print(f" - {item}")
        elif isinstance(dado, dict):
            print(f"Imprimindo dicionario de textos")
            for chave, valor in dado.items():
                print(f" - {chave}: {valor}")
        else:
            print("Tipo de dado não suportado para impressão")


impressora = Impressora()
impressora.imprimir(dado="Olá mundo")
impressora.imprimir(dado=["Olá", "Mundo", "!"])
impressora.imprimir(dado={"saudacao": "Olá", "Objeto": "Mundo"})
impressora.imprimir(dado=42)
