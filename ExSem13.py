#ex1
# def soma_elementos(lista):
#     return sum(lista)

# print("a soma de tudo é:",soma_elementos([1,2,3,4,5]))

#ex2

# def e_palindromo(texto):
#     texto_normal = texto.lower().replace(" ", "")
#     texto_invertido = texto[::-1]
#     return texto == texto_invertido

# print(e_palindromo("arara"))
# print(e_palindromo("radar"))
# print(e_palindromo("python"))
# print(e_palindromo("ana"))    
# print(e_palindromo("Ame a ema")) 

# #ex3
# def maior_elemento(lista):
#     return max(lista)

# print(maior_elemento([1,2,3,4,5,6,89]))

#ex4
def contar_caracteres(texto, caractere_alvo):
    """
    Conta o número de vezes que um caractere específico aparece em uma string.

    Args:
        texto: A string onde a contagem será feita.
        caractere_alvo: O caractere a ser contado. Espera-se que seja uma string
                    de comprimento 1, mas o método count() funciona mesmo que
                    seja uma substring maior.

    Returns:
        O número de vezes que o caractere_alvo aparece na string texto.
    """

    return texto.count(caractere_alvo)


# Exemplo 1: Contando uma letra
minha_string = "abracadabra"
letra = "a"
ocorrencias = contar_caracteres(minha_string, letra)
print(f"A letra '{letra}' aparece {ocorrencias} vezes em '{minha_string}'.")
# Saída: A letra 'a' aparece 5 vezes em 'abracadabra'.

# Exemplo 2: Contando um caractere que não existe
minha_string_2 = "python é legal"
letra_2 = "z"
ocorrencias_2 = contar_caracteres(minha_string_2, letra_2)
print(f"A letra '{letra_2}' aparece {ocorrencias_2} vezes em '{minha_string_2}'.")
# Saída: A letra 'z' aparece 0 vezes em 'python é legal'.

# Exemplo 3: Contando espaços
frase = "Olá mundo, como você está?"
espaco = " "
ocorrencias_espaco = contar_caracteres(frase, espaco)
print(f"O caractere de espaço aparece {ocorrencias_espaco} vezes em '{frase}'.")
# Saída: O caractere de espaço aparece 4 vezes em 'Olá mundo, como você está?'.

# Exemplo 4: O método count() também funciona para substrings
palavra = "banana"
sub = "na"
ocorrencias_sub = contar_caracteres(palavra, sub)
print(f"A substring '{sub}' aparece {ocorrencias_sub} vezes em '{palavra}'.")
# Saída: A substring 'na' aparece 2 vezes em 'banana'.