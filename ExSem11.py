# import random

# numJogador1 = []
# numJogador2 = []

# for i in range(3):
#     numJogador1.append(random.randint(1,6))
#     numJogador2.append(random.randint(1,6))

#     SomaP1 = sum(numJogador1)
#     SomaP2 = sum(numJogador2)

# print(f"a os dados do P1 é {numJogador1} e a soma é {SomaP1}")
# print(f"a os dados do P1 é {numJogador2} e a soma é {SomaP2}")

# if SomaP1 > SomaP2:
#     print("P1 Wins!")
# elif SomaP2 > SomaP1:
#     print("P2 Wins!")
# else:
#     print("empate")


# lista = []
# for i in range(5):
#     lista.append(int(input("APENAS NUMEROS POSITIVOS: ")))
#     ordenadaLista = sorted(lista)
#     Rlista =list(reversed(lista))

# print(ordenadaLista)
# print(Rlista)

# Ex1

# import random 
# numRandom = []
# for i in range(5):
#     numRandom.append(random.randint(1, 100))
# print(numRandom)

#Ex 2

# nums = []
# for i in range(3):
#     nums.append(int(input("NUMS ")))
# print(nums)

# #Ex 3

# frase = (input("frase!!!!!!!!!!!!!!!!!! "))
# print(frase.split())

#Ex 4

# import random
# lista = []
# for i in range(1,10):   
#     lista.append(random.randint(1,10))
#     reversa = list(reversed(lista))
# print(lista)
# print(reversa)

#Ex 5
comidas = ["banana", "goiaba", "pastel", "caldo", "bannananananananananana"]
maiorPalavra = ""
menorPalavra = ""
maior = len(comidas[0])
menor = len(comidas[0])

for palavra in comidas:
    if len(palavra) > maior:
        maior = len(palavra)
        maiorPalavra = palavra
    elif len(palavra) < menor:
        menor = len(palavra)
        menorPalavra = palavra
print(maiorPalavra)
print(menorPalavra)