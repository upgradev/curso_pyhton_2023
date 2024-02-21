livros = {
    "978-1234567890": {
        "titulo": "A Arte da Guerra",
        "autor": "Sun Tzu",
        "anoo_publicacao": 500
    },
    "978-0987654321": {
        "titulo": "1984",
        "autor": "George Orwell",
        "anoo_publicacao": 1949
    }
}

print(livros)

# cuidados com tipos de chaves mutaveis
ruim = {}
lista_chave = [1, 2, 3]
# ruim[lista_chave] isso vai dar um erro

# bom
bom = {}
tupla_chave = (1, 2, 3)
bom[tupla_chave] = "valor"
print(bom)

# dicionario vc listas - quando utilizar cada um
filmes_favoritos = ["Pulp Fiction", "Cidade de Deus", "O poderoso chefão"]
primeiro_filme = filmes_favoritos[0]
print(primeiro_filme)

contatos = {
    "Alice": "555-1234",
    "Bob": "555-5678"
}

telefone_alice = contatos["Alice"]
print(telefone_alice)

