# ####1. Calculadora com Funções
# def somar(a, b):
#     return a + b

# def subtrair(a, b):
#     return a - b

# def multiplicar(a, b):
#     return a * b

# def dividir(a, b):
#     if b == 0:
#         return "Erro: divisão por zero"
#     return a / b


# a = float(input("Primeiro número: "))
# b = float(input("Segundo número: "))
# op = input("Operação (+, -, *, /): ")

# if op == "+":
#     print(somar(a, b))
# elif op == "-":
#     print(subtrair(a, b))
# elif op == "*":
#     print(multiplicar(a, b))
# elif op == "/":
#     print(dividir(a, b))
# else:
#     print("Operação inválida")

####2. Validador de CPF (simplificado)
# def validar_cpf(cpf):
#     if len(cpf) != 11 or not cpf.isdigit():
#         return False

#     # primeiro dígito
#     soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
#     dig1 = (soma * 10 % 11) % 10

#     # segundo dígito
#     soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
#     dig2 = (soma * 10 % 11) % 10

#     return cpf[-2:] == f"{dig1}{dig2}"


# print(validar_cpf("12345678909"))
# print(validar_cpf("11144477735"))


####3. Gerador de Tabuada
# def tabuada(numero, inicio=1, fim=10):
#     for i in range(inicio, fim + 1):
#         print(f"{numero} x {i} = {numero * i}")

# tabuada(5)


####4. Contador de Palavras
# def contar_palavras(texto):
#     palavras = texto.split()
#     contagem = {}

#     for p in palavras:
#         p = p.lower()
#         contagem[p] = contagem.get(p, 0) + 1

#     return contagem

# frase = input("Digite uma frase: ")
# print(contar_palavras(frase))


####5. Ordenação Personalizada (Bubble Sort)
# def ordenar_lista(lista, crescente=True):
#     n = len(lista)

#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if crescente:
#                 if lista[j] > lista[j + 1]:
#                     lista[j], lista[j + 1] = lista[j + 1], lista[j]
#             else:
#                 if lista[j] < lista[j + 1]:
#                     lista[j], lista[j + 1] = lista[j + 1], lista[j]

#     return lista


# print(ordenar_lista([5, 2, 9, 1]))
# print(ordenar_lista([5, 2, 9, 1], crescente=False))


####6. Jogo de Adivinhação
# import random

# def jogar():
#     numero = random.randint(1, 100)
#     tentativas = 0

#     while True:
#         palpite = int(input("Adivinhe o número (1-100): "))
#         tentativas += 1

#         if palpite < numero:
#             print("Maior")
#         elif palpite > numero:
#             print("Menor")
#         else:
#             print("Acertou!")
#             return tentativas


# t = jogar()
# print("Tentativas:", t)


####7. Conversor de Bases
# def converter_base(numero, base_origem, base_destino):
#     decimal = int(numero, base_origem)

#     if base_destino == 2:
#         return bin(decimal)[2:]
#     elif base_destino == 8:
#         return oct(decimal)[2:]
#     elif base_destino == 10:
#         return str(decimal)
#     elif base_destino == 16:
#         return hex(decimal)[2:].upper()
#     else:
#         return "Base inválida"


# print(converter_base("1010", 2, 16))


####8. Sistema de Caixa Eletrônico
# def sacar(valor):
#     if valor % 2 != 0 or valor <= 0:
#         return None

#     notas = [100, 50, 20, 10, 5, 2]
#     resultado = {}

#     for n in notas:
#         resultado[n], valor = divmod(valor, n)

#     return resultado


# print(sacar(186))


####9. Análise de Lista com Múltiplos Retornos
# def analisar_lista(lista):
#     menor = min(lista)
#     maior = max(lista)
#     soma = sum(lista)
#     media = soma / len(lista)
#     return menor, maior, soma, media


# numeros = []

# while True:
#     n = int(input("Digite um número (-1 para parar): "))
#     if n == -1:
#         break
#     numeros.append(n)

# menor, maior, soma, media = analisar_lista(numeros)

# print("Menor:", menor)
# print("Maior:", maior)
# print("Soma:", soma)
# print("Média:", media)


####10. Sistema de Estoque (lista global)
# estoque = []

# def adicionar_produto(nome, quantidade):
#     global estoque
#     estoque.append({"nome": nome, "quantidade": quantidade})

# def remover_produto(nome):
#     global estoque
#     estoque = [p for p in estoque if p["nome"] != nome]

# def listar_estoque():
#     for p in estoque:
#         print(p)


# while True:
#     print("\n1-Adicionar 2-Remover 3-Listar 4-Sair")
#     op = input("Opção: ")

#     if op == "1":
#         n = input("Nome: ")
#         q = int(input("Quantidade: "))
#         adicionar_produto(n, q)

#     elif op == "2":
#         n = input("Nome: ")
#         remover_produto(n)

#     elif op == "3":
#         listar_estoque()

#     elif op == "4":
#         break