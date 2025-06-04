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

# ## 2. Leia uma matriz 4 x 4, imprima a matriz e retorne a localização (linha e a coluna) do maior valor.

# matriz = []
# print("Digite os elementos da matriz 4x4:")

# for i in range(4):
#     linha_atual = []
#     for j in range(4):
#         while True:
#             try:
#                 elemento = int(input(f"Elemento da linha {i + 1}, coluna {j + 1}: "))
#                 linha_atual.append(elemento)
#                 break
#             except ValueError:
#                 print("Entrada inválida. Por favor, digite um número inteiro.")
#     matriz.append(linha_atual)

# print("\nMatriz digitada:")
# for linha_para_imprimir in matriz:
#     for elemento_para_imprimir in linha_para_imprimir:
#         print(f"{elemento_para_imprimir:5}", end=" ")
#     print()

# maior_valor = matriz[0][0]
# posicao_linha_maior = 0
# posicao_coluna_maior = 0

# for i in range(4):
#     for j in range(4):
#         if matriz[i][j] > maior_valor:
#             maior_valor = matriz[i][j]
#             posicao_linha_maior = i
#             posicao_coluna_maior = j

# print(f"\nO maior valor na matriz é: {maior_valor}")
# print(f"Ele está localizado na linha {posicao_linha_maior + 1} e coluna {posicao_coluna_maior + 1}.")
# print(f"(Isso corresponde aos índices da lista: linha {posicao_linha_maior}, coluna {posicao_coluna_maior})")

# #ex3

# NUM_ALUNOS = 5

# matriz_alunos = []

# print("--- Entrada de Dados dos Alunos ---")

# for i in range(NUM_ALUNOS):
#     print(f"\n--- Aluno {i + 1} de {NUM_ALUNOS} ---")
#     info_aluno_atual = []

#     while True:
#         try:
#             matricula = int(input(f"Digite o número de matrícula do aluno {i + 1}: "))
#             info_aluno_atual.append(matricula)
#             break
#         except ValueError:
#             print("Entrada inválida. A matrícula deve ser um número inteiro.")

#     while True:
#         try:
#             media_provas = int(input(f"Digite a média das provas do aluno {i + 1}: "))
#             info_aluno_atual.append(media_provas)
#             break
#         except ValueError:
#             print("Entrada inválida. A média das provas deve ser um número inteiro.")

#     while True:
#         try:
#             media_trabalhos = int(input(f"Digite a média dos trabalhos do aluno {i + 1}: "))
#             info_aluno_atual.append(media_trabalhos)
#             break
#         except ValueError:
#             print("Entrada inválida. A média dos trabalhos deve ser um número inteiro.")
    
#     matriz_alunos.append(info_aluno_atual)

# for aluno_info in matriz_alunos:
#     nota_final_calculada = aluno_info[1] + aluno_info[2]
#     aluno_info.append(nota_final_calculada)

# maior_nota_final_encontrada = -1
# matricula_aluno_maior_nota = -1

# if matriz_alunos:
#     maior_nota_final_encontrada = matriz_alunos[0][3]
#     matricula_aluno_maior_nota = matriz_alunos[0][0]

#     for aluno_info in matriz_alunos:
#         nota_final_atual = aluno_info[3]
#         if nota_final_atual > maior_nota_final_encontrada:
#             maior_nota_final_encontrada = nota_final_atual
#             matricula_aluno_maior_nota = aluno_info[0]

# print("\n--- Resultado ---")
# if matricula_aluno_maior_nota != -1:
#     print(f"A matrícula do aluno com a maior nota final ({maior_nota_final_encontrada}) é: {matricula_aluno_maior_nota}")
# else:
#     print("Não foi possível determinar o aluno com a maior nota (lista de alunos vazia ou erro).")