from math import sqrt
from random import randint


class RedeNeural():
    def __init__(self, rede, entradas, pesos):
        self.entradas = entradas
        self.pesos = pesos
        self.rede = rede

    def iniciar(self):
        '''Inicia uma rede neural'''

        return RedeNeural.rede(self)

    def neuronio(peso, entradas):
        '''Neurônio individual'''

        resultado = sum(entradas) * sqrt(peso ** 2)
        return resultado

    def rede(self):
        '''Montador da rede neural'''

        # Ande por todas as camadas
        for camada in range(0, len(self.rede)):
            novasEntradas = []

            # Ande pela quantidade de neurônios da camada
            for neuronio in range(0, self.rede[camada]):
                novasEntradas.append(

                    # Aplique em o resultado em um neurônio
                    RedeNeural.neuronio(
                        self.pesos[camada][neuronio],
                        self.entradas))

            self.entradas = novasEntradas

        # Retorne os pesos usados e o resultado
        return self.entradas

class Treino():
    def __init__(self,rede, intervalorMenor, intervaloMaior, esperado, entradas, geracoes
):
        self.intervalorMenor = intervalorMenor
        self.intervaloMaior = intervaloMaior
        self.esperado = esperado
        self.entradas = entradas
        self.geracoes = geracoes
        self.rede = rede

    def melhorRede(self, resultados, esperado):
        melhorResultadoPeso = []

        for resultado in resultados:

            if melhorResultadoPeso == []:
                melhorResultadoPeso = resultado
            else:

                maior = resultado['saida'][0]
                menor = esperado[0]

                if menor > maior:
                    a = maior
                    maior = menor
                    menor = a

                teste = maior - menor

                if melhorResultadoPeso['saida'][0] > teste:
                    melhorResultadoPeso = resultado

            return melhorResultadoPeso

    def gerarPesosAleatorios(self):
        pesos = []

        for camada in self.rede:

            pesosCamada = []
            for neuronio in range(0, camada):

                sorteado = randint(self.intervalorMenor * 1000, self.intervaloMaior * 1000)
                sorteado = sorteado / 1000

                pesosCamada.append(sorteado)

            pesos.append(pesosCamada)

        return pesos

    def treinarRede(self):

        resultados = []

        for geracao in range(0, self.geracoes):
            pesos = Treino.gerarPesosAleatorios(self)

            neuronio = RedeNeural(self.rede, self.entradas, pesos)
            resultados.append(neuronio.iniciar())

        return Treino.melhorRede(self, resultados, self.esperado)



class Otimizar():
    def __init__(self, rede, esperado, entradas, geracoes, melhorPeso, otimizacaoPor = 1):
        self.otimizacaoPor = otimizacaoPor
        self.melhorPeso = melhorPeso
        self.esperado = esperado
        self.entradas = entradas
        self.geracoes = geracoes
        self.rede = rede

    def melhorRede(self, resultados):
        melhorResultadoPeso = []

        for resultado in resultados:

            if melhorResultadoPeso == []:
                melhorResultadoPeso = resultado
            else:

                maior = resultado['saida'][0]
                menor = self.esperado[0]

                if menor > maior:
                    a = maior
                    maior = menor
                    menor = a

                teste = maior - menor

                if melhorResultadoPeso['saida'][0] > teste:
                    melhorResultadoPeso = resultado

        return melhorResultadoPeso

    def otimizarPesosAleatorios(self, melhorPeso):

        pesos = []

        for camada in range(0, len(self.rede)):

            pesosCamada = []
            for neuronio in range(0, self.rede[camada]):

                if melhorPeso[camada][neuronio] < 0:
                    menor = melhorPeso[camada][neuronio] + (
                        melhorPeso[camada][neuronio] / self.otimizacaoPor)
                    maior = melhorPeso[camada][neuronio] - (melhorPeso[
                        camada][neuronio] / self.otimizacaoPor)
                else:
                    menor = melhorPeso[camada][neuronio] - (melhorPeso[
                        camada][neuronio] / self.otimizacaoPor)
                    maior = melhorPeso[camada][neuronio] + (melhorPeso[
                        camada][neuronio] / self.otimizacaoPor)

                sorteado = randint(int(menor * 1000), int(maior * 1000))
                pesosCamada.append(sorteado / 1000)
            pesos.append(pesosCamada)

        return pesos

    def otimizarRede(self):
        if self.otimizacaoPor == 0:
            self.otimizacaoPor = 1

        resultados = []

        for geracao in range(0, self.geracoes):

            pesos = Otimizar.otimizarPesosAleatorios(self, self.melhorPeso)
            neuronio = RedeNeural(self.rede, self.entradas, pesos)
            resultados.append({'saida': neuronio.iniciar(), 'pesos': pesos})

       
        return Otimizar.melhorRede(self, resultados)


