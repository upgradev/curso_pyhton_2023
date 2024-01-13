################ CALCULADORA SIMPLES ###############

def adicionar(a, b):
    return a + b
def subtrair(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    return a / b

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

op = input("Escolha uma operação: (adicionar, subtrair, multiplicar, dividir) ")
resultado = 0
if op == "adicionar":
    resultado = adicionar(num1, num2)
elif op == "subtrair":
    resultado = subtrair(num1, num2)
elif op == "multiplicar":
    resultado = multiplicar(num1, num2)
elif op == "dividir":
    resultado = dividir(num1, num2)
else:
    print("Operação Invalida")

print(f"Resultado: {resultado}")