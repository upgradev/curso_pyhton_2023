class Pessoa:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.acordado = False
        self.comendo = False
        self.dirigindo = False

    def acordar(self):
        if self.acordado == True:
            print(f"{self.nome} já está acordado")
        else:
            self.acordado = True
            print(f"{self.nome} acordou.")

    def comer(self):

        if self.dirigindo:
            print(f"{self.nome} não pode comer enquanto dirige.")
        elif not self.acordado:
            print(f"{self.nome} não pode comer enquanto está dormindo.")
        elif self.comendo:
            print(f"{self.nome} já esta comendo")
        else:
            self.comendo = True
            print(f"{self.nome} começou a comer.")

    def parar_de_comer(self):
        if not self.comendo:
            print(f"{self.nome} não esta comendo no momento.")
        else:
            self.comendo = False
            print(f"{self.nome} Terminou de comer.")

    def dirigir(self):

        if not self.acordado:
            print(f"{self.nome} não pode dirigir enquanto está dormindo.")
        elif self.comendo:
            print(f"{self.nome} não deve dirigir enquanto come.")
        elif self.dirigindo:
            print(f"{self.nome} já esta dirigindo.")
        else:
            self.dirigindo = True
            print(f"{self.nome} começou a dirigir.")

    def parar_de_dirigir(self):

        if not self.dirigindo:
            print(f"{self.nome} não esta dirigindo")
        else:
            self.dirigindo = False
            print(f"{self.nome} João parou de dirigir.")

    def dormir(self):

        if self.dirigindo:
            print(f"{self.nome} não pode dormir enquanto dirige")
        elif self.comendo:
            print(f"{self.nome} não pode dormir enquanto come")
        elif not self.acordado:
            print(f"{self.nome} ja esta dormindo")
        else:
            print(f"{self.nome} João foi dormir")
            self.acordado = False
            self.comendo = False


joao = Pessoa("João")
joao.acordar()
joao.acordar()
joao.comer()
joao.comer()
joao.parar_de_comer()
joao.parar_de_comer()
joao.dirigir()
joao.dirigir()
joao.comer()
joao.parar_de_dirigir()
joao.parar_de_dirigir()
joao.dormir()
joao.dormir()
