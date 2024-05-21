class Retangulo:
    def __init__(self, largura, altura) -> None:
        self._largura = largura
        self._altura = altura

    @property
    def largura(self):
        return self._largura

    @largura.setter
    def largura(self, valor):
        if valor > 0:
            self._largura = valor
        else:
            print("Largura deve ser maior que zero")

    @property
    def area(self):
        return self._largura * self._altura

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        if altura > 0:
            self._altura = altura
        else:
            print("Altura deve ser maior que zero")


r = Retangulo(largura=5, altura=6)
print(f"Area: {r.area}")

r.largura = 7
print(f"Largura: {r.largura}")
print(f"Area: {r.area}")
r.largura = -5
r.altura = 2
print(r.altura)
print(f"Area: {r.area}")
