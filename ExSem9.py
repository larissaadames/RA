# megaSena = ["1","2","3","4","5"]
# aposta = input("Quais números que vc quer apostar? ")
# if megaSena == aposta:
#     print("VC GANHOU!!")
# else:
#     print("nao foi dessa vez amigo :/")

# #1.
# a = [1, 0, 5, -2, -5, 7]
# soma = a[0] + a[1] + a[5] 
# print ("essa é a soma: ", soma )
# a[4] = 100
# print(a[0])
# print(a[2])
# print(a[3])
# print(a[4])
# print(a[5])

#2.
# num1 = int(input("num: "))
# num2 = int(input("num: "))
# num3 = int(input("num: "))
# num4 = int(input("num: "))
# num5 = int(input("num: "))
# num6 = int(input("num: "))
# print(num1, num2, num3, num4, num5, num6)

#3.
# num1 = int(input("num: "))
# num2 = int(input("num: "))
# num3 = int(input("num: "))
# num4 = int(input("num: "))
# num5 = int(input("num: "))
# num6 = int(input("num: "))
# num7 = int(input("num: "))
# num8 = int(input("num: "))
# num9 = int(input("num: "))
# num10 = int(input("num: "))

# numeros = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]
# print (numeros)

# val1 = num1 ** 2
# val2 = num2 ** 2
# val3 = num3 ** 2
# val4 = num4 ** 2
# val5 = num5 ** 2
# val6 = num1 ** 2
# val7 = num2 ** 2
# val8 = num3 ** 2
# val9 = num4 ** 2
# val10 = num5 ** 2

# valores = [val1, val2, val3, val4, val5, val6, val7, val8, val9, val10]
# print(valores)

#4.
# num1 = int(input("num: "))
# num2 = int(input("num: "))
# num3 = int(input("num: "))
# num4 = int(input("num: "))
# num5 = int(input("num: "))
# num6 = int(input("num: "))
# num7 = int(input("num: "))
# num8 = int(input("num: "))
# numeros = [num1, num2, num3, num4, num5, num6, num7, num8]
# print(numeros)
# val1 = int(input("valor 1: "))
# val2 = int(input("valor 2: "))
# numeros[2] = val1
# numeros[5] = val2
# print(numeros)

# #5.
# nums = [0,1,2,3,4,5,6,7,8,9]
# pares = 0 
# i = 0
# while i <= 9:
#     nums[i] = int(input("num? "))
#     if nums[i] % 2 == 0:
#         pares += 1
#     i += 1
# print(pares)

#6.
# num = 0
# i = 0
# vetor = [0]*10

# while i < 10: 
#     num = int(input(f"Digite o {i+1}º:"))
#     vetor[i] = num
#     i += 1

# maior = vetor[0]
# menor = vetor[0]
# i = 1

# while i < 10:
#     if vetor[i] > maior:
#         maior = vetor[i]
#     if vetor[i] < menor:
#         menor = vetor[i]
#     i += 1
# print(f"maior: {maior}")
# print(f"menor: {menor}"):

#7
# num = 0
# i = 0
# vetor = [0]*10

# while i < 10: 
#     num = int(input(f"Digite o {i+1}º:"))
#     vetor[i] = num
#     i += 1

# maior = vetor[0]
# posicao = 0
# i = 1

# while i < 10:
#     if vetor[i] > maior:
#         maior = vetor[i]
#         posicao = i
#     i += 1
# print("vetor", vetor)
# print(f"maior: {maior}")
# print(f"posicao: {posicao}")

# #8
# notas = [0] * 15
# i = 0

# while i < 15:
#     nota = int(input(f"Digite a nota do {i + 1}º aluno: "))
#     notas[i] = nota
#     i += 1

# soma = 0
# i = 0
# while i < 15:
#     soma += notas[i]
#     i += 1

# media = soma / 15


# print("\nNotas dos alunos:", notas)
# print(f"Média geral da turma: {media:.2f}")
#.2f para formatar

#9
# vetor = [0] * 10
# i = 0

# while i < 10:
#     numero = int(input(f"Digite o {i + 1}º número: "))
#     vetor[i] = numero
#     i += 1


# nega = 0
# posi = 0


# i = 0
# while i < 10:
#     if vetor[i] < 0:
#         nega += 1
#     elif vetor[i] > 0:
#         posi += vetor[i]
#     i += 1

# print("vetor :", vetor)
# print(f"números negativos: {nega}")
# print(f"Soma números positivos: {posi:.2f}")

#10
# valores = [0] * 5
# i = 0

# while i < 5:
#     numero = int(input(f"Digite o {i + 1}º valor: "))
#     valores[i] = numero
#     i += 1

# maior = valores[0]
# menor = valores[0]
# soma = valores[0]

# i = 1
# while i < 5:
#     if valores[i] > maior:
#         maior = valores[i]
#     if valores[i] < menor:
#         menor = valores[i]
#     soma += valores[i]
#     i += 1

# media = soma / 5

# print("\nValores lidos:", valores)
# print(f"Maior valor: {maior}")
# print(f"Menor valor: {menor}")
# print(f"Média dos valores: {media:.2f}")

#11

valores = [0] * 5
i = 0

while i < 5:
    numero = int(input(f"Digite o {i + 1}º valor: "))
    valores[i] = numero
    i += 1

maior = valores[0]
posMaior= 0

menor = valores[0]
posMenor = 0
i = 1


while i < 5:
    if valores[i] > maior:
        maior = valores[i]
        posMaior = i
    if valores[i] < menor:
        menor = valores[i]
        posMenor = i
    i += 1

# Mostra os resultados
print("\nValores digitados:", valores)
print(f"Maior valor: {maior} na posição {posMaior}")
print(f"Menor valor: {menor} na posição {posMenor}")
