# exercicio soma de numeros pares
N = int(input("Digite um número inteiro positivo: "))
soma_pares = 0
for i in range(1, N + 1):
    if i % 2 == 0:
        print(f"número par: {i} + {soma_pares} = {i +soma_pares}")
        soma_pares += i
print(f"A soma dos pares é: {soma_pares}")

# exercicio de multiplicacao de exercicios
# resultado = 1

# for numero in range(1, 6):
#     resultado *= numero
#     print(f"Multiplicando por {numero}, o resultado é {resultado}")

#################################################
# soma = 0
# for i in range(1, 11, 2):
#     print(f"Número impar atual: {i}")
#     soma += i
# print(f"\nA soma dos número impares de 1 a 10 é: {soma}")

# for i in range(2, 12, 2):
#     print(i)


# for i in range(1, 11):
#     print(i)

# for i in range(10, 0, -1):
#     print(i)

