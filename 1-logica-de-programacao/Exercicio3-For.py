################################## Soma dos quadrados

numero_inteiro = int(input("Digite um número inteiro: "))
soma = 0
for i in range(1, numero_inteiro + 1):
    quadrado = i**2
    soma += quadrado
    print(f"Quadrado de {i}: {quadrado}")
print(f"A soma dos quadrados é: {soma}")


################################# Tabela de Multiplicação

# numero_inteiro = int(input("Digite um número inteiro positivo: "))

# for i in range(1, 11):
#     print(f"{numero_inteiro} * {i} = {numero_inteiro * i} ")
# print("Fim da tabela de multiplicação!")