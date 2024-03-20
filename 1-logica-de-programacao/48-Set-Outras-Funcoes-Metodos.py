frutas = {"maça", "banana", "laranja", "uva", "manga"}

numero_de_frutas = len(frutas)
print(f"Número de frutas usando len(): {numero_de_frutas}")

fruta_desejada = "maça"
if fruta_desejada in frutas:
    print(f"Veirifcar se tem o item: {fruta_desejada}")
else :
    print(f"Não está no conjunto")
    

frutas_copia = frutas.copy()
print(f"Copia de frutas: {frutas_copia}")
print(frutas is frutas_copia)

print()
print("Exercícios ##################")

animais = {"cachorro", "gato", "pássaro", "peixe", "coelho"}
print(f"Lista de animais: {animais}")

qtde_animais = len(animais)
print(f"Qtde de animais: {qtde_animais}")

def verificar_animal(animal):
    if animal in animais:
        print(f"{animal} está no conjunto")
    else:
        print(f"{animal} não esta no conjunto")

verificar_animal("cachorro")
verificar_animal("macaco")

animais_copia = animais.copy()
print(animais_copia in animais)
animais_copia.add("tartaruga")
print(f"Conjunto original: {animais}")
print(f"Conjunto copia: {animais_copia}")