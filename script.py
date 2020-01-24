from random import randint
from neural import RedeNeural


def obterMelhorResultado(resultados, esperado):
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


def randomize(rede, intervalorMenor, intervaloMaior):
    pesos = []

    for camada in rede:

        pesosCamada = []
        for neuronio in range(0, camada):

            sorteado = randint(intervalorMenor * 1000, intervaloMaior * 1000)
            sorteado = sorteado / 1000

            pesosCamada.append(sorteado)

        pesos.append(pesosCamada)
    return pesos


def microRandomizacao(rede, melhorPeso):

    pesos = []

    for camada in range(0, len(rede)):

        pesosCamada = []
        for neuronio in range(0, rede[camada]):

            if melhorPeso[camada][neuronio] < 0:
                menor = melhorPeso[camada][neuronio] + (
                    melhorPeso[camada][neuronio] / 2)
                maior = melhorPeso[camada][neuronio] - (melhorPeso[
                    camada][neuronio] / 2)
            else:
                menor = melhorPeso[camada][neuronio] - (melhorPeso[
                    camada][neuronio] / 2)
                maior = melhorPeso[camada][neuronio] + (melhorPeso[
                    camada][neuronio] / 2)

            sorteado = randint(int(menor * 1000), int(maior * 1000))
            pesosCamada.append(sorteado / 1000)
        pesos.append(pesosCamada)

    return pesos


def treinamento(rede, intervalorMenor, intervaloMaior, esperado, entradas, geracoes):

    resultados = []

    for geracao in range(0, geracoes):
        pesos = randomize(rede, intervalorMenor, intervaloMaior)
        n = RedeNeural(rede, entradas, pesos)
        resultados.append(n.iniciar())

    print('melhor resultado:', obterMelhorResultado(resultados, esperado))


def otimizacao(rede, intervalorMenor, intervaloMaior, esperado, entradas, geracoes, melhorPeso):

    resultados = []

    for geracao in range(0, geracoes):
        pesos = microRandomizacao(rede, melhorPeso)
        n = RedeNeural(rede, entradas, pesos)
        resultados.append(n.iniciar())

    print(
        'melhor resultado otimizado:',
        obterMelhorResultado(resultados, esperado))


intervalorMenor = -8
intervaloMaior = 8

rede = [2, 2, 1]
esperado = [8]
entradas = [2, 4]
geracoes = 1000

# Treine a rede até chegar ao melhor peso
'''
reinamento(
    rede,
    intervalorMenor,
    intervaloMaior,
    esperado,
    entradas,
    geracoes)
'''
# Otimize os resultados

melhorPeso = [[-6.556, 3.89], [2.121, 3.149], [-0.025]]
geracoesOtimizacao = 100000
otimizacao(
    rede, intervalorMenor, intervaloMaior, esperado,
    entradas, geracoesOtimizacao, melhorPeso)

'''clientes vendas  faturamento
    2      4         8
    4      8         16
    8      16        x = 33.03
    16     32        x = 66.06
'''
