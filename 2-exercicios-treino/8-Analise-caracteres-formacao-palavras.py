"""
Exercício: Análise de Caracteres e Formação de Palavras

Objetivo: Desenvolver um programa que obtenha do usuário uma letra ou uma palavra 
e realize análises sobre o tipo de caractere inserido, além de funções adicionais 
se uma palavra completa for fornecida.

Instruções:

    1. Solicite ao usuário que digite uma letra ou uma palavra.
    
    2. Se o usuário digitar apenas um caractere:
    
        a. Verifique se é uma vogal ou consoante.
        b. Se for uma vogal, exiba: "Você digitou uma vogal."
        c. Se for uma consoante, exiba: "Você digitou uma consoante."
        d. Se o caractere não for uma letra, exiba: "Caractere inválido."
    
    3. Se o usuário digitar mais de um caractere (uma palavra):
        
        a. Calcule e exiba o número de vogais na palavra.
        b. Calcule e exiba o número de consoantes na palavra.
        c. Exiba a palavra em ordem inversa.
        d. Informe se a palavra é um palíndromo (se lê da mesma forma de frente para trás 
        e de trás 
        para frente, como "arara").
    
    4. Peça ao usuário se deseja verificar outra letra ou palavra ou sair do programa.

Observações: O programa deve considerar letras maiúsculas e 
minúsculas (ou seja, "A" e "a" são ambas vogais).
"""

vogais = ['a', 'e', 'i', 'o', 'u']

while True:

    letra_palavra = input("Digite uma letra ou uma palavra: ")

    ordem_inversa = ""

    if (len(letra_palavra) == 1):
        if letra_palavra.lower() in vogais:
            print("Você digitou uma vogal.")
        elif (letra_palavra.lower().isalpha()):
            print("Você digitou uma consoante.")
        else:
            print("Caractere inválido.")

    else:
        numero_vogais = 0
        numero_consoantes = 0
        
        for char in letra_palavra:
            
            if char in vogais:
                numero_vogais+=1
        print(f"o número de vogais na palavra é {numero_vogais}")

        for char in letra_palavra:
            if char.lower().isalpha() and char not in vogais:
                numero_consoantes+=1
        
        print(f"o número de consoantes na palavra é {numero_consoantes}")
        
        ordem_inversa = letra_palavra.lower()[::-1]
        print(f"A palavra {letra_palavra} em ordem inversa {ordem_inversa}")
    
        print("É palindromo") if ordem_inversa == letra_palavra else print("Não é palindromo")
        
    

    continuar = input("Deseja continuar digitando mais palavras (sim/nao)? ")
    
    if continuar.lower() == "nao":
        print("Obrigado por digitar as palavras!")
        break;