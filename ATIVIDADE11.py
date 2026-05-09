# # 1
# arquivo = open('cadastro.txt', 'r')
# for linha in arquivo:
#     dados = linha.strip().split(',')
#     nome =  dados[0]
#     idade = dados[1]
#     print('Nome', nome, 'idade', idade)


# arquivo.close()


# # 2
# with open('cadastro.csv', 'r') as c:
#     conteudo = c.read()
#     print(conteudo)


# EXERCÍCIO 1 — Criar e escrever
# ------------------------------------------------------------
def exercicio_1():
    print("=== Cadastro de Pessoas ===")
    print("Digite 'sair' no nome para encerrar.\n")
 
    with open("cadastro.txt", "a", encoding="utf-8") as arquivo:
        while True:
            nome = input("Nome: ").strip()
            if nome.lower() == "sair":
                print("Cadastro encerrado.")
                break
 
            idade = input("Idade: ").strip()
            arquivo.write(f"{nome},{idade}\n")
            print(f"✔ '{nome}' cadastrado com sucesso!\n")
 
 
# ------------------------------------------------------------
# EXERCÍCIO 2 — Ler e exibir
# ------------------------------------------------------------
def exercicio_2():
    print("=== Pessoas Cadastradas ===\n")
 
    try:
        with open("cadastro.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
 
        if not linhas:
            print("Nenhuma pessoa cadastrada.")
            return
 
        for linha in linhas:
            linha = linha.strip()
            if linha:                          # ignora linhas em branco
                nome, idade = linha.split(",", 1)
                print(f"Nome: {nome}, Idade: {idade}")
 
    except FileNotFoundError:
        print("Arquivo 'cadastro.txt' não encontrado. Execute o Exercício 1 primeiro.")
 
 
# ------------------------------------------------------------
# EXERCÍCIO 3 — Contar linhas
# ------------------------------------------------------------
def contar_linhas(nome_arquivo):
    """Retorna o número de linhas não-vazias do arquivo."""
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            return sum(1 for linha in arquivo if linha.strip())
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        return 0
 
 
def exercicio_3():
    print("=== Contar Linhas ===\n")
    total = contar_linhas("cadastro.txt")
    print(f"O arquivo 'cadastro.txt' possui {total} linha(s).")
 
 
# ------------------------------------------------------------
# EXERCÍCIO 4 — Procurar palavra
# ------------------------------------------------------------
def exercicio_4():
    print("=== Procurar Palavra em Arquivo ===\n")
 
    palavra      = input("Digite a palavra a procurar: ").strip().lower()
    nome_arquivo = input("Nome do arquivo: ").strip()
 
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().lower()
 
        # Conta todas as ocorrências (sobrepostas não são contadas pelo padrão)
        ocorrencias = conteudo.count(palavra)
        print(f"\nA palavra '{palavra}' aparece {ocorrencias} vez(es) em '{nome_arquivo}'.")
 
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
 
 
# ------------------------------------------------------------
# EXERCÍCIO 5 — Copiar arquivo
# ------------------------------------------------------------
def exercicio_5():
    print("=== Copiar Arquivo ===\n")
 
    origem  = input("Nome do arquivo de origem:  ").strip()
    destino = input("Nome do arquivo de destino: ").strip()
 
    try:
        with open(origem, "r", encoding="utf-8") as arq_origem:
            linhas = arq_origem.readlines()
 
        with open(destino, "w", encoding="utf-8") as arq_destino:
            arq_destino.writelines(linhas)
 
        print(f"\n✔ '{origem}' copiado para '{destino}' com sucesso! ({len(linhas)} linha(s) copiada(s)).")
 
    except FileNotFoundError:
        print(f"Arquivo de origem '{origem}' não encontrado.")
 
 
# ------------------------------------------------------------
# MENU PRINCIPAL
# ------------------------------------------------------------
def menu():
    opcoes = {
        "1": ("Criar e escrever (cadastro.txt)",  exercicio_1),
        "2": ("Ler e exibir cadastro.txt",         exercicio_2),
        "3": ("Contar linhas de cadastro.txt",     exercicio_3),
        "4": ("Procurar palavra em arquivo",       exercicio_4),
        "5": ("Copiar arquivo",                    exercicio_5),
        "0": ("Sair",                              None),
    }
 
    while True:
        print("\n" + "=" * 40)
        print("  EXERCÍCIOS — MANIPULAÇÃO DE ARQUIVOS")
        print("=" * 40)
        for chave, (descricao, _) in opcoes.items():
            print(f"  [{chave}] {descricao}")
        print("=" * 40)
 
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