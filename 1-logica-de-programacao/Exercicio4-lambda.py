# Filtrando e transformando dados com lambda

# 1 - dada uma lista de numeros: numeros = [2,5,8,10,12,15,18,20,23,25,28]
# 2 - Use a função filter e uma função lambda para criar uma nova  lista que contem apenas os números ímpares da lista original
# 3-  em seguida use a função map e uma função lamda para criar uma nova lista
#  que contem o quadrado de cada numero da lista de numeros impares
# 4 -  imprima ambas as listas

numeros = [2, 5, 8, 10, 12, 15, 18, 20, 23, 25, 28]
numeros_impares = list(filter(lambda x: x % 2 != 0, numeros))
print(numeros_impares)
numeros_ao_quadrado = list(map(lambda numero : numero ** 2, numeros_impares))
print(numeros_ao_quadrado)