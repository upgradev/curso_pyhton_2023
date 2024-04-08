"""
Exercício: Nome na Vertical em Escada com Variações

Desenvolva um programa com as seguintes especificações:

    1. Solicite ao usuário que digite seu nome.

    2. Pergunte ao usuário como ele deseja ver o nome exibido:
        a) Em formato de escada.
        b) Em formato de escada invertida.
        
    3. Baseado na escolha do usuário, exiba o nome conforme solicitado.

Por exemplo, se o usuário digitar o nome "ANA" e escolher a opção de 
escada, o programa deve exibir:

A
AN
ANA

Se escolher a opção de escada invertida, o programa deve exibir:

  A
 AN
ANA

"""

nome = input("Digite o seu nome: ")
print("Como deseja ver o seu nome exibido? ")
print("a) Em formato de escada? ")
print("b) Em formato de escada invertida? ")
exibir = input("Escolha a opção a ou b? ")


def nome_escala(nome):
    for n in range(0, len(nome) + 1):
        print(nome[:n])


def nome_escala_invertida(nome):
    espaco = len(nome) - 1
    for n in range(1, len(nome) + 1):
        print(" " * espaco + nome[:n])
        espaco -= 1

if exibir.lower() == 'a':
    nome_escala(nome)
elif exibir.lower() == 'b':
    nome_escala_invertida(nome)
else:
    print("Opção nao existe")
