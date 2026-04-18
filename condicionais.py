# #classificação de notas com menção
# 
# nota = float(input("Digite a nota do aluno (0 a 10):" ))
# 
# if nota >= 9:
#  print ('Excelente')
# 
# elif nota >= 7 and nota < 9:
#  print ('Bom')
# 
# elif nota >= 5 and nota < 7:
#  print ('Regular')
# 
# else:
#  print ('Insuficiente')
 
#

#validação de triângulo

# lado_a = float(input('Digite o primeiro lado: '))
# lado_b = float(input('Digite o segundo lado: '))
# lado_c = float(input('Digite o terceiro lado: '))
# 
# 
# if lado_a < lado_b + lado_c and lado_b < lado_a + lado_c and lado_c < lado_a + lado_b:
#         if lado_a == lado_b and lado_b == lado_c:
#             print('Equilátero')
#         elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
#             print ('Isóceles')
#         else:
#             print ('Escaleno')
# 
# 
# else:
#     print ('Os valores não formam um triângulo')



#CÁLCULO DE IMC COM FAIXAS

# peso = float(input('Digite o peso em kg: '))
# altura = float(input('Digite a altura em metros: '))
# imc = peso / altura ** 2
#  
# if imc < 18.5:
#     print('Abaixo do peso')
# elif imc >= 18.5 or imc < 25:
#     print('Peso Normal')
# elif imc <= 25 or imc < 30:
#                print('Sobrepeso')
# else:
#     print('Obesidade')

          
# Exiba o salário líquido após os descontos.


salario  =  float(input('R$ '))
if salario >= 1500.0 and salario <2500.0:
     inss =  salario * 0.11
     print('INSS:', inss)
     salario = salario - inss
     print('desconto de 11 % R$', salario)
elif salario >= 2500.0 and salario < 3500.0:
     inss =  salario * 0.11
     print('INSS:', inss)
     salario_inns = salario - inss
     print('desconto de 11 % R$', salario_inss)
     
     irrf = salario * 0.075
     print('IRRF', irrf)
     salario_irrf  =  salario - irrf
     print('desconto do IRRF 7.5 % ', salario_irrf)
     
 
elif salario >= 3500.0 and salario <= 5000.0:
     inss =  salario * 0.11
     print('INSS:', inss)
     salario_in = salario - inss
     print('desconto de 11 % R$', salario_in)
     
     irrf = salario * 0.15
     print('IRRF', round(irrf,2))
     salario  =  salario - irrf
     print('desconto do IRRF 15 % ', round(salario,2))
 
elif salario > 5000.0:
     inss =  salario * 0.11
     print('INSS:', inss)
     salario_in = salario - inss
     print('desconto de 11 % R$', salario_in)
     
     irrf = salario * 0.27
     print('IRRF', irrf)
     salario  =  salario - irrf
     print('desconto do IRRF 27 % ', salario)   

### **Jogo de Pedra, Papel e Tesoura**

# Leia duas jogadas (`"pedra"`, `"papel"` ou `"tesoura"`) e
# determine o vencedor ou empate. Use condicionais aninhadas.
# 
# lista =  ['pedra', 'papel', 'tesoura']
# 
# escolha_maquina =  random.choice(lista)
# print(escolha_maquina)
# chute  =  input('Esolha: pedra, papel ou tesoura')
# 
# if escolha_maquina == chute:
#     print('A máquina escolheu >>',escolha_maquina)
#     print('Você escolheu >>', chute)
#     print('EMPATE!')
# elif escolha_maquina == 'papel' and chute == 'pedra':
#         print('A maquina ganhou')
#         print('A máquina escolheu >>',escolha_maquina)
#         print('Você escolheu >>', chute)
# elif escolha_maquina == 'tesoura' and chute == 'papel':
#         print('A maquina ganhou')
#         print('A máquina escolheu >>',escolha_maquina)
#         print('Você escolheu >>', chute)
# 
# elif escolha_maquina == 'pedra'and chute == 'tesoura':
#         print('A maquina ganhou')
#         print('A máquina escolheu >>',escolha_maquina)
#         print('Você escolheu >>', chute)
# 
# elif escolha_maquina == 'pedra' and chute == 'papel':
#         print('Você ganhou!')
#         print('A máquina escolheu >>',escolha_maquina)
#         print('Você escolheu >>', chute)
# elif escolha_maquina == 'papel' and chute == 'tesoura':
#         print('Você ganhou!')
#         print('A máquina escolheu >>',escolha_maquina)
#         print('Você escolheu >>', chute)
# 
# elif escolha_maquina == 'tesoura' and chute == 'pedra':
#         print('Você ganhou!')
#         print('A máquina escolheu >>',escolha_maquina)
#         print('Você escolheu >>', chute)
# else:
#     print('DIGITE ALGO VÁLIDO')
# 
# 
# 


# 
# 
# Leia a nota da N1 e N2. Calcule a média ((N1+N2)/2). Se média ≥
# 7, aprovado. Se média < 4, reprovado. Caso contrário, o aluno
# vai para recuperação. Nesse caso, leia a nota da recuperação (NR).
# A média final é (média + NR)/2. Se média final ≥ 5, aprovado; senão,
# reprovado.

# 
# n1  =  float(input('>>'))
# n2  =  float(input('>>'))
# media  =  (n1 +  n2) / 2
# 
# if  media >=7:
#     print('Aprovado')
# elif media > 4 and media <7:
#     nr  =  float(input('Nota de recuperação: '))
#     nf =  (media +  nr)/2
#     if nf >= 5:
#         print('Aprovada ')
#     else: print('Reprovado')    
#     
# else:
#     print('reprovado')
# 


# Leia o ano de nascimento, o sexo (`M` ou `F`) e se o usuário possui
# alguma deficiência impeditiva (`sim` ou `não`).
# 
# - Se sexo for `F`, exiba `"Não obrigatório"`.
# - Se sexo for `M`, calcule a idade. Se idade < 18, exiba o
# tempo restante. Se idade = 18, exiba `"Aliste-se imediatamente"`.
# Se idade > 18 e ≤ 45, exiba `"Já passou do prazo"`. Se idade > 45,
# exiba `"Dispensado por idade"`.
# - Se houver deficiência, altere a mensagem para `"Dispensado por
# condição de saúde"` (prioridade sobre outras mensagens).
#


# deficiencia = input('POssui deficiencia s/n?')
# ano_n =  int(input('ano: '))
# sexo = input('F/M')
# 
# 
# 
# if sexo == 'f':
#     print('Não obrigatório...')
# elif sexo == 'm':
#     idade =  2026 - ano_n
#     
#     if deficiencia == 's':
#         print('dispensado por condição de saúde')
#     if idade == 18 and deficiencia == 'n':
#         print('Aliste -se imediatamente')
#     elif idade >18  and idade <= 45:
#         print('Já passou do prazo')
# 
        
        
#         
# Leia a idade do cliente e o tipo de plano (`"basico"`,
#                                             `"standard"`, `"premium"`).
# O valor mensal é calculado como:
# 
# - Básico: R$ 100 + (idade * 2)
# - Standard: R$ 150 + (idade * 3)
# - Premium: R$ 200 + (idade * 5)
#     
#     Se o cliente tiver mais de 60 anos, há um acréscimo de
#     10% sobre o valor total.        
#         
        
# idade = int(input('idade: '))
# plano =  input('PLano: basico/ standard/premium  ')
# 
# if plano == 'basico':
#     valor  = 100 + idade * 2
#     print('R$', valor)
#     if idade > 60:
#         n_v =  valor * 0.10
#         valor  =  valor + n_v
#         print('R$',valor)
# elif plano == 'standard':
#     valor  =  150 + idade * 3
#     print('R$', valor)    
#     if idade > 60:
#         n_v =  valor * 0.10
#         valor  =  valor + n_v
#         print('R$',valor)        
# elif plano == 'standard':
#     valor  =  200 + idade * 5         
#     print('R$', valor)
#     if idade > 60:
#         n_v =  valor * 0.10
#         valor  =  valor + n_v
#         print('R$',valor)    
#         
        
#         
# meses   =  [0,1,2,3,4,5,6,7,8,9,10,11,12]
# dias_meses = [0,list(range(0,31)),
#               list(range(0,29)),
#               list(range(0,31)),
#               list(range(0,30)),
#               list(range(0,31)),
#               list(range(0,30)),
#               list(range(0,31)),
#               list(range(0,31)),
#               list(range(0,30)),
#               list(range(0,31)),
#               list(range(0,30)),
#               list(range(0,31))
#               ]
# 
# ano =  int(input('ano: '))
# mes =  int(input('Digite o número do mês: '))
# dia =  int(input('Digite o dia:  '))
# 
# 
# if (ano % 400 == 0 or ano % 4 == 0) or (ano % 100 ==0):
#     print('ano bissexto...')
# else:
#     print('Não é bissexto...')
# 
# if mes in meses:
#     i =  meses.index(mes)
#     if dia in dias_meses[i]:
#         print('data válida')
# else:
#     print('Data invalida')
#         
# 

v = int(input('>>'))

if v < 10 or v > 1000 or v % 5 != 0:
    print('invalida')
else:
    p50 = v // 50
    v  =  v % 50

    p20 = v // 20
    v  =  v % 20

    p10 = v // 10
    v  =  v % 10

    p5 = v // 5
    v  =  v % 5    

    print('notas de 50', p50)
    print('notas de 20', p20)
    print('notas de 10', p10)
    print('notas de 5', p5)        
        
        

