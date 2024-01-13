################### Exercício: Função para calcular estatistica de números
def estatisticas(*args):
    return sum(args) / len(args), max(args), min(args)

numeros = list(map(float, input("Digite uma sequencia de números separados por espaço: ").split()))

media, maior, menor = estatisticas(*numeros)
print(f"Média: {media}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")


################ Varios argumentos *args
# def soma(*args):
#     resultado = sum(args)
#     return resultado

# total = soma(2,4,5,8,10, 20, 51)
# print(total)


# def saudacao(nome):
#     print(f"Olá, {nome}! Bem Vindo(a) ao nosso programa!")

# saudacao("João")

# def soma(a, b):
#     return a + b

# resultado = soma(3, 4)
# print(f"O resultado da soma é: {resultado}")

############### argumentos default e non default
# def exibir_informacao(nome="Allan", idade=39, cidade ="Desconhecida"):
#     print(f"Nome: {nome}")
#     print(f"Idade: {idade}")
#     print(f"Cidade: {cidade}")
#     print()

# exibir_informacao("João", 25, "São Paulo")
# exibir_informacao("Maria", 30)
# exibir_informacao()


# def saudacao(nome):
#     print(f"Olá, {nome}! Bem Vindo!")

# nome_usuario = "João"
# saudacao(nome_usuario)

# def soma(a, b):
#     return a + b

# numero1 = int(input("Digite o primeiro numero: "))
# numero2 = int(input("Digite o segundo numero: "))

# resultado = soma(numero1, numero2)

# print(f"A soma é {resultado}")

# def soma(a, b):
#     return a + b
# resultado = soma(2, 3)
# print(resultado)

# resultado = soma(8, 9)
# print(resultado)