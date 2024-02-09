# INTRODUÇÃO AOS DICIONARIOS
# exemplo prático
livro = {
    "titulo": "1984",
    "autor": "George Orwell",
    "ano": 1949,
}

print(livro["titulo"])

# diferença entre lista, tuplas e dicionários
frutas = ["maça", "banana", "cereja"]
print(frutas[1])

coordenadas = (4.5, 6.7)
print(coordenadas[0])

contatos = {
    "Alice": "555-1234",
    "Bob": "555-5678"
}
print(contatos["Alice"])

# CRIANDO DICIONÁRIOS
# Sintaxe básica
carro = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": 1964
}
print(carro)

# dicionario vazio
pessoa = {}
print(pessoa)

# dicionário com múltiplos itens
pessoa = {
    "nome": "Maria",
    "idade": 30,
    "profissao": "Engenheira",
    "nacionalidade": "Brasileira"
}
print(pessoa)

# Dicionários aninhados
familia = {
    "pai": {
        "nome": "Roberto",
        "idade": 50
    },
    "mae": {
        "nome": "Clara",
        "idade": 48
    },
    "filho": {
        "nome": "Pedro",
        "idade": 22
    }
}

print(familia["pai"]["nome"])

# EXERCÍCIO
animal = {
    "tipo": "gato",
    "cor": "branco",
    "idade": 3
}
print(animal)

estudante = {}
estudante["nome"] = "Carlos"
estudante["curso"] = "Matemática"
estudante["semestre"] = 2

print(estudante)

livro = {
    "titulo": "A Arte da Guerra",
    "autor": "Sun Tzu",
    "publicado": 1500
}

print(livro)

universidade = {
    "nome": "Universidade Federal",
    "localidade": {
        "cidade": "Rio de Janeiro",
        "bairro": "Centro"
    }
}

print(universidade)
print(universidade["nome"])
print(universidade["localidade"]["cidade"])
