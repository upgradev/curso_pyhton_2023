############################ EXERCICIO FABRICA DE OPERACÕES
def fabrica_de_funcoes(operacao):
    def soma(*args):
        return sum(args)
    
    def subtracao(*args):
        resultado = args[0]
        for num in args[1:]:
            resultado = resultado - num
        return resultado

    def multiplicacao(*args):
        resultado = 1
        for num in args:
            resultado *= num
        return resultado    

    def divisao(*args):
        resultado = args[0]
        for num in args[1:]:
            if num == 0:
                raise ValueError("Divisão por zero não é permitida")
            resultado/= num
        return resultado
    if operacao == "soma":
        return soma
    elif operacao == "multiplicacao":
        return multiplicacao
    elif operacao == "subtracao":
        return subtracao
    elif operacao == "divisao":
        return divisao
    else:
        def operacao_nao_suportada(*args):
            return "Operacao Não Suportada"
        return operacao_nao_suportada

adicionar = fabrica_de_funcoes("soma")
print(adicionar(5,3,2))
adicionar = fabrica_de_funcoes("subtracao")
print(adicionar(5,3,2))
adicionar = fabrica_de_funcoes("multiplicacao")
print(adicionar(5,3,2))
adicionar = fabrica_de_funcoes("divisao")
print(adicionar(10,2,5))
adicionar = fabrica_de_funcoes("sda")
print(adicionar(0,3,2))

# ##################### FUNÇÕES COM OBJETOS DE PRIMEIRA CLASSE
# Isso significa que elas podem ser tratadas como qualquer outro objeto, como strings, listas ou ate mesmo classes
# def saudacao():
#     return "Olá Mundo!"

# cumprimentar = saudacao
# print(cumprimentar())

# # Passando funções como argumentos
# def saudacao_nome(nome):
#     return f"Olá, {nome}"
# def cumprimentar(funcao, nome):
#     return funcao(nome)

# print(cumprimentar(saudacao_nome, "Alice"))

# # retornando funções de outras funções
# def nivel_saudacao(nivel):
#     def saudacao_basica():
#         return "Oi!"
#     def saudacao_avancada():
#         return "Olá, como você esta?"
    
#     if nivel == "basico":
#         return saudacao_basica
#     else:
#         return saudacao_avancada
    
# cumprimento = nivel_saudacao("basico")
# print(cumprimento())

################## NON LOCAL usada para trabalhar com variaveis em um escopo mais próximo, 
# mas não global, como funções alinhadas
# print("\n--------------------------\n")
# def funcao_externa():
#     variavel_externa = "Eu sou externa"
#     print(variavel_externa)
#     def funcao_interna():
#         nonlocal variavel_externa
#         variavel_externa = "Eu fui modificada pela função interna"
#         print(variavel_externa)
#     funcao_interna()
#     print(variavel_externa)
    
# funcao_externa()

################ alterar a variavel global
# contador = 0
# def incrementar_contador():
#     global contador
#     contador += 1
#     print(contador)

# incrementar_contador()
# incrementar_contador()
# incrementar_contador()

################ ESCOPO DE VARIAVEIS (LOCAIS X GLOBAIS)
# variavel_global = "Eu sou uma variavel global."

# def funcao_exemplo():
#     #global variavel_global # para alterar o valor a variavel global passar o global
#     variavel_local = "Eu sou uma variável local."
#     print(variavel_local)
#     print(variavel_global)
#     #variavel_global = "Oi"
#     print(variavel_global)

# funcao_exemplo()
# print(f"variavel_global fora da função: {variavel_global}")



################Kwargs
# def exibir_informacoes(**kwargs):
#     # Função que exibe informações pessoais
#     for chave, valor in kwargs.items():
#         print(f"{chave} : {str(valor)}" )


# exibir_informacoes(nome="João", idade=25, cidade="Campo Grande", sexo="Masculino")

#####################