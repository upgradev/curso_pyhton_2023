class Termostato:
    def __init__(self, temperatura_atual=20) -> None:
        self.temperatura_atual = temperatura_atual

    def aumentar_temperatura(self, valor):
        self.temperatura_atual += valor
        print(
            f"Temperatura aumentanda em {valor}°. Nova temperatura {self.temperatura_atual}°")

    def diminuir_temperatura(self, valor):
        self.temperatura_atual -= valor
        print(
            f"Temperatura diminuída em {valor}°. Nova temperatura {self.temperatura_atual}°")

    def configurar_temperatura(self, nova_temperatura):
        self.temperatura_atual = nova_temperatura
        print(f"Temperatura configurada para {nova_temperatura}°")

    def mostrar_temperatura(self):
        print(f"Temperatura atual: {self.temperatura_atual}°")


meu_termostato = Termostato()
meu_termostato.aumentar_temperatura(5)
meu_termostato.diminuir_temperatura(10)
meu_termostato.configurar_temperatura(10)
meu_termostato.mostrar_temperatura()
meu_termostato.aumentar_temperatura(50)
meu_termostato.diminuir_temperatura(25)
meu_termostato.configurar_temperatura(15)
meu_termostato.mostrar_temperatura()
