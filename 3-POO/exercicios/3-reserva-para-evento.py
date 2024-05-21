class Evento:
    def __init__(self, capacidade=10) -> None:
        self.capacidade = capacidade
        self.lugares_diponiveis = capacidade

    def reservar(self):
        if self.lugares_diponiveis > 0:
            self.lugares_diponiveis -= 1
            print("Lugar reservado com sucesso")
        else:
            print("Não há mais lugares disponiveis")
            return

    def cancelar(self):
        if self.lugares_diponiveis != self.capacidade:
            self.lugares_diponiveis += 1
            print("reserva cancelado com sucesso")
        else:
            print("Não há reserva para cancelar")
            return

    def lugares_disponiveis(self):
        print(f"Lugares Disponíveis: {self.lugares_diponiveis}")


evento = Evento()

# evento.lugares_disponiveis()
# evento.reservar()
# evento.reservar()
# evento.reservar()
# evento.lugares_disponiveis()
# evento.cancelar()
# evento.cancelar()
# evento.cancelar()
# evento.cancelar()
# evento.cancelar()
# evento.reservar()
# evento.lugares_disponiveis()

for _ in range(7):
    evento.reservar()
evento.lugares_disponiveis()

for _ in range(8):
    evento.cancelar()
evento.lugares_disponiveis()