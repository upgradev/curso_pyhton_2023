class Mamifero:
    def __init__(self) -> None:
        print("Sou um Mamífero")

    def amamentar(self):
        print("Amamentando........")


class Ave:
    def __init__(self) -> None:
        print("Sou uma ave")

    def voar(self):
        print("Voando....")


class Morcego(Mamifero, Ave):
    def __init__(self) -> None:
        Mamifero.__init__(self)
        Ave.__init__(self)
        print("Sou um morcego")

    def emitir_som(self):
        print("Emitindo som de ecolocalização")


morcego = Morcego()
morcego.amamentar()
morcego.voar()
morcego.emitir_som()


print("\n Exercício --------------------------------")


class Musico:
    def tocar_instrumento(self):
        print("Tocando instrumento Musical.")


class Atleta:
    def correr(self):
        print("Correndo na pista")


class MusicoAtleta(Musico, Atleta):
    def exibir_habilidades(self):
        print("Tocando instrumento e correndo")

musico_atleta = MusicoAtleta()
musico_atleta.tocar_instrumento()
musico_atleta.correr()
musico_atleta.exibir_habilidades()