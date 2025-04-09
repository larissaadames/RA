# # print("Seja bem-vindo!!")
# # print(" 1. Soma \n 2. Subtração \n 3. Divisão \n 4. Multiplicação \n 5. Sair")

# # opcao = int(input("Escolha uma opção! "))

# # valorA = float(input("Insira o primeiro valor: "))
# # valorB = float(input("Insira o segundo valor: "))

# # if opcao == 1:
# #     resul1 = valorA + valorB
# #     print(resul1)
# # elif opcao == 2:
# #     result2 = valorA - valorB 
# #     print(result2)
# # elif opcao == 3:
# #     result3 = valorA / valorB
# #     print(result3)
# # elif opcao == 4:
# #     result4 = valorA * valorB
# #     print(result4)

# # else:
# #     print("Até a próxima!")
# #     exit();



# 2. Você está em uma floresta e precisa escolher um caminho para seguir. Existem duas opções: o caminho da esquerda e o caminho da direita.
# Se você escolher o caminho da esquerda, irá encontrar um rio e precisará decidir se quer tentar atravessá-lo ou não. 
# Se escolher o caminho da direita, irá encontrar uma montanha e precisará decidir se quer subi-la ou não. 
# Crie um programa em Python que simule essa situação e apresente o resultado final.



# print("Você está em uma floresta e precisa escolher um caminho! \n O caminho da esquerda tem um rio, e o da direita tem uma montanha")
# caminho = input("qual caminho você escolhe? Esquerda ou direita?").lower().strip()
# if caminho == "esquerda":
#     print("vc encontrou um rio")
#     atravessar = input("voce decide atravessar o rio? (responda com sim e nao)").lower().strip()
#     if  atravessar == "sim":
#         print("vc atravessou")
#     elif atravessar == "nao":
#         print("vc nao travessou")

# elif caminho == "direita":
#     subir = input("vc deseja subir?").lower().strip()
#     if subir == "sim":
#         input("vc subiu")
#     elif subir == "nao":
#         print("vc nao subiu")