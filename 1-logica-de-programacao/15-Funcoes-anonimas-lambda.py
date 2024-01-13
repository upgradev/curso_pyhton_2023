######## funções anonimas (lambda)
################## são funções de pequana extensão. Ao contrário de uma função definida com 
# def, a função pode ter apenas uma exmpressão e retorna implicitamente o resultado dessa expressão. Ela é 
# frequentemente usada para pequenas operações que são convenientes de se definir sem nomear uma função completa



#################### restrição de escopo
# Modificar uma variavel global usando global em uma função lambda, mas não podemos
#  Função regugal modificando uma variavel global
contador = 0

def aumentar_contador():
    global contador
    contador += 1

aumentar_contador()
print(contador)
aumentar_contador()
print(contador)

# aumentar_contador = lambda: global contador; contador +=1 #descomentar da erro

aumentar_contador()
print(contador)




##########Nomeação
# função lambda com sorted

# pessoas = [("João", 35), ("Maria", 25), ("Pedro", 1)]
# pessoas_ordenadas = sorted(pessoas, key=lambda x: x [1]) # ordenando pela idade que esta na posicao 1
# print(pessoas_ordenadas)
# pessoas_ordenadas = sorted(pessoas, key=lambda x: x [0]) # ordenando pela nome que esta na posicao 0
# print(pessoas_ordenadas)


# Exemplo pratico 2 - Limitações
# função regular para classificar numero
# def classificar_numero(n):
#     if n < 0:
#         return "Negativo"
#     elif n == 0:
#         return "Zero"
#     else:
#         return "Positivo"

# print(classificar_numero(3)) 

# # tentativa função lambda para classificar numero (menos clara)

# classificar_numero_lambda = lambda n : "Negativo" if n < 0 else ("Zero" if n == 0 else "Positivo")

# print(classificar_numero_lambda(-1)) 


# Exemplo prático 1 - Definição e uso
# Função regular para dobrar um número
# def dobrar(n):
#     return n * 2
# print("Função regular: ", dobrar(5))

# # Função lambda para dobrar numero
# dobrar_com_lambda = lambda n : n * 2
# print("Função lambda: ",dobrar_com_lambda(5))
