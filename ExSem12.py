## 1. Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os demais elementos. Escreva ao final a matriz obtida.

# matriz = [
# [0,0,0,0,0],
# [0,0,0,0,0],
# [0,0,0,0,0],
# [0,0,0,0,0],
# [0,0,0,0,0]
# ]

# for linha in range(5):
#     for coluna in range(5):
#         if linha == coluna:
#             matriz[linha][coluna] = 1

# for linha in range(5):
#     print(matriz[linha])

## 2. Leia uma matriz 4 x 4, imprima a matriz e retorne a localização (linha e a coluna) do maior valor.

# 1. Ler a matriz 4x4
matriz = []
print("Digite os elementos da matriz 4x4:")

for i in range(4):  # 4 linhas
    linha_atual = []
    for j in range(4):  # 4 colunas
        while True:
            try:
                elemento = int(input(f"Elemento da linha {i + 1}, coluna {j + 1}: "))
                linha_atual.append(elemento)
                break  # Sai do loop 'while' se a entrada for válida
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro.")
    matriz.append(linha_atual)

# 2. Imprimir a matriz
print("\nMatriz digitada:")
for linha_para_imprimir in matriz:
    for elemento_para_imprimir in linha_para_imprimir:
        print(f"{elemento_para_imprimir:5}", end=" ") # {:5} para alinhar um pouco
    print()  # Pula para a próxima linha

# 3. Encontrar o maior valor e sua localização
maior_valor = matriz[0][0]  # Assume o primeiro elemento como o maior inicialmente
posicao_linha_maior = 0
posicao_coluna_maior = 0

for i in range(4):
    for j in range(4):
        if matriz[i][j] > maior_valor:
            maior_valor = matriz[i][j]
            posicao_linha_maior = i
            posicao_coluna_maior = j

# 4. Exibir o maior valor e sua localização
print(f"\nO maior valor na matriz é: {maior_valor}")
print(f"Ele está localizado na linha {posicao_linha_maior + 1} e coluna {posicao_coluna_maior + 1}.")
print(f"(Isso corresponde aos índices da lista: linha {posicao_linha_maior}, coluna {posicao_coluna_maior})")