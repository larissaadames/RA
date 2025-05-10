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
tab = int(input("A tabuada de que número vc quer? "))

if 1<= tab <= 10:

    for i in range(1, 11):
        print(f"{tab} X {i} = {tab * i}")
else:
    print("Digite um número válido")