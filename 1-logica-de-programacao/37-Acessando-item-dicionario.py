# ACESSANDO ITENS NO DICIONÁRIO
# Acessando valores usando chaves

smartphone = {
    "marca": "Apple",
    "modelo": "Iphone 12",
    "cor": "Azul",
    "capacidade": "128GB",
    "sistema": "IOS"
}

print("Método direto")
print(f"Marca: {smartphone['marca']}")

# Método get()
print("\nUsando método get():")
print(f"Modelo: {smartphone.get('modelo')}")
print(f"Camera: {smartphone.get('camera', 'Informação não disponível')}")

# Verificando a existẽncia de uma chave
print("\nVerificando a existência de uma chave")

if "sistema" in smartphone:
    print(f"O Smartphone roda no sistema {smartphone['sistema']}")
else:
    print(f"Sistema operacional não especificado")

if "camera" in smartphone:
    print(f"Camera {smartphone['camera']}")
else:
    print(f"Informações da camera não disponível")


# EXERCICIO
artista = {
    "nome": "Ludwing van Beethoven",
    "nascimento": 1770,
    "falecimento": 1827,
    "nacionalidade": "Alemã",
    "estilo": "Clássico"
}
print("\nExercício")
print(f"Nome do artista: {artista['nome']}")
# print(f"Nome do artista: {artista['profissao']}") da erro pois nao existe a chave

print(f"Nacionalidade: {artista.get('nacionalidade')}")
print(f"Profissão: {artista.get('profissao', 'Informação da profissão não disponível')}")