from math import sqrt
from random import randint, uniform, choice

class RedeNeural():
    def __init__(self, rede, entradas, pesos):
        self.entradas = entradas
        self.pesos = pesos
        self.rede = rede

    def neuronio(peso, entradas):
        '''Neurônio individual'''
        soma = 0

        for entrada in entradas:
            soma = soma + entrada

        tipo = peso[1]
        multiplicador = peso[0]

        if tipo == "+":
            resultado = soma + multiplicador

        if tipo == "-":
            resultado = soma - multiplicador

        elif tipo == "*":
            resultado = soma * multiplicador

        elif tipo == "/":
            if soma == 0:
                soma = 0.1

            if multiplicador == 0:
                multiplicador = 0.1

            resultado = soma / multiplicador

        return resultado

    def reden(self):
        '''Montador da rede neural'''

        for camada in range(0, len(self.rede)):
            novasEntradas = []

            for neuronio in range(0, self.rede[camada]):
                novasEntradas.append(

                    RedeNeural.neuronio(
                        self.pesos[camada][neuronio],
                        self.entradas))

            self.entradas = novasEntradas

        return self.entradas

class Treino():

    def __init__(self):
        pass

    def melhorRede(self, conjuntoResultados, listaEsperado):
        melhorResultadoPeso = []

        for geracao in range(len(conjuntoResultados)):
            if melhorResultadoPeso == []:
                somaMelhor = 0
                melhorResultadoPeso = conjuntoResultados[geracao]

                for entrada in range(len(conjuntoResultados[geracao])):
                    for esperado in range(len(listaEsperado[geracao])):
                        s = listaEsperado[geracao]
                        l = conjuntoResultados[geracao][entrada]['saida']

                        for p in range(len(l)):
                            x = l[p]
                            y = s[p]

                            if x > y:
                                somaMelhor = somaMelhor + (x - y)
                                continue

                            somaMelhor = somaMelhor + (y - x)
            else:

                somaMelhor = 0
                for entrada in range(len(conjuntoResultados[geracao])):
                    for esperado in range(len(listaEsperado[geracao])):
                        s = listaEsperado[geracao]
                        l = conjuntoResultados[geracao][entrada]['saida']

                        for p in range(len(l)):
                            x = l[p]
                            y = s[p]

                            if x > y:
                                somaMelhor = somaMelhor + (x - y)
                                continue

                            somaMelhor = somaMelhor + (y - x)

                if somaMelhor > somaTestes:
                    melhorResultadoPeso = conjuntoResultados[geracao]
                    somaMelhor = somaTestes

            return [melhorResultadoPeso,somaMelhor]

    def gerarPesosAleatorios(self, rede, intervalorMenor, intervaloMaior):
        pesos = []

        possiveis = ["+","-","*","/"]

        for camada in rede:

            pesosCamada = []
            for neuronio in range(0, camada):

                sorteado = randint(intervalorMenor, intervaloMaior)
                tipo = choice(possiveis)

                pesosCamada.append([sorteado, tipo])

            pesos.append(pesosCamada)

        return pesos

    def treinarRede(self, rede, intervalorMenor, intervaloMaior, listaEsperado, listaEntradas, geracoes):

        resultados = []

        for geracao in range(geracoes):

            pesos = Treino.gerarPesosAleatorios(self, rede, intervalorMenor, intervaloMaior)
    
            tmp = []

            for entradas in listaEntradas:
                n = RedeNeural(rede, entradas, pesos)
                tmp.append({'saida': n.reden(), 'pesos': pesos})

            resultados.append(tmp)
 
        return Treino.melhorRede(self, resultados, listaEsperado)

class Otimizacao():

    def __init__(self):
        pass


    def melhorRede(self, conjuntoResultados, listaEsperado):
        melhorResultadoPeso = []

        for geracao in range(len(conjuntoResultados)):
            if melhorResultadoPeso == []:
                somaMelhor = 0
                melhorResultadoPeso = conjuntoResultados[geracao]

                for entrada in range(len(conjuntoResultados[geracao])):
                    for esperado in range(len(listaEsperado[geracao])):
                        s = listaEsperado[geracao]
                        l = conjuntoResultados[geracao][entrada]['saida']

                        for p in range(len(l)):
                            x = l[p]
                            y = s[p]

                            if x > y:
                                somaMelhor = somaMelhor + (x - y)
                                continue

                            somaMelhor = somaMelhor + (y - x)
            else:

                somaMelhor = 0
                for entrada in range(len(conjuntoResultados[geracao])):
                    for esperado in range(len(listaEsperado[geracao])):
                        s = listaEsperado[geracao]
                        l = conjuntoResultados[geracao][entrada]['saida']

                        for p in range(len(l)):
                            x = l[p]
                            y = s[p]

                            if x > y:
                                somaMelhor = somaMelhor + (x - y)
                                continue

                            somaMelhor = somaMelhor + (y - x)

                if somaMelhor > somaTestes:
                    melhorResultadoPeso = conjuntoResultados[geracao]
                    somaMelhor = somaTestes

            return [melhorResultadoPeso,somaMelhor]

    def microPesosAleatorios(self, rede, escala, melhorPeso):
        possiveis = ["+","-","*","/"]

        pesos = []

        for camada in range(len(rede)):

            pesosCamada = []
            for neuronio in range(0, rede[camada]):
                #print(melhorPeso[camada][neuronio])
                maior = melhorPeso[camada][neuronio][0] - melhorPeso[camada][neuronio][0] / escala
                menor = melhorPeso[camada][neuronio][0] + melhorPeso[camada][neuronio][0] / escala
                if menor > maior:
                    a = maior
                    maior = menor
                    menor = a

                sorteado = round(uniform(float(menor), float(maior)),5)
                tipo = choice(possiveis)

                pesosCamada.append([sorteado, tipo])

            pesos.append(pesosCamada)

        return pesos

    def otimizarRede(self, rede, escala, listaEsperado, listaEntradas, geracoes, melhorPeso):

        resultados = []

        for geracao in range(geracoes):

            pesos = Otimizacao.microPesosAleatorios(self, rede, escala, melhorPeso)
    
            tmp = []

            for entradas in listaEntradas:
                n = RedeNeural(rede, entradas, pesos)
                tmp.append({'saida': n.reden(), 'pesos': pesos})

            resultados.append(tmp)
 
        return Otimizacao.melhorRede(self, resultados, listaEsperado)

class MicroInfluencia():

    def __init__(self):
        pass

    def melhorRede(self, conjuntoResultados, listaEsperado):
        melhorResultadoPeso = []

        for geracao in range(len(conjuntoResultados)):
            if melhorResultadoPeso == []:
                somaMelhor = 0
                melhorResultadoPeso = conjuntoResultados[geracao]

                for entrada in range(len(conjuntoResultados[geracao])):
                    for esperado in range(len(listaEsperado[geracao])):
                        s = listaEsperado[geracao]
                        l = conjuntoResultados[geracao][entrada]['saida']

                        for p in range(len(l)):
                            x = l[p]
                            y = s[p]

                            if x > y:
                                somaMelhor = somaMelhor + (x - y)
                                continue

                            somaMelhor = somaMelhor + (y - x)
            else:

                somaMelhor = 0
                for entrada in range(len(conjuntoResultados[geracao])):
                    for esperado in range(len(listaEsperado[geracao])):
                        s = listaEsperado[geracao]
                        l = conjuntoResultados[geracao][entrada]['saida']

                        for p in range(len(l)):
                            x = l[p]
                            y = s[p]

                            if x > y:
                                somaMelhor = somaMelhor + (x - y)
                                continue

                            somaMelhor = somaMelhor + (y - x)

                if somaMelhor > somaTestes:
                    melhorResultadoPeso = conjuntoResultados[geracao]
                    somaMelhor = somaTestes

            return [melhorResultadoPeso,somaMelhor]

    def analisarInfluencia(self, rede, listaEsperado, listaEntradas, melhorPeso):

        resultados = []
        for camada in range(len(melhorPeso)):
            for neuronio in range(len(melhorPeso[camada])):
         
                numero = str(melhorPeso[camada][neuronio][0])
                copia = melhorPeso[camada][neuronio][0]

                for nchar in range(len(numero)):
                    copiaOriginal = str(numero)

                    for valor in range(0,10):
                        if numero[nchar] == '.' or numero[nchar] == '-':
                            break

                        numero = numero[:nchar] + str(valor) + numero[nchar + 1:]

                        melhorPeso[camada][neuronio][0] = float(numero)

                        tmp = []
                        for entradas in listaEntradas:
                            n = RedeNeural(rede, entradas, melhorPeso)
                            tmp.append({'saida': n.reden(), 'pesos': melhorPeso})

                        resultados.append(tmp)

                    numero = copiaOriginal

                melhorPeso[camada][neuronio][0] = float(copia)

        return MicroInfluencia.melhorRede(self, resultados, listaEsperado)
