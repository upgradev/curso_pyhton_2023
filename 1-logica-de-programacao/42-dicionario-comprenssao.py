quadrados = {
    x: x ** 2 for x in range(1, 6)
}

print(quadrados)

# usando um loop for tradicional
quadrados = {}
print(quadrados)
for x in range(1, 6):
    quadrados[x] = x**2
print(quadrados)

# converter chaves em valores e valores em chaves
original = {"a": 1, "b": 2, "c": 3}
invertido = {valor: chave for chave, valor in original.items()}
print(f"Original: {original}")
print(f"Invertido: {invertido}")

invertido = {}
for chave, valor in original.items():
    invertido[valor] = chave
print(f"Invertido com for: {invertido}")

# filtrando itens de um dicionario:
precos = {
    "laptop": 1000,
    "mouse": 25,
    "monitor": 200,
    "teclado": 30,
    "cabo hdmi": 10
}

caros = {}
for produto, preco in precos.items():
    if preco > 50:
        caros[produto] = preco

print("com for", caros)

caros = {}
caros = {produto: preco for produto, preco in precos.items() if preco > 50}
print(f"com comprenssao: {caros}")

# dicionario com palavra e seus comprimentos
palavras = {"Python", "Compreensão", "Dicionário"}
comprimentos = {palavra: len(palavra) for palavra in palavras}
print(comprimentos)

# tradicional
palavras = ["Python", "Compreensão", "Dicionário"]
comprimentos = {}
for palavra in palavras:
    comprimentos[palavra] = len(palavra)
print("Com for: ", comprimentos)

# ################# exercício
numeros = [1, 2, 3, 4, 5]
quadrados = {n: n**2 for n in numeros}
print(quadrados)

quadrados = {}
for n in numeros:
    quadrados[n] = n**2
print(quadrados)
