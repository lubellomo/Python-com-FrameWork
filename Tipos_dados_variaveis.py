# dados 
# scrip - interpretar -  resposta 
# lógica + melhorar 
# memória ram - curta duração

# 4 tipos

# cadastro 
# nome idade email peso altura endereco
# salario > 2000

# texto   -  "text"  'text'  -  nome  - email - endereco
# inteiro - 10,  0  ,  -1  -  idade 
# decimal - 5.2, 9.10,0.  - peso  - altura  - 
# lógico  - True ,  False  -  saslario
#            1        0

print(10 + 2)
print(True + 10)
print(5.2 + 5)
print('text' + "fhsdjkfh")
print('fhsdgfhsdgfs')


# concatenação juntar dados

print('Olá', 'João')
print(f'Olá {'João'}')

# indentação -  organizar o código

print()


# variáveis

imc = 0

# Não podem por numero
# caracteres especiais # @% &*

# pode começar por letra
# _ underline pode utilizar

# seguida de um igual 

# ESTRUTURA DE DADO

imc = 0 
altura  =  1.70
peso = 62.0
imc =  peso // (altura ** 2)
print(imc)

# SINAIS ARITIMÉTICOS
# +   -    *   /   %   **  // 

print('SINAIS ARITMÉTICOS')
# saida sem é um número 

x = 10
y = 20
x = 200

print(x + y)
print(x - y)
print(x / y)
print(x * y)
print(x ** y)


print(x // y)
print(x % y)


# sinais lógicos 
y = 20
x = 200
print(x == y) # comparação
print(x > y) # maior
print(x < y) # menor
print(x >= y) # maior ou igual
print(x <= y) # menor ou igual
print(x != y) # diferente


print() # imprime algo ambiente de teste 


var =  10 # variáveis 


# nome = input('Digite seu nome:  ') # dinamico 
# # 


# print(nome)


# nome  = 'Julia'


# nome  =  input('Nome: ')



# print('CADASTRE SEUS DADOS: ')
# # int()  float() str() bool() type casting


# nome = input('Nome: ')
# idade  = int(input('Idade: ')) + 10
# endereco  = input('Endereço: ')
# curso = input('Curso: ')
# altura = float(input('Altura'))
# saldo_banco = float(input('Saldo: '))


# print('NOME:', nome)
# print('IDADE:', idade)
# print('ENDEREÇO:', endereco)
# print('CURSO:', curso)
# print('ALTURA:', altura)
# print('SALDO NO BANCO:', saldo_banco)

# PEDINDO DOIS NÚMEROS AO USUARIO
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

#OPERAÇÕES MATEMÁTICAS
print("Soma: " , num1 + num2)
print("subtracao: " , num1 - num2)
print("multiplicacao: " , num1 * num2)
print("divisão: " , num1 / num2 ) 

#VERIFICAÇÃO
print("Os numeros são iguais?", num1 == num2)
print("O primeiro é maior que o segundo", num1 > num2)
print("Pelo menos um dos numeros é maior que 10" , (num1 > 10 ) or (num2 > 10))

# Peça o valor de um produto e: 

# Calcule um desconto de 10%.

# Mostre o valor final.


# Verifique se o valor final é maior que 100.


# Verifique se o produto ficou barato (menor que 50).


#VALOR DO PRODUTO:
valor = float(input("Digite o valor do produto"))

#DESCONTO DE 10%
desconto = valor *0.10
valor_final = valor - desconto

#VALOR FINAL DO PRODUTO COM DESCONTO
print("Valor Final: " , valor_final)

#VERIFICAR SE O VALOR FINAL É MAIOR QUE 10
print("valor é maior que 100?" , valor_final > 100)

#VERIFICAR SE O PRODUTO FICOU MENOR QUE 50
print("Valor é menor que 50?" , valor_final < 50)







