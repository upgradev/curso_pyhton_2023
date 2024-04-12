"""
Exercício: Comparação de Preços e Desconto Adicional para Cinco Produtos

Objetivo: Desenvolver um programa que obtenha do usuário o preço de cinco
produtos e indique qual produto deve ser comprado com base no menor preço. 

Além disso, se o usuário optar por comprar o produto recomendado, o programa oferecerá um desconto.

Instruções:

    1. Solicite ao usuário que informe o preço de cinco produtos.
    2. Determine e exiba qual dos cinco produtos é o mais barato.
    3. Informe ao usuário a diferença de preço entre o produto mais barato e os outros quatro.
    4. Pergunte ao usuário se ele deseja comprar o produto mais barato agora.
        a. Se o usuário responder "sim", ofereça um desconto de 5% sobre o preço 
        do produto mais barato e informe o novo preço.
        
        b. Se o usuário responder "não", exiba uma mensagem: "Lembre-se de sempre 
        buscar o melhor negócio!"
    
    5. Caso o usuário escolha comprar o produto mais barato com o desconto, 
    peça um método de pagamento:
    
    a. Se o método de pagamento for "dinheiro", ofereça um desconto adicional de 2%.
    b. Se for "cartão", informe que o pagamento pode ser dividido em até 3 vezes sem juros.
    
    6.Exiba um resumo da compra, incluindo produto escolhido, preço original, desconto 
    aplicado e preço final.

Observações: O programa deve considerar que o usuário fornecerá apenas valores numéricos 
válidos para os preços. As respostas do usuário para perguntas como a intenção de compra 
podem ser "sim" ou "não", e o programa deve ser insensível a maiúsculas e minúsculas (ou 
seja, "Sim", "sim" e "SIM" são consideradas a mesma resposta).
"""

preco_cinco_produtos = []

for i in range(0, 5):
    produto = float(input(f"Informe o preco do {i+1}° produto: "))
    preco_cinco_produtos.append(produto)

produto_mais_barato = min(preco_cinco_produtos)
print(f"O produto mais barato é o {produto_mais_barato}")

for i, preco in enumerate(preco_cinco_produtos, 1):
    diferenca = preco - produto_mais_barato
    print(
        f"A diferença do produto {i} e a diferença do mais barato é {diferenca:.2f}")

comprar = input("Deseja comprar o produto mais barato? (sim/nao)")


if comprar.lower() == 'sim':
    valor_desconto = produto_mais_barato * 0.05
    preco_com_desconto = produto_mais_barato - valor_desconto

    metodo_pagamento = input("Qual metodo de pagamento? (dinheiro/cartao)")

    if metodo_pagamento.lower() == "dinheiro":
        desconto_adicional = preco_com_desconto * 0.02
        preco_final = preco_com_desconto - desconto_adicional

    if metodo_pagamento.lower() == "cartao":
        print("o pagamento pode ser dividido em até 3 vezes sem juros")
        preco_final = preco_com_desconto
    
    print(f"\nResumo da Compra:")
    print(f"Produto escolhido: Produto mais barato")
    print(f"Preço original: R$ {produto_mais_barato:.2f}")
    print(f"Desconto aplicado: R$ {preco_com_desconto + desconto_adicional:.2f}")
    print(f"Preço final: R$ {preco_final:.2f}")
    
else:
    print("Lembre-se de sempre buscar o melhor negócio!")
