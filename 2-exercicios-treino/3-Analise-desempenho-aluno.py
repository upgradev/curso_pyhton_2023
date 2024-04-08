"""
Programa que avalie o desempenho de um aluno ao 
longo dos bimestres. Para isso, o profgrama deve solicitar as quatro
notas bimestrais do aluno e, com base nelas, realizar as seguintes açõe

1- calcular e exibir a media das notas
2- determinar e mostrar a maior e a menor nota entre as inseridas
3- com base na media, informar ao usuario se o aluno esta aprovado,
em recuperação ou reprovado> Critérios:
aprovado: media >= 7
em recuperação: 5 <= media < 7
reprovado: media < 5
4- Calcular e mostrar a quantidade de notas que estãoa cima da media calculada
"""

nota1 = float(input("Digite a nota do primeiro bimestre: "))
nota2 = float(input("Digite a nota do segundo bimestre: "))
nota3 = float(input("Digite a nota do terceiro bimestre: "))
nota4 = float(input("Digite a nota do quarto bimestre: "))

media = (nota1 + nota2 + nota3 + nota4) / 4
maior_nota = max(nota1, nota2, nota3, nota4)
menor_nota = min(nota1, nota2, nota3, nota4)


print(f"A média das notas é: {media}")
print(f"A maior nota é: {maior_nota}")
print(f"A menor nota é: {menor_nota}")

if media >= 7:
    print("Aprovado")
elif media >= 5 and media < 7:
    print("Recuperação")
else:
    print("Reprovado")

contador = 0

for nota in [nota1, nota2, nota3, nota4]:
    if nota > media:
        contador += 1

print(f"Quantidade de notas acima da média é: {contador}")