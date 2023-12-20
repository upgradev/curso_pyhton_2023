numero_secreto1 = 7
numero_secreto2 = 3

tentativas = 5

adivinhou1 = False
adivinhou2 = False

while tentativas > 0 and (not adivinhou1 or not adivinhou2):
    print(f"Tentativas restantes: {tentativas}")

    palpite1 = int(input("Adivinhe o primeiro numero secreto (1-10) "))
    palpite2 = int(input("Adivinhe o segundo numero secreto (1-10) "))

    if palpite1 == numero_secreto1:
        print("Você adivinhou o primeiro número!")

        adivinhou1 = True
    if palpite2 == numero_secreto2:
        print("Você adivinhou o segundo número!")

        adivinhou2 = True
    if not adivinhou1 or not adivinhou2:
        print("Tente novamente!")

        tentativas -= 1

if adivinhou1 and adivinhou2:
    print("Parabéns você adivinhou ambos os números")
else:
    print(f"Você não conseguiu adivinhas os numeros. Eles eram: {numero_secreto1} e {numero_secreto2}")