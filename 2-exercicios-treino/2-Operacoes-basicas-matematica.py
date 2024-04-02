"""
programa que solicite ao usuario a entrada de dois numeros e,
com base nesses numeros, realize as seguintes operações
1- calcular e mostrar a soma dos dois numeros
2- calcular e mostrar a subtração do primeiro numero pelo segundo
3- calcular e mostrar a multiplicação dos dois numeros
4- calcular e mostrar a divisao do primeiro pelo segundo (se o segundo nao for zero)
5- verificar e informar se algum dos numeros (ou ambos) é zero
6- calcular e mostrar a media dos dois numeros
7- comparar os dois numeros e informar qual é o maior numero ou se são iguais
"""

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return 0
def verificarSeEZero(num1, num2):    
    return "O primeiro é zero " if num1 == 0 else "O segundo é zero" if num2 == 0 else "Ambos são" if num1 and num2 ==0 else "Nenhum é zero"

def media(num1, num2):
    return (num1 + num2) / 2

def maior_menor_igual(num1, num2):
    return "O primeiro é maior que o segundo " if num1 > num2 else "O segundo é maior que o primeiro " if num2 > num1 else "São iguais"

print(f"A soma é: ", soma(num1, num2))
print(f"A subtração é: ",subtracao(num1, num2))
print(f"A multiplicação é: ",multiplicacao(num1, num2))
print(f"A divisão é: ",divisao(num1, num2))
print(verificarSeEZero(num1, num2))
print(f"A média é: ",media(num1, num2))
print(maior_menor_igual(num1, num2))