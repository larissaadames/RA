bois = int(input("Quantos bois serão analisados? \n"))

maiorPeso = 0
menorPeso = float("inf")
idgordo = 0
idmagro = 0

for i in range (bois):
    peso = float(input(f"Digite o peso do boi {i+1} em KG: "))
    ide = int(input(f"Digite o ID do boi {i+1}: "))
    if peso > maiorPeso:
        maiorPeso = peso
        idgordo = ide
    if peso < menorPeso:
        menorPeso = peso
        idmagro = ide


print ("\n= RESULTADO FINAL ===")
print (f"Boi mais gordo: ID = {idgordo}, o peso:{maiorPeso}")
print (f"Boi mais magro: ID = {idmagro}, o peso:{menorPeso}")
if menorPeso == maiorPeso:
    print("os pesos sao iguais")

