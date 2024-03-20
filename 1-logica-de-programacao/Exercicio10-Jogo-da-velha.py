tabuleiro = []

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(" ")
    tabuleiro.append(linha)


def exibir_tabuleiro():
    for linha in tabuleiro:
        print('|'.join(linha))
        print("-"*5)


def verificar_vencedor(jogador):
    for i in range(3):
        todas_celulas_linha = True
        todas_celulas_coluna = True
        for j in range(3):
            if tabuleiro[i][j] != jogador:
                todas_celulas_linha = False
            if tabuleiro[j][i] != jogador:
                todas_celulas_coluna = False
        if todas_celulas_linha or todas_celulas_coluna:
            return True

        if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
            return True
        if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
            return True
        return False


def jogada(jogador):
    while True:
        jogada = input(
            f"Jogador {jogador}, escolha a linha e coluna (ex: 0 2): ")

        try:
            linha, coluna = map(int, jogada.split())

            if tabuleiro[linha][coluna] == ' ':
                tabuleiro[linha][coluna] = jogador
                break
            else:
                print("Posição já ocupada. Tente novamente.")
        except:
            print("Entrada invalida. Tente Novamente.")


jogador_atual = 'X'

for _ in range(9):
    exibir_tabuleiro()

    jogada(jogador_atual)

    if verificar_vencedor(jogador_atual):
        exibir_tabuleiro()
        print(f"Jogador {jogador_atual} venceu")
        break

    jogador_atual = 'O' if jogador_atual == 'X' else 'X'

else:
    exibir_tabuleiro()
    print("Empate")

print()
