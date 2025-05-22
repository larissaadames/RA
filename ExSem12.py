## 1. Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os demais elementos. Escreva ao final a matriz obtida.

matriz = [
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0]
]

for linha in range(5):
    for coluna in range(5):
        if linha == coluna:
            matriz[linha][coluna] = 1

for linha in range(5):
    print(matriz[linha])

## 2. Leia uma matriz 4 x 4, imprima a matriz e retorne a localização (linha e a coluna) do maior valor.

# matriz = [
# [0,0,0,0,0],
# [0,0,0,0,0],
# [0,0,0,0,0],
# [0,0,0,0,0]
# ]

# print(matriz)

# whilhe 