# ---------------------------------------------
# EXERCÍCIO 1 - CLASSE LIVRO
# ---------------------------------------------

class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo =  titulo
        self.autor = autor
        self.ano = ano
        self.dispo = True

    def emprestrar(self):
      nome  = input('nome: ')
    #   print(self.dispo)
      emprestar =  input('Emprestar? ')
      if emprestar == 'sim':
        if nome  == self.titulo:
            if self.dispo == True:
                print(self.dispo)
                print('esta disponivel ...')
                self.dispo = False
                print('Emprestado')
                return self.dispo

            else:
                print('Não esta diponivel')
        else:
            print('Não temos esse livro...')
    def devolver(self):
        self.dispo = True
        print('Livro devolvido')
        return self.dispo
    def info(self):
        return [
        self.titulo,
        self.autor,
        self.ano,
        self.dispo 
        ]


livro =  Livro('Cisne negro', 'taleb','2012')
livro.emprestrar()
livro.devolver()
print(livro.info())

# ---------------------------------------------
# EXERCÍCIO 2 - CLASSE DE FUNCIONÁRIO
# ---------------------------------------------

class Funcionario:
    def __init__(self, nome, cargo, salario_base):
        self.nome = nome
        self.cargo = cargo
        self.salario_base = salario_base

    def aumentar_salario(self, percentual):
        aumento = self.salario_base * (percentual / 100)
        self.salario_base += aumento

    def calcular_bonus(self):
        return self.salario_base * 0.10

    def exibir_dados(self):
        print("\n=== Dados do Funcionário ===")
        print("Nome:", self.nome)
        print("Cargo:", self.cargo)
        print(f"Salário: R$ {self.salario_base:.2f}")
        print(f"Bônus: R$ {self.calcular_bonus():.2f}")


# Criando funcionário
funcionario1 = Funcionario("Carlos", "Desenvolvedor", 5000)

# Usuário informa a porcentagem
percentual = float(input("Digite a porcentagem de aumento: "))

# Aplicando aumento
funcionario1.aumentar_salario(percentual)

# Mostrando dados atualizados
funcionario1.exibir_dados()


# =========================================
# 3. Classe Carro com Controle de Velocidade
# =========================================

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0

    def acelerar(self, valor):
        self.velocidade += valor

        # Limite máximo
        if self.velocidade > 200:
            self.velocidade = 200

        print(f"{self.modelo} acelerou para {self.velocidade} km/h")

    def frear(self, valor):
        self.velocidade -= valor

        # Não pode ficar negativa
        if self.velocidade < 0:
            self.velocidade = 0

        print(f"{self.modelo} reduziu para {self.velocidade} km/h")

    def velocidade_atual(self):
        print(f"Velocidade atual: {self.velocidade} km/h")


# Criando carro
carro1 = Carro("Honda", "Civic")

print("=== Controle do Carro ===")

# Acelerando
carro1.acelerar(50)
carro1.acelerar(100)
carro1.acelerar(80)  # Máximo 200

# Freando até parar
carro1.frear(70)
carro1.frear(80)
carro1.frear(100)

# Mostrando velocidade final
carro1.velocidade_atual()


# =========================================
# 4. Classe Agenda
# =========================================

class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print(f"E-mail: {self.email}")


class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)
        print(f"Contato {contato.nome} adicionado com sucesso!")

    def listar_contatos(self):
        print("\n=== Lista de Contatos ===")

        for contato in self.contatos:
            contato.exibir_dados()
            print("-" * 20)

    def buscar_contato(self, nome):
        print(f"\nBuscando contato: {nome}")

        for contato in self.contatos:
            if contato.nome.lower() == nome.lower():
                contato.exibir_dados()
                return

        print("Contato não encontrado.")


# Criando contatos
contato1 = Contato("Ana", "1199999-1111", "ana@email.com")
contato2 = Contato("Bruno", "1198888-2222", "bruno@email.com")
contato3 = Contato("Carla", "1197777-3333", "carla@email.com")

# Criando agenda
agenda = Agenda()

# Adicionando contatos
agenda.adicionar_contato(contato1)
agenda.adicionar_contato(contato2)
agenda.adicionar_contato(contato3)

# Listando contatos
agenda.listar_contatos()

# Buscando contatos
agenda.buscar_contato("Bruno")
agenda.buscar_contato("Pedro")