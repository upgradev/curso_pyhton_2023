# Função Lambda com filter
# Filtramos uma lista apenas para obter numeros pares usando a função filter()
# junto com  uma função lambda


# Dada uma lista de palavras, retorne umanova lista contendo o comprimento de cada palavra
palavras = ["maça", "banana", "arroz", "abacate"]
comprimentos = list(map(lambda palavra: len(palavra), palavras))
print(comprimentos)

# lambda com map
# dado uma lista de numeros, retorne uma nova lista onde cada número é elevado ao quadrado
# numeros = [1, 2, 3, 4, 5]
# numeros_ao_quadrado = list(map(lambda x: x ** 2, numeros))
# print(numeros_ao_quadrado)


# dado uma lista de nomes, filtre-a para obter apenas os nomes que começam com a letra A
# lista original de nomes
# nomes =["Alice", "Bob", "Ana", "Charlie", "Alex", "Tom"]
# nomes_com_A = list(filter(lambda nome: nome[0] == "A", nomes))
# print(nomes_com_A)

# nomes2 =["Alice", "Bob", "Ana", "Charlie", "Alex", "Tom", "Alice"]
# nomes_com_Alice = list(filter(lambda nome: nome == "Alice", nomes2))
# print(nomes_com_Alice)


# problema: Dada uma lista de numeross, filtre-a para obter apenas os numeros pares

# Lista original de numeros
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # usando filter() e lambda para obter numeros pares
# numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
# print(numeros_pares)
