# Dicionário um dentro do outro
alunos = {
    "João": {
        "Matemática": 8.5,
        "Português": 9.0,
        "História": 7.5
    },
    "Maria": {
        "Matemática": 9.5,
        "Português": 8.0,
        "Geografia": 8.7
    },
    "Pedro": {
        "Matemática": 7.0,
        "Português": 7.5,
        "História": 8.0,
        "Geografia": 9.0
    }
}

print("Acessando notas do joão em matematica")
nota_joao_matematica = alunos["João"]["Matemática"]
print(f"Nota do João em matemática: {nota_joao_matematica}")

print("Modificando a nota de Maria em geográfia")
alunos["Maria"]["Geografia"] = 9.2
print(f"Nota atualizada de maria em geografia: {alunos['Maria']['Geografia']}")

print("Adiconando uma nota de quimica para o pedro")
alunos["Pedro"]["Química"] = 8.8
print(f"Nota do Pedro em quimica: {alunos['Pedro']['Química']}")

print("\nExercicio")
estacionamento = {
    "A1": {
        "marca": "Toyota",
        "modelo": "Corolla",
        "dono": "Sr. Silva"
    },
    "B2": {
        "marca": "Honda",
        "modelo": "Civic",
        "dono": "Dona Maria"
    },
    "C3": {
        "marca": "Ford",
        "modelo": "Mustang",
        "dono": "Sr. Jorge"
    },
}
print(f"Estacionamento Antes: {estacionamento}")
print(
    f"Modelo do carro estacionado na vaga B2: {estacionamento['B2']['modelo']}")
estacionamento['A1']['dono'] = "Sra. Lucia"
print(f"Estacionamento com atualização: {estacionamento}")
estacionamento["D4"] = {
    "marca": "Chevrolet",
    "modelo": "Onix",
    "dono": "Sr. Roberto"
}
print(f"Estacionamento com atualização: {estacionamento}")

for vaga, carro in estacionamento.items():
    if carro["dono"] == "Sra. Lucia":
        print(f"marca do carro da Sra. Lucia: {carro['marca']}")
        break