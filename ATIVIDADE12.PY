
# EXERCÍCIO 1 — Classe Pessoa

class Pessoa:
    def __init__(self, nome, idade):
        self.nome  = nome
        self.idade = idade
 
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
 
 
def exercicio_1():
    print("=== Exercício 1 — Classe Pessoa ===\n")
 
    pessoa1 = Pessoa("Ana", 28)
    pessoa2 = Pessoa("Carlos", 35)
 
    pessoa1.apresentar()
    pessoa2.apresentar()
 
 

# EXERCÍCIO 2 — Classe Retângulo

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura  = altura
 
    def calcular_area(self):
        return self.largura * self.altura
 
    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)
 
 
def exercicio_2():
    print("=== Exercício 2 — Classe Retângulo ===\n")
 
    ret = Retangulo(5, 3)
    print(f"Largura:   {ret.largura}")
    print(f"Altura:    {ret.altura}")
    print(f"Área:      {ret.calcular_area()}")
    print(f"Perímetro: {ret.calcular_perimetro()}")
 
 
# ------------------------------------------------------------
# EXERCÍCIO 3 — Classe Conta Bancária
# ------------------------------------------------------------
class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo   = 0.0
 
    def depositar(self, valor):
        if valor <= 0:
            print("O valor do depósito deve ser positivo.")
            return
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado.")
 
    def sacar(self, valor):
        if valor <= 0:
            print("O valor do saque deve ser positivo.")
            return
        if valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado.")
 
    def exibir_saldo(self):
        print(f"Titular: {self.titular} | Saldo: R$ {self.saldo:.2f}")
 
 
def exercicio_3():
    print("=== Exercício 3 — Classe Conta Bancária ===\n")
 
    conta = ContaBancaria("Maria")
    conta.exibir_saldo()
 
    conta.depositar(1000)
    conta.depositar(500)
    conta.sacar(200)
    conta.sacar(2000)       # deve exibir "Saldo insuficiente"
 
    conta.exibir_saldo()
 
 
# ------------------------------------------------------------
# EXERCÍCIO 4 — Classe Produto
# ------------------------------------------------------------
class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.nome               = nome
        self.preco              = preco
        self.quantidade_estoque = quantidade_estoque
 
    def total_estoque(self):
        return self.preco * self.quantidade_estoque
 
    def adicionar_estoque(self, quantidade):
        if quantidade <= 0:
            print("Quantidade deve ser positiva.")
            return
        self.quantidade_estoque += quantidade
        print(f"{quantidade} unidade(s) adicionada(s). Estoque atual: {self.quantidade_estoque}")
 
    def remover_estoque(self, quantidade):
        if quantidade <= 0:
            print("Quantidade deve ser positiva.")
            return
        if quantidade > self.quantidade_estoque:
            print(f"Estoque insuficiente. Disponível: {self.quantidade_estoque}")
        else:
            self.quantidade_estoque -= quantidade
            print(f"{quantidade} unidade(s) removida(s). Estoque atual: {self.quantidade_estoque}")
 
 
def exercicio_4():
    print("=== Exercício 4 — Classe Produto ===\n")
 
    produto = Produto("Notebook", 3500.00, 10)
    print(f"Produto:       {produto.nome}")
    print(f"Preço:         R$ {produto.preco:.2f}")
    print(f"Estoque:       {produto.quantidade_estoque} unidades")
    print(f"Valor total:   R$ {produto.total_estoque():.2f}\n")
 
    produto.adicionar_estoque(5)
    produto.remover_estoque(3)
    produto.remover_estoque(50)    # deve exibir "Estoque insuficiente"
 
    print(f"\nValor total atualizado: R$ {produto.total_estoque():.2f}")
 
 
# ------------------------------------------------------------
# EXERCÍCIO 5 — Classe Aluno
# ------------------------------------------------------------
class Aluno:
    def __init__(self, nome, matricula):
        self.nome       = nome
        self.matricula  = matricula
        self.notas      = []
 
    def adicionar_nota(self, nota):
        if not (0 <= nota <= 10):
            print("Nota inválida. Deve estar entre 0 e 10.")
            return
        self.notas.append(nota)
        print(f"Nota {nota:.1f} adicionada.")
 
    def calcular_media(self):
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)
 
    def situacao(self):
        media = self.calcular_media()
        if media >= 7:
            return "Aprovado"
        elif media >= 5:
            return "Recuperação"
        else:
            return "Reprovado"
 
 
def exercicio_5():
    print("=== Exercício 5 — Classe Aluno ===\n")
 
    aluno = Aluno("Lucas", "2024001")
    aluno.adicionar_nota(8.0)
    aluno.adicionar_nota(6.5)
    aluno.adicionar_nota(7.0)
 
    media = aluno.calcular_media()
    print(f"\nAluno:     {aluno.nome}")
    print(f"Matrícula: {aluno.matricula}")
    print(f"Notas:     {aluno.notas}")
    print(f"Média:     {media:.2f}")
    print(f"Situação:  {aluno.situacao()}")
 
 
# ------------------------------------------------------------
# MENU PRINCIPAL
# ------------------------------------------------------------
def menu():
    opcoes = {
        "1": ("Classe Pessoa",          exercicio_1),
        "2": ("Classe Retângulo",       exercicio_2),
        "3": ("Classe Conta Bancária",  exercicio_3),
        "4": ("Classe Produto",         exercicio_4),
        "5": ("Classe Aluno",           exercicio_5),
        "0": ("Sair",                   None),
    }
 
    while True:
        print("\n" + "=" * 42)
        print("  EXERCÍCIOS — PROGRAMAÇÃO ORIENTADA A OBJETOS")
        print("=" * 42)
        for chave, (descricao, _) in opcoes.items():
            print(f"  [{chave}] {descricao}")
        print("=" * 42)
 
        escolha = input("Escolha uma opção: ").strip()
 
        if escolha == "0":
            print("Até mais!")
            break
        elif escolha in opcoes:
            print()
            opcoes[escolha][1]()
        else:
            print("Opção inválida. Tente novamente.")
 
 
if __name__ == "__main__":
    menu()