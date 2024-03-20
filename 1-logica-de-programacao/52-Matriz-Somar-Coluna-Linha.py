M = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print(M)

for linha in range(4):
    for coluna in range(4):
        print(f"{M[linha][coluna]}", end=" ")
    print()

soma_coluna = 0
coluna_especifica = 1
for linha in range(4):
    soma_coluna += M[linha][coluna_especifica]

print(f"A soma dos valores da coluna {coluna_especifica} é {soma_coluna}")

linha_especifica = 0
soma_linha = 0

for coluna in range(4):
    soma_linha += M[linha_especifica][coluna]

print(f"A soma dos valores da linha {linha_especifica} é {soma_linha}")

# ############### Exemplo matriz e media de notas

matriz_alunos = []

for i in range(3):
    nome = input(f"Digite o nome do aluno {i + 1}: ")

    notas = []
    for j in range(4):
        nota = int(input(f"Digite a nota {j + 1} do aluno {nome}: "))
        notas.append(nota)

    matriz_alunos.append([nome] + notas)

for aluno in matriz_alunos:
    nome = aluno[0]
    notas = aluno[1:]
    media = sum(notas) / 4

    print("\n" + "-"*40)
    print(f"Nome: {nome}")
    print(f"Notas: {notas}")
    print(f"Média: {media}")
