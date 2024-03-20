s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

# Uniao
uniao = s1 | s2
print(uniao)

uniao_metodo = s1.union(s2)
print(uniao_metodo)

# intersecção
interseccao = s1 & s2
print(interseccao)
interseccao_metodo = s1.intersection(s2)
print(interseccao)

# Diferença
diferenca = s1 - s2
print(diferenca)
diferenca_metodo = s1.difference(s2)
print(diferenca_metodo)

# diferença simetrica
diferenca_simetrica = s1 ^ s2
print(diferenca_simetrica)

diferenca_simetrica_metodo = s1.symmetric_difference(s2)
print(diferenca_simetrica_metodo)


# subset (subconjunto) verifica se o primeiro conjunto s3 é um subconjunto do segundo s1
s3 = {1, 2}
is_subset = s3.issubset(s1)
print(is_subset)

# superset (superconjunto) verifica se o primeiro conjunto é um superconjunto, se s1 tem todos os elementos de s3 por exemplo
is_superset = s1.issuperset(s3)
print(is_superset)

# exercicio
print("Exercício ###############################")
print()

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

print(f"Conjuntos: s1: {s1} e s2: {s2}")

uniao = s1.union(s2)
print(f"União: {uniao}")

interseccao = s1.intersection(s2)
print(f"Interseccao: {interseccao}")

diferenca = s1.difference(s2)
print(f"Diferença: {diferenca}")

diferenca_simetrica = s1.symmetric_difference(s2)
print(f"Diferença simetrica: {diferenca_simetrica}")

subset = s1.issubset(s2)
print(f"subset: {subset}")
superset = s1.issuperset(s2)
print(f"superset: {superset}")