# Adicionando itens
produto = {
    "id": 12345,
    "nome": "Camisa Polo",
    "cor": "Vermelho",
    "preco": 49.90,
    "estoque": 100
}

produto["marca"] = "FashionBrand"
produto["desconto"] = 10

print(f"Após adicionar itens: {produto} ")

# Atualizar itens
produto["preco"] = 59.90
produto["desconto"] = 15
print(f"Após atualizar itens: {produto} ")

# Removendo itens
del produto["desconto"]  # Remove o item do desconto do dicionario
cor_removida = produto.pop("cor")
print(f"Cor removida: {cor_removida}")
print(f"Após deletar itens: {produto} ")

item_removido = produto.popitem()  # remove o último item inserido
print(f"Item removido: {item_removido}")

# Copiando dicionário
# Método copy
produto_copia_1 = produto.copy()  # cópia mais profunda
# Método dict
produto_copia_2 = dict(produto)  # cópia mais rasa

print(f"Cópias do produto: ")
print(f"Cópia 1: {produto_copia_1}")
print(f"Cópia 2: {produto_copia_2}")

# Exercício

aluno = {
    "matricula": "A12345",
    "nome": "João Silva",
    "curso": "Engenharia de computação",
    "semestre": 5,
    "cr": 8.5
}

# Adicionando itens
aluno["hobbies"] = ["Leitura", "Corrida", "Xadrez"]
aluno["idade"] = 22
print(aluno)

# Atualizar
aluno["semestre"] = 6
aluno["cr"] = 8.7
print(aluno)

# Remover
del aluno["idade"]
print(aluno)

hobbies_removidos = aluno.pop("hobbies")
print(f"Hobbies removidos: {hobbies_removidos}")

item_removido = aluno.popitem()
print(f"Item removido: {item_removido}")
print(f"Aluno: {aluno}")

copia_1 = aluno.copy()
print(f"Copia 1 com copy: {copia_1}")

copia_2 = dict(aluno)
print(f"Copia 2 com dict: {copia_2}")