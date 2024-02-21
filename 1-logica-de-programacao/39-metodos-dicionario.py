livro = {
    "titulo": "O Pequeno Principe",
    "autor": "Antoine de Saint-Exupéry",
    "ano": 1943,
    "editora": "Reynal & Hitchcock",
    "preco": 20.50
}

# Keys values e itens
print(f"Chaves do dicionário: {list(livro.keys())}")
print(f"Valores do dicionário: {list(livro.values())}")
print(f"Itens do dicionário: {list(livro.items())}")

# Clear()
print("\nClear()")
copia_livro = livro.copy()
copia_livro.clear()
print(f"Dicionário após o clear: {list(copia_livro.items())}")

# setdefault()
print("\nsetdefault()")
isbn = livro.setdefault("ISBN", "978-3-16-148410-0")
print(f"Isbn: {isbn}")
print(f"Dicionário após o setdefault(): {livro}")

# update()
print("\nUpdate")
atualizacoes = {
    "preco": 18.50,
    "formato": "Capa Dura"
}

livro.update(atualizacoes)
print(f"Dicionário após o update: {livro}")

print("\nfromkeys()")

chaves = ["Titulo", "Autor", "Sinopse"]
novo_livro = dict.fromkeys(chaves, "Desconhecido")
print(f"Dicionario criado com fromkeys(): {novo_livro}")

# Exercício
filme = {
    "titulo": "Inception",
    "diretor": "Christopher Nolan",
    "ano": 2010,
    "genero": "Ficção Científica"
}

print(f"Chaves do filme: {list(filme.keys())}")
print(f"Valores do filme: {list(filme.values())}")
print(f"Itens do filme lista de tuplas: {list(filme.items())}")

copia_filme = filme.copy()
copia_filme.clear()
print(f"Cópia do filme depois do clear: {copia_filme}")

elenco = filme.setdefault("elenco", ["Leonado DiCaprio", "Ellen Page"])
print(f"Elenco: {elenco}")
print(f"Dicionario de filme apos setdefault(): {filme}")

informacoes_adicionais = {
    "duracao": 148,
    "idioma": "Inglês"
}

filme.update(informacoes_adicionais)
print(f"Filme com informações adicionais update(): {filme}")

chaves = ["nome", "idade", "ocupacao"]
perfil = dict.fromkeys(chaves, "Desconhecido")
print(f"Dicionario criado com fromkeys(): {perfil}")