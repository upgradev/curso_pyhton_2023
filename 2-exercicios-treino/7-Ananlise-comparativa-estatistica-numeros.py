"""
Exercício - Análise Comparativa e Estatística de Números

Objetivo: Desenvolver um programa que obtenha do usuário dez números e realize 
análises estatísticas e matemáticas com base nos valores inseridos.

Instruções:

    1. Solicite ao usuário que informe dez números.
    2. Determine e exiba qual é o maior número.
    3. Determine e exiba qual é o menor número.
    4. Calcule e exiba a média dos dez números.
    5. Informe quantos dos números são pares.
    6. Informe quantos dos números são positivos.
    7. Calcule e exiba a variação (diferença) entre o maior e o menor número.
    8. Mostre a soma dos números que são maiores que a média.
    9. Informe quantos dos números são negativos.
    
Observações: O programa deve considerar que o usuário fornecerá apenas 
valores numéricos válidos. Em todas as operações, os resultados devem ser 
exibidos com até duas casas decimais, quando aplicável.

"""
NUMEROS = 10
numeros_digitados = []


for numero in range(1, NUMEROS+1):
    numero_digitado = float(input(f"Insira o {numero}° número: "))
    numeros_digitados.append(numero_digitado)

maior_numero = max(numeros_digitados)
menor_numero = min(numeros_digitados)
media = sum(numeros_digitados)/len(numeros_digitados)
pares = 0
positivos = 0
soma_maior_media = 0.0
negativos = 0

for num in numeros_digitados:
    if num % 2 == 0:
        pares += 1
    if num > 0:
        positivos += 1
    if num < 0:
        negativos += 1
    if num > media:
        soma_maior_media += num
        
variacao = maior_numero - menor_numero



print(f"O maior número é {maior_numero:.2f}")
print(f"O menor número é {menor_numero:.2f}")
print(f"A média é: {media:.2f}")
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números positivos: {positivos}")
print(f"A variação é: {variacao}")
print(f"A soma dos números que são maiores que a média é: {soma_maior_media}")
print(f"Quantidade de números negativos: {negativos}")
