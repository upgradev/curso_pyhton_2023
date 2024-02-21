# Exemplo 1
lista = [1, 2, 2, 3, 4, 4, 5, 5]
conjunto = set(lista)
print(conjunto)  # não mostra itens duplicados, remove elementos duplicados]

# Exemplo 2
conjunto = {1, 2, "Python", (4, 5)}
print(conjunto)

try:
    conjunto.add([6, 7])
except TypeError as e:
    # saida é erro pois esta tentando adicionar elementos mutaveis, tem que ser imutaveis como numeros, string e tuplas
    print(f"Erro: {e}")


# Criando um conjunto
# usando chaves
s_chaves = {1, 2, 3, 3, 4}
print(s_chaves)

# usando a funcao set
s_funcao = set([1, 2, 3, 3, 4])
print(s_funcao)
print(s_chaves == s_funcao)
print()

# exercicio

frutas_chaves = {"maçã", "banana", "cereja"}
print(frutas_chaves)

frutas_lista = ["uva", "manga", "manga", "uva", "maçã"]
frutas_funcao = set(frutas_lista)
print(frutas_funcao)

interseccao = frutas_chaves.intersection(frutas_funcao)

if interseccao:
    print(f"Frutas em comum: {interseccao}")
else:
    print(f"Os conjuntos não tem fruta em comum")
