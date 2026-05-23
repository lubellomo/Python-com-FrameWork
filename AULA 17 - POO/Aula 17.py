from abc import ABC, abstractmethod


class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor  = autor
        self.ano    = ano

    def __str__(self):
        return f"'{self.titulo}' por {self.autor} ({self.ano})"


class LivroDigital(Livro):
    def __init__(self, titulo, autor, ano, fmt):
        super().__init__(titulo, autor, ano)
        self.formato = fmt

    def __str__(self):
        return f"{super().__str__()} [{self.formato}]"


class Veiculo(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def mover(self):
        ...


class Carro(Veiculo):
    def mover(self):
        print(f"{self.nome}: acelerando com motor 🚗")


class Bicicleta(Veiculo):
    def mover(self):
        print(f"{self.nome}: pedalando! 🚲")


class Vetor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vetor({self.x}, {self.y})"

    def __add__(self, outro):
        return Vetor(self.x + outro.x, self.y + outro.y)

    def __sub__(self, outro):
        return Vetor(self.x - outro.x, self.y - outro.y)

    def __mul__(self, escalar):
        return Vetor(self.x * escalar, self.y * escalar)


def saudacao(self):
    print(f"Olá! Sou uma instância de {type(self).__name__}")


Anonima = type("Anonima", (object,), {"saudacao": saudacao})


# --- Rodando tudo ---

print("=== Livro ===")
l1 = Livro("Dom Casmurro", "Machado", 1899)
l2 = LivroDigital("Sapiens", "Harari", 2011, "PDF")
print(l1)
print(l2)

print("\n=== Veículo ===")
frota = [Carro("Fusca"), Bicicleta("Caloi")]
for v in frota:
    v.mover()

print("\n=== Vetor ===")
a = Vetor(2, 3)
b = Vetor(1, 4)
print(a + b)
print(a - b)
print(a * 3)

print("\n=== Classe Anônima ===")
obj = Anonima()
obj.saudacao()
print(type(obj))
print(isinstance(obj, object))
