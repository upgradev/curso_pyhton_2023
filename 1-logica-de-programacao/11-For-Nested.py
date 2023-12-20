
##################### fatorial
numero = int(input("Digite um número inteiro não negativo: "))
if numero < 0:
    print("O número deve ser não negativo")
else:
    fatorial = 1
    for multiplicador in range(1, numero + 1):
        fatorial *= multiplicador
        print(f"{multiplicador}! = ", end=" ")
        
        for i in range(1, multiplicador + 1):
            print(i, end=" ")
            if i != multiplicador:
                print(" * ", end="")
        print("=", fatorial)
    
    # for i in range(1, numero + 1):
    #     fatorial *= i
    # print(f"O fatorial de {numero} é {fatorial}") 

# texto = "Hello World!"
# consoantes = [char for char in texto if char.lower() not in 'aeiou']
# print(consoantes)

# quadrado_impares = [x**2 for x in range(10) if x % 2 != 0]
# print(quadrado_impares)

# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f"{i} * {j} = {i * j}")