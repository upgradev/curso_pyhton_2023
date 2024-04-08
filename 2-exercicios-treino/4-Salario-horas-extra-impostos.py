"""
Exercício Cálculo do Salário com Horas Extras e Imposto de Renda

Objetivo: Desenvolver um programa que ajude o usuário a entender a 
composição do seu salário mensal. O programa deve considerar o valor 
recebido por hora, as horas trabalhadas no mês, o cálculo de horas 
extras e o desconto do imposto de renda.

Instruções:

    1. Solicite ao usuário o valor que ele ganha por hora.
    2. Pergunte quantas horas foram trabalhadas no mês.
    3. Calcule o salário bruto multiplicando o valor por hora 
    pelas horas trabalhadas.
    
    4. Se o usuário tiver trabalhado mais de 160 horas no mês, 
    calcule o valor das horas extras. Cada hora extra deve ser 
    compensada com um adicional de 50% sobre o valor da hora comum.
    
    5. Calcule o imposto de renda sobre o salário (considerando as horas extras). 
    O imposto de renda tem uma taxa fixa de 11% sobre o salário.
    
    6. Mostre ao usuário uma descrição detalhada contendo:
        - Salário Bruto.
        - Valor das Horas Extras (se aplicável).
        - Valor do Imposto de Renda.
        - Salário Líquido (Salário Bruto + Horas Extras - Imposto de Renda).
"""

valor_por_hora = float(input("Digite o valor recebido por hora: "))
horas_trabalhadas = float(input("Quantidade de horas trabalhadas: "))

salario_bruto = valor_por_hora * horas_trabalhadas

horas_extras = 0
valor_horas_extra = 0

if horas_trabalhadas > 160:
    horas_extras = horas_trabalhadas - 160
    valor_horas_extra = horas_extras * valor_por_hora * 0.5

imposto_renda = 0.11 * (salario_bruto + valor_horas_extra)
salario_liquido = (salario_bruto+ valor_horas_extra) - imposto_renda

print(f"Salario bruto: {salario_bruto}")
print(f"Valor hora extra: {valor_horas_extra}")
print(f"O valor do imposto de renda: {imposto_renda}")
print(f"Sĺario líquido: {salario_liquido}")