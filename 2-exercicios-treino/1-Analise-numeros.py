# Desenvolver um programa que solicita ao usuario a entrada de um numero
# e com base nesse numero realiza as seguintes operações
"""
1- mostrar o numero informado
2- Informar se o numero é par ou impar
3- Informar se o numero é positivo, negativo ou zero
4- Se o numero for positivo, calcular e mostrar sua raiz quadrada
"""
import math

numero = float(input("Digite um número: "))
print(f"O número informado foi o {numero}")
par_impar = "Par" if numero % 2 == 0 else "Ímpar"
positivo_negativo_zero = "Positivo" if numero > 0 else "Negativo" if numero < 0 else "Zero"
raiz_quadrada = math.sqrt(numero) if numero > 0 else "Não existe raiz quadrade de numero negativo"

print(f"O número {numero} é {par_impar}")
print(f"O número {numero} é {positivo_negativo_zero}")
print(f"A raiz quadrada do {numero} é {raiz_quadrada}")