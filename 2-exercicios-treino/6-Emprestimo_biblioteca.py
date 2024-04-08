"""
Exercício Controle de Empréstimos em uma Biblioteca

Objetivo: Desenvolver um programa que auxilie Maria, uma bibliotecária, 
a controlar o número de livros emprestados por um usuário durante o mês. Para 
cada dia que o usuário exceder o limite estabelecido de livros pegos, uma multa 
será aplicada.

Instruções:

    1. O sistema de biblioteca possui um limite estabelecido de 5 
    livros que cada usuário pode pegar por vez.
    
    2. Para cada livro excedente, o usuário deve pagar uma multa de R$ 2,00.
    
    3. O programa deve começar solicitando ao usuário o número de 
    dias em que pegou livros no mês.
    
    4. Em seguida, para cada um desses dias, o programa deve pedir que 
    o usuário informe o número de livros pegos.
    
    5. O sistema deve calcular e exibir o excesso de livros e o valor 
    da multa para cada dia.
    
    6. Ao final, o programa deve mostrar o total de livros excedentes e 
    o total da multa acumulada no mês.
    
    7. Se, ao final do mês, o usuário não tiver excedido o limite em nenhum dia, 
    o programa deve mostrar uma mensagem de parabenização por seguir as regras.

Observação: O programa deve considerar que o usuário informará dados válidos, ou seja, 
valores inteiros não-negativos para o número de dias e o número de livros pegos em cada dia.
"""

LIMITE_LIVROS = 5
MULTA_POR_LIVRO = 2.00

numero_de_dias = int(
    input("Informe o número de dias em que você pegou livros nesse mês: "))

total_livros_excedentes  = 0
total_multa = 0

for dia in range(1, numero_de_dias + 1):
    numero_de_livros = int(input(f"Quantos livros você pegou no dia {dia}? "))
    
    excesso = max(0, numero_de_livros - LIMITE_LIVROS)
    multa = excesso * MULTA_POR_LIVRO
    
    if excesso > 0:
        print(f"No dia {dia} você excedeu em {excesso} em livros e deve pagar R${multa:.2f} de multa")
    else:
        print(f"No dia {dia}, você não excedeu o limite de livros.")
    
    total_livros_excedentes  += excesso
    total_multa += multa

if total_livros_excedentes > 0:
    print(f"Ao longo do mês você excedeu um total de {total_livros_excedentes} livros e deve pagar R$ {total_multa:.2f} de multa")
else:
    print(f"Parabéns por seguir as regras da biblioteca durante todo o mês.")