#---------------coisas da aula-----------------------

# for contador in range(11):
#     if contador %2 != 0:
#         print(f"[{contador}] é impar")
#     else:
#         print(f"[{contador}] é par")

# letras = ["p", "r", "o", "f", "e"]

# for i in range(5):
#     print(letras[i])

# letras = ["p", "r", "o", "f", "e"]

# for i in letras:
#     print(i)
#--------------------------------------

#Ex 1

# for i in range(51):
#     print(i)

#Ex 2

# for i in range(1, 101):
#     if i %2 == 0:
#         print(f"{i} é impar")

#Ex 3

# tab = int(input("A tabuada de que número vc quer? "))

# if 1<= tab <= 10:

#     for i in range(1, 11):
#         print(f"{tab} X {i} = {tab * i}")
# else:
#     print("Digite um número válido")

#Ex 4

# soma = 0
# qntde = int(input("Quantas idades você vai digitar? "))

# for i in range(qntde):
#     idade = int(input(f"Digite a idade {i + 1}: "))
#     soma += idade

# media = soma / qntde
# print(f"A média das idades é {media:.2f}")

# Ex 5

# pares = 0
# impares = 0
# for i in range(11):
#     num = int(input("Digite um númer: "))
#     if i %2 != 0:
#         impares += 1
#     else:
#         pares += 1
# print(f"Sao {pares} nums pares")
# print(f"Sao {impares} nums impares")

#Ex 6

# dentro = 0
# fora = 0
# for i in range (11):
#     num = int(input("numero: "))
#     if 10 <=  num <= 20:
#         dentro += 1
#     else:
#         fora += 1
# print("fora: ",fora)
# print("dentro: ", dentro)

#Ex 7 

# soma = 0 
# for i in range (51):
#     num = int(input("nums: "))
#     if num %2 == 0:
#         soma += num 
# print(soma)

# soma = 0

# for i in range(51):
#     numero_par = i * 2
#     soma += numero_par

# print("A soma dos 50 primeiros números pares é:", soma)


#Ex 8

# # Lista vazia para armazenar os 10 números
# valores = []

# # Leitura dos 10 números
# for i in range(10):
#     numero = int(input(f"Digite o {i + 1}º número: "))
#     valores.append(numero)

# # Bubble Sort para ordenar em ordem crescente
# n = len(valores)
# for i in range(n):
#     for j in range(0, n - i - 1):
#         if valores[j] > valores[j + 1]:
#             # Troca os elementos
#             valores[j], valores[j + 1] = valores[j + 1], valores[j]

# # Imprime a lista ordenada
# print("Números em ordem crescente:")
# for numero in valores:
#     print(numero)

#Ex 9
# # Solicita o texto ao usuário
# texto = input("Digite um texto qualquer: ").lower().strip()

# # Lista de vogais normais e acentuadas
# todas_vogais = {
#     'a': 0, 'á': 0,
#     'e': 0, 'é': 0,
#     'i': 0, 'í': 0,
#     'o': 0, 'ó': 0,
#     'u': 0, 'ú': 0
# }

# # Conta as vogais no texto
# for letra in texto:
#     if letra in todas_vogais:
#         todas_vogais[letra] += 1

# # Soma total de vogais (com e sem acento)
# total_vogais = sum(todas_vogais.values())

# # Exibe o resultado
# print(f"\nTotal de vogais (com e sem acento): {total_vogais}")
# print("Quantidade por vogal:")
# for vogal, quantidade in todas_vogais.items():
#     if quantidade > 0:
#         print(f"{vogal.upper()}: {quantidade}")

# #Ex 10

##Sem dicionário
# vetor = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]

# qntde = 0
# maisFrequente = 0
# numResposta = 0

# for num in vetor:
#     for prox in vetor:
#         if prox  == num:
#             qntde += 1
        
#     if qntde > maisFrequente:
#         maisFrequente > qntde
#         numResposta = num

#     qntde = 0
#     print(maisFrequente)

# vetor = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]

# # com dicionário 
# frequencia = {}

# for numero in vetor:
#     if numero in frequencia:
#         frequencia[numero] += 1
#     else:
#         frequencia[numero] = 1

# # Encontra o número com a maior frequência
# mais_frequente = None
# maior_contagem = 0

# for numero, contagem in frequencia.items():
#     if contagem > maior_contagem:
#         mais_frequente = numero
#         maior_contagem = contagem

# # Exibe o resultado
# print(f"O número que mais se repete é: {mais_frequente} (aparece {maior_contagem} vezes)")



#Ex 11
# a. Tamanho dos vetores fornecido pelo usuário
# n = int(input("Tamanho dos vetores: "))

# # b. Leitura dos elementos do vetor A
# print("Digite os elementos do vetor A:")
# vetor_a = []
# for i in range(n):
#     valor = int(input(f"A[{i}]: "))
#     vetor_a.append(valor)

# # Leitura dos elementos do vetor B
# print("Digite os elementos do vetor B:")
# vetor_b = []
# for i in range(n):
#     valor = int(input(f"B[{i}]: "))
#     vetor_b.append(valor)

# # c. Soma dos elementos A[i] + B[i] em C[i]
# vetor_c = []
# for i in range(n):
#     soma = vetor_a[i] + vetor_b[i]
#     vetor_c.append(soma)

# # d. Exibição do vetor C
# print("Vetor C:", vetor_c)
