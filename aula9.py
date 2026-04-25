####2.CONTAGEM REGRESSIVA COM PAUSA
####Peça um número inteiro positivo. Use while para fazer uma contagem regressiva até 0, exibindo cada número. Após o término, exiba "Fogo!".

# numero = int(input('Numero Inteiro Positivo: '))
# while numero > 0:
#     print(numero)
#     numero -= 1

# print('fogo!')

####3.MÉDIA DE NOTAS COM WHILE
####Peça notas até que o usuário digite -1. Calcule e exiba a média das notas válidas (0 a 10). Ignore entradas inválidas e use continue quando necessário.

# soma = 0
# quantidade = 0

# while True:
#     nota = float(input("Digite uma nota (0 a 10) ou -1 para sair: "))

#     if nota == -1:
#         break

#     if nota < 0 or nota > 10:
#         print("Nota inválida! Digite um valor entre 0 e 10.")
#         continue

#     soma += nota
#     quantidade += 1

# if quantidade > 0:
#     media = soma / quantidade
#     print(f"Média das notas: {media:.2f}")
# else:
#     print("Nenhuma nota válida foi informada.")


####4.VALIDAÇÃO DE SENHA COM LIMITE DE TENTATIVA
####Defina uma senha fixa (ex: `"python123"`). Dê ao usuário 3 tentativas usando `while`. Se acertar, exiba `"Acesso liberado"` e encerre. Se errar todas, exiba `"Conta bloqueada"`.

# senha_correta = "python123"
# tentativas = 0

# while tentativas < 3:
#     senha = input("Digite a senha: ")

#     if senha == senha_correta:
#         print("Acesso liberado")
#         break

#     tentativas += 1
#     print("Senha incorreta!")

# if tentativas == 3:
#     print("Conta bloqueada")

####5.NUMEROS PRIMOS
####Peça um número inteiro positivo e determine se ele é primo. Use `for` com `range` e `break` para otimizar.

# numero = int(input("Digite um número inteiro positivo: "))

# if numero <= 1:
#     print("Não é primo")
# else:
#     eh_primo = True

#     for i in range(2, int(numero ** 0.5) + 1):
#         if numero % i == 0:
#             eh_primo = False
#             break

#     if eh_primo:
#         print("É primo")
#     else:
#         print("Não é primo")


####6.SEQUÊNCIA DE FIBONACCI 
####Gere os primeiros N termos da sequência de Fibonacci, onde N é informado pelo usuário. Use `for` ou `while` para iterar.

# n = int(input("Digite a quantidade de termos: "))

# a, b = 0, 1

# for i in range(n):
#     print(a)
#     a, b = b, a + b

# n = int(input("Digite a quantidade de termos: "))

# a, b = 0, 1
# contador = 0

# while contador < n:
#     print(a)
#     a, b = b, a + b
#     contador += 1


####7.SOMA DE DIGÍTOS
####Peça um número inteiro positivo e calcule a soma de seus dígitos. Use while para extrair os dígitos um a um.

# numero = int(input("Digite um número inteiro positivo: "))

# soma = 0

# while numero > 0:
#     digito = numero % 10
#     soma += digito
#     numero //= 10

# print("Soma dos dígitos:", soma)

####8.MENU INTERATIVO
####Crie um menu que permaneça ativo até que o usuário escolha a opção `"Sair"`. As opções podem ser:

# - `1` – Exibir mensagem "Olá!"
# - `2` – Exibir a data/hora atual (use `import datetime`)
# - `3` – Sair

# Use `while True` e `break` para sair.

# import datetime

# while True:
#     print("\nMenu:")
#     print("1 - Exibir mensagem")
#     print("2 - Exibir data/hora atual")
#     print("3 - Sair")

#     opcao = input("Escolha uma opção: ")

#     if opcao == "1":
#         print("Olá!")

#     elif opcao == "2":
#         agora = datetime.datetime.now()
#         print("Data e hora atual:", agora)

#     elif opcao == "3":
#         print("Saindo...")
#         break

#     else:
#         print("Opção inválida! Tente novamente.")

####9.SIMULADOR DE LANÇAMENTO DE DADOS
####Simule 100 lançamentos de um dado de 6 faces. Conte quantas vezes cada face foi sorteada e exiba o resultado. Use `for` e `random.randint(1,6)`. (Importe `random`.)

# import random

# # Inicializa o contador de cada face
# contagens = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

# # Simula 100 lançamentos
# for i in range(100):
#     resultado = random.randint(1, 6)
#     contagens[resultado] += 1

# # Exibe os resultados
# print("Resultados dos 100 lançamentos:")
# for face in contagens:
#     print(f"Face {face}: {contagens[face]} vezes")
