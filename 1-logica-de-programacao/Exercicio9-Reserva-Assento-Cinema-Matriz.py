
cinema = []

for i in range(5):  # Fileiras
    fileira = []  # fileira atual

    for j in range(10):
        fileira.append('D')
    cinema.append(fileira)


while True:
    print('\nMenu: ')
    print('1. Ver disposição dos assentos')
    print('2. Reservar Assento')
    print('3. Sair')

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        for fileira in cinema:
            for assento in fileira:
                print(assento, end=" ")
            print()
    elif escolha == '2':
        fileira = int(input("Digite o numero da fileira / Linha (0-4): "))
        assento = int(input("Digite o numero do assento / Coluna (0-9): "))

        if cinema[fileira][assento] == 'D':
            cinema[fileira][assento] = 'R'
            print('Assento reservado com sucesso!')
        else:
            print("Assento já está reservado ou ocupado.")
        
    elif escolha == '3':
        print("Obrigado por usar nosso sistema")
        break
    else:
        print("Opção inválida")

print()
