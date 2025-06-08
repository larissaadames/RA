#ex1
# def soma_elementos(lista):
#     return sum(lista)

# print("a soma de tudo é:",soma_elementos([1,2,3,4,5]))

#ex2

# def e_palindromo(texto):
#     texto_normal = texto.lower().replace(" ", "")
#     texto_invertido = texto[::-1]
#     return texto == texto_invertido

# print(e_palindromo("arara"))
# print(e_palindromo("radar"))
# print(e_palindromo("python"))
# print(e_palindromo("ana"))    
# print(e_palindromo("Ame a ema")) 

# #ex3
# def maior_elemento(lista):
#     return max(lista)

# print(maior_elemento([1,2,3,4,5,6,89]))

# # #ex4
# def contar_caracteres(texto, caractere_alvo):
#     return texto.count(caractere_alvo)

# minha_string = "abracadabra"
# letra = "a"
# ocorrencias = contar_caracteres(minha_string, letra)
# print(f"A letra '{letra}' aparece {ocorrencias} vezes em '{minha_string}'.")

# minha_string_2 = "python é legal"
# letra_2 = "z"
# ocorrencias_2 = contar_caracteres(minha_string_2, letra_2)
# print(f"A letra '{letra_2}' aparece {ocorrencias_2} vezes em '{minha_string_2}'.")

# frase = "Olá mundo, como você está?"
# espaco = " "
# ocorrencias_espaco = contar_caracteres(frase, espaco)
# print(f"O caractere de espaço aparece {ocorrencias_espaco} vezes em '{frase}'.")

# palavra = "banana"
# sub = "na"
# ocorrencias_sub = contar_caracteres(palavra, sub)
# print(f"A substring '{sub}' aparece {ocorrencias_sub} vezes em '{palavra}'.")


# #calculadora
# def soma(a, b):
#   return a + b

# def subtracao(a, b):
#   return a - b

# def multiplicacao(a, b):
#   return a * b

# def divisao(a, b):
#   if b == 0:
#     return "Erro: Divisão por zero não é permitida."
#   return a / b

# def exibir_menu():
#   print("\n--- Calculadora Simples ---")
#   print("Escolha uma operação:")
#   print("1. Soma")
#   print("2. Subtração")
#   print("3. Multiplicação")
#   print("4. Divisão")
#   print("5. Sair")
#   print("---------------------------")

# def calculadora():
#   while True:
#     exibir_menu()
#     escolha = input("Digite o número da sua opção: ")

#     if escolha == '5':
#       print("Saindo da calculadora. Até logo!")
#       break
#     elif escolha in ('1', '2', '3', '4'):
#       try:
#         num1 = float(input("Digite o primeiro valor: "))
#         num2 = float(input("Digite o segundo valor: "))
#       except ValueError:
#         print("Entrada inválida. Por favor, digite números válidos.")
#         continue

#       if escolha == '1':
#         print(f"\nResultado: {num1} + {num2} = {soma(num1, num2)}")
#       elif escolha == '2':
#         print(f"\nResultado: {num1} - {num2} = {subtracao(num1, num2)}")
#       elif escolha == '3':
#         print(f"\nResultado: {num1} * {num2} = {multiplicacao(num1, num2)}")
#       elif escolha == '4':
#         resultado_div = divisao(num1, num2)
#         if isinstance(resultado_div, str):
#             print(f"\n{resultado_div}")
#         else:
#             print(f"\nResultado: {num1} / {num2} = {resultado_div}")
#     else:
#       print("Opção inválida. Por favor, escolha uma opção entre 1 e 5.")

#     input("\nPressione Enter para continuar...")

# if __name__ == "__main__":
#   calculadora()