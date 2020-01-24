from math import sqrt


class RedeNeural():
    def __init__(self, rede, entradas, pesos):
        self.entradas = entradas
        self.rede = rede
        self.pesos = pesos

    def iniciar(self):
        self.entradas, self.pesos = RedeNeural.rede(self)
        return {'saida': self.entradas, 'pesos': self.pesos}

    def n(peso, entradas):
        resultado = sum(entradas) * sqrt(peso ** 2)
        return resultado

    def rede(self):
        for camada in range(0, len(self.rede)):
            novasEntradas = []

            for neuronio in range(0, self.rede[camada]):
                novasEntradas.append(
                    RedeNeural.n(
                        self.pesos[camada][neuronio],
                        self.entradas))

            self.entradas = novasEntradas
        return self.entradas, self.pesos
'''
rede = [2,2,1]
entradas = [16,32]
pesos = [[-6.556, 3.89], [2.121, 3.149],[-0.025]]
n = RedeNeural(rede,entradas,pesos)
print(n.iniciar())
'''
