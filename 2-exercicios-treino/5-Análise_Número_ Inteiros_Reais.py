"""
Exercício Análise de Números Inteiros e Reais

Objetivo: Desenvolver um programa que obtenha do usuário dois 
números inteiros e um número real, e em seguida realize e apresente 
uma série de cálculos e análises relacionadas a esses números.

Instruções:

    1. Solicite ao usuário dois números inteiros.
    2. Solicite ao usuário um número real.
    3. Calcule e exiba o produto do dobro do primeiro número com metade do segundo.
    4. Calcule e exiba a soma do triplo do primeiro número com o terceiro número.
    5. Calcule e exiba o terceiro número elevado ao cubo.
    6. Determine e informe se o primeiro número é par ou ímpar.
    7. Determine e informe se o terceiro número é positivo, negativo ou zero.
    8. Calcule e mostre a média aritmética entre os três números.
"""

num_int_1 = int(input("Digite o primeiro número inteiro: "))
num_int_2 = int(input("Digite o segundo número inteiro: "))
num_real = float(input("Digite o número real: "))

produto_do_numero  = (num_int_1 * 2) * (num_int_2 / 2)
soma_triplo = (num_int_1 * 3) + num_real
elevado_ao_cubo = num_real ** 3

numero_par_impar = "É par " if num_int_1 % 2 == 0 else "É Impár"
pos_neg_zero = "É positivo" if num_real > 0 else "É negativo" if num_real < 0 else "É zero"

media_atirmetica = (num_int_1 + num_int_2 + num_real) / 3


print(f"O produto do dobro do primeiro número com metade do segundo: {produto_do_numero}")
print(f"a soma do triplo do primeiro número com o terceiro número: {soma_triplo}")
print(f"O terceiro número elevado ao cubo: {elevado_ao_cubo:.2f}")
print(f"O primeiro número é  : {numero_par_impar}")
print(f"O terceiro número é : {pos_neg_zero}")
print(f"A média aritmética entre os três números é : {media_atirmetica:.2f}")
