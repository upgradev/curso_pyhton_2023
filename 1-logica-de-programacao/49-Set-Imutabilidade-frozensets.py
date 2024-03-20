# imutabilidade não pode ter list ou outro set
# valido
conjunto_valido = {1, 2, 3, "string", (10, 20)}
print(f"Conjunto valido: {conjunto_valido}")

# nao é valido
# conjunto_invalido = {1,2.5, "string", [10,20]} # ira causar um erro

# conjunto_invalido_2 = {1,2,{10,20}} # ira causar um erro

# frozenset : se criar um frozenset não pode mais adicionar nem remover elementos dele
fs = frozenset([1, 2, 3, 4])
print(f"frozenset: {fs}")
# fs.add(5) da erro nao existe add nele

conjunto_contendo_frozenset = {frozenset([1, 2, 3]), frozenset([4, 5, 6])}
print(conjunto_contendo_frozenset)

print()
print("Exercício ##########################")
conjunto_a = {1, "Python", (10, 20)}
# conjunto_a.add([3, 4, 5]) erro
# print(conjunto_a)

conjunto_a.add(5)
print(conjunto_a)
conjunto_a.remove(1)
print(conjunto_a)

fs1 = {1, 2, 3}
fs2 = {4, 5, 6}
conjunto_b = {frozenset(fs1), frozenset(fs2)}
print(conjunto_b)