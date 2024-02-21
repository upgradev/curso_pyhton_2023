usuario = {
    "nome": 'João',
    "idade": 25,
    "email": "joao@email.com"
}


def exibir_perfil(perfil):
    for chave, valor in perfil.items():
        print(f"{chave.title()}: {valor}")


exibir_perfil(usuario)

# retornando dicionários de funcoes


def criar_perfil(nome, idade, email):
    return {
        "nome": nome,
        "idade": idade,
        "email": email
    }


novo_usuario = criar_perfil("Ana", 30, "ana@teste.com")
print("\nNovo Perfil")
exibir_perfil(novo_usuario)

print()
# ###################### exercício
def registrar_livro(titulo, autor, ano):
    return {
        "titulo": titulo,
        "autor": autor,
        "ano": ano
    }

livro = registrar_livro("1984", "George Orwell", 1949)
print(livro)

def exibir_livro(livro_dicionario):
    print(f"Título: {livro_dicionario['titulo']}") 
    print(f"Autor: {livro_dicionario['autor']}") 
    print(f"Ano: {livro_dicionario['ano']}") 

exibir_livro(livro)