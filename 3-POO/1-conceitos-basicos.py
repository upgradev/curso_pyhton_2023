# 1- classes e objetos

class LivroOld:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano


meu_livro = LivroOld("1984", "George Orwell", 1949)

# 2 - Atributos
print(meu_livro.titulo)
print(meu_livro.autor)
print(meu_livro.ano)

# 3 - métodos


class Livro:
    def __init__(self, titulo, autor, ano) -> None:
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def descricao(self):
        return f"'{self.titulo}' por {self.autor} publica em {self.ano}"


meu_livro = Livro("1984", "George Orwell", 1949)
print(meu_livro.descricao())


