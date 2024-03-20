# Criando elemento inicial
s = {1, 2, 3, 4}
print(s)

# Usando Add
s.add(5)
print(s)
s.add(3)
print(s)

# remove
# s.remove(50) erro pois nao existe o elemento e mostra o erro
s.remove(5)
print(s)

try:
    s.remove(50)
except KeyError as e:
    print(f"Erro: {e}")

# discard
s.discard(4) #remove o elemento e se o elemento nao existir nao gera o erro
print(s)
s.discard(4)
print(s)

# pop
elemento_removido = s.pop() # ele remove qq elemento, por que os sets estão desordenados
print(f"Elemento removido: {elemento_removido}")
print(s)

# clear
s.clear() #limpa o conjunto do set
print(s)


################# exercicio
animais = {"gato", "cachorro", "pássaro"}
print(animais)

animais.add("peixe")
print(animais)

animais.remove("pássaro")
print(animais)

animais.discard("lagarto")
print(animais)

elemento_rem = animais.pop()
print(f"Animal removido: {elemento_rem}")
print(animais)

animais.clear()
print(animais)