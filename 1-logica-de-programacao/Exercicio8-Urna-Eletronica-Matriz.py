urna = [["Alice", 0], ["Bob", 0], ["Charlie", 0]]

# Simulacao de 4 eleitores
for i in range(4):
    voto = input(
        "Digite o nome do Candidato em que deseja votar (Alice, Bob, Charlie): ")

    encontrado = False

    for candidato in urna:
        if candidato[0] == voto:
            candidato[1] += 1
            encontrado = True
            break

    if not encontrado:
        print("Voto nulo")

print("\nResultados:")

votos_maximos = -1
vencedor = ""

for candidato in urna:
    print(f"{candidato[0]}: {candidato[1]} votos")
    if candidato[1] > votos_maximos:
        votos_maximos = candidato[1]
        vencedor = candidato[0]
print(f"\nO Vencedor é {vencedor} com {votos_maximos} votos")
print()