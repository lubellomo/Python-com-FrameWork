# BANCO main()
# SAQUE 
# DEPOSITO
# EXTRATO
# EMPRESTIMO

def saque(saldo, saque):
    return saldo - saque 

def deposito(saldo, saque):
    return saldo + saque

def extrato (ex):
    return ex

def emprestimo(valor, saldo):
    to =  valor + saldo 
    return f'emprestimo  R$ {valor} , Em conta R${to}'

def main_banco():
  
  dados = {
      'saldo':5000,
      'extrato':[5000],
      'emprestimos':0
    }
  while True:   

    menu  =  input('''Escolha uma opção:
                   
                   1 - saque
                   2 - deposito
                   3 - extrato
                   4 - emprestimo 
                   
                    ''')
    if menu == '1':
        valor  =  float(input('R$ '))
        saqu =  saque(dados['saldo'], valor)
        dados['extrato'].append(-valor)
        print(saqu)
        dados['saldo'] = saqu
        print(dados)
    elif menu  == '2':
        valor  =  float(input('R$ '))
        depo=  deposito(dados['saldo'], valor)
        dados['extrato'].append(valor)
        print(depo)
        dados['saldo'] = depo        
        print(dados)         
    elif menu == '3':
        ex = extrato(dados['extrato'])
        print(ex)
    elif menu =='4':
        valor  =  float(input('R$ '))
        dados['emprestimos'] += (valor)
        emprestimos = emprestimo(valor,dados['saldo'])
        dados['extrato'].append(valor)
        print(emprestimos)
    else:
        print('Digite algo valido')    

   
main_banco()
input('digite enter para sair')


