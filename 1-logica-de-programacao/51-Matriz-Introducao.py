# Subtração de matrizes
A = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
print("\nImprimindo matriz A")
for linha in range(3):
    for coluna in range(3):
        print(f"{A[linha][coluna]}", end=" ")
    print()

B = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nMatriz B")
for linha in range(3):
    for coluna in range(3):
        print(f"{B[linha][coluna]}", end=" ")
    print()

D = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print("\nMatriz D")
for linha in range(3):
    for coluna in range(3):
        print(f"{D[linha][coluna]}", end=" ")
    print()

print("\nSubtração das Matrizes")

for linha in range(3):
    for coluna in range(3):
        D[linha][coluna] = A[linha][coluna] - B[linha][coluna]

for linha in D:
    print(linha)

print("\nSoma das matrizes A e B")

for linha in range(3):
    for coluna in range(3):
        D[linha][coluna] = A[linha][coluna] + B[linha][coluna]

for linha in D:
    print(linha)

soma_diagonal = 0

for i in range(3):
    soma_diagonal += A[i][i]

print(f"Soma diagonal: {soma_diagonal}")

matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

soma = 0
for l in range(4):
    for c in range(4):
        if(matriz[l][c] % 2 == 0):
            soma += matriz[l][c]

print(f"Soma pares da matriz: {soma}")
