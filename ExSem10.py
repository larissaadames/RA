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
dentro = 0
fora = 0
for i in range (11):
    num = int(input("ASKMDKMDFLKM"))
    if 10 >=  num <= 20:
        dentro =+ 1
    else:
        fora =+ 1
print("fora: ",fora)
print("dentro: ", dentro)