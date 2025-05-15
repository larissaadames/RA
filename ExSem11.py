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


lista = []
for i in range(5):
    lista.append(int(input("APENAS NUMEROS POSITIVOS: ")))
    ordenadaLista = sorted(lista)
    Rlista =list(reversed(lista))

print(ordenadaLista)
print(Rlista)


