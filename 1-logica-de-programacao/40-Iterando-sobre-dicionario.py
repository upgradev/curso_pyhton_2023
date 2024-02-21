notas = {
    "Matemática": 8.5,
    "Português": 9.0,
    "História": 7.5,
    "Geografia": 8.0,
    "Química": 9.5
}

print("Iteração sobre as chaves")
print("Materias cursadas pelo aluno: ")
for materia in notas:
    print(f"{materia}")

print("Materias usando o keys()")
for materia in notas.keys():
    print(f"{materia}")

print("Iterando apenas sobre os valores")
print("Notas do aluno: ")
total = 0
for nota in notas.values():
    print(nota)
    total += nota

media = total / len(notas)
print(f"Média das notas: {media}")

print("Iterando sobre as chaves e valores juntos")
for materia, nota in notas.items():
    print(f"{materia} : {nota}")


# Exercicio
vendas = {
    "Janeiro": 120,
    "Fevereiro": 150,
    "Março": 80,
    "Abril": 190,
    "Maio": 210
}

print("\nExercícios")
print("Iterando sobre as chaves meses")
for meses in vendas.keys():
    print(meses)

total = 0
vendas_baixa = float("inf")
mes_venda_baixa = ""
for valores in vendas.values():
    total += valores
    if valores < vendas_baixa:
        vendas_baixa = valores

for mes, venda in vendas.items():
    if venda == vendas_baixa:
        mes_venda_baixa = mes
        break

print(f"Total de vendas: {total}")
print(f"O mês com a menor venda é: {mes_venda_baixa} com {vendas_baixa} livros vendidos")