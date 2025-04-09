print("Seja bem-vindo!!")
print(" 1. Soma \n 2. Subtração \n 3. Divisão \n 4. Multiplicação \n 5. Sair")

opcao = int(input("Escolha uma opção! "))


if opcao == 5 :
    print("Até a próxima!")

elif opcao >=1 and opcao <= 5: 

    valorA = int(input("Insira o primeiro valor: "))
    valorB = int(input("Insira o segundo valor: "))

else:
    print("opcao invalida")

if opcao == 1:
    resul1 = valorA + valorB
    print(resul1)
elif opcao == 2:
    result2 = valorA - valorB 
    print(result2)
elif opcao == 3:
    result3 = valorA / valorB
    print(result3)
elif opcao == 4:
    result4 = valorA * valorB




# 2. Você está em uma floresta e precisa escolher um caminho para seguir. Existem duas opções: o caminho da esquerda e o caminho da direita.
# Se você escolher o caminho da esquerda, irá encontrar um rio e precisará decidir se quer tentar atravessá-lo ou não. 
# Se escolher o caminho da direita, irá encontrar uma montanha e precisará decidir se quer subi-la ou não. 
# Crie um programa em Python que simule essa situação e apresente o resultado final.



# print("Você está em uma floresta e precisa escolher um caminho! \n O caminho da esquerda tem um rio, e o da direita tem uma montanha")
# caminho = input("Qual caminho você escolhe? Esquerda ou Direita? ").lower().strip()
# if caminho == "esquerda":
#     print("Você encontrou um rio!")
#     atravessar = input("Você decide atravessar o rio? (responda com sim e nao) ").lower().strip()
#     if  atravessar == "sim":
#         print("Você atravessou o rio e encontrou uma clareira na floresta com vários animais legais!")
#     elif atravessar == "nao":
#         print("Você ficou parado(a) na borda do rio e viu vários cardumes de peixinhos!")

# elif caminho == "direita":
#     print("Você encontrou uma montanha nevada!")
#     subir = input("deseja subir? (responda com sim e nao) ").lower().strip()
#     if subir == "sim":
#         input("Você subiu e encontrou uma cabana com um casal idoso, e a senhora do casal te chamou para tomar sopa!")
#     elif subir == "nao":
#         print("Você ficou olhando a montanha e viu um lindo pôr do sol")