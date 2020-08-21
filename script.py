from neural import Treino
from neural import Otimizacao
from neural import MicroInfluencia

def treinar():
    script = Treino()
    return script.treinarRede(rede, intervalorMenor, intervaloMaior, lstEsper, listaEntradas, geracoes)

def otimizar(melhorPeso, escala):
    script = Otimizacao()
    return script.otimizarRede(rede, escala, lstEsper, listaEntradas, geracoes, melhorPeso)

def analisaInfluenciaMicro(melhorPeso):
    script = MicroInfluencia()
    return script.analisarInfluencia(rede, lstEsper, listaEntradas, melhorPeso)

registro = 0
menor = -1
listaEntradas = [[0, 0, 0, 0, 6.2, 5.8, 4.6, 5.9, 0.0, 2, 4, 3], [0, 0, 0, 0, 6.0, 6.2, 5.2, 4.5, 1.0, 2, 4, 3], [0, 0, 0, 0, 7.3, 6.7, 7.1, 7.2, 0.0, 5, 0, 3], [1, 3, 1, 1, 0.0, 0.0, 0.0, 0.0, 1.0, 4, 4, 4], [1, 3, 1, 1, 0.0, 0.0, 0.0, 0.0, 1.0, 5, 2, 5], [0, 0, 0, 0, 7.3, 7.4, 7.6, 6.5, 1.0, 5, 3, 5], [0, 0, 0, 0, 5.8, 6.0, 7.3, 5.1, 1.0, 5, 2, 6], [0, 0, 0, 0, 4.4, 4.8, 4.7, 4.6, 1.0, 3, 4, 4], [0, 0, 0, 0, 6.4, 5.4, 5.0, 5.5, 1.0, 3, 5, 3], [0, 0, 0, 0, 6.9, 7.5, 7.3, 6.0, 0.0, 3, 5, 5], [0, 0, 0, 0, 6.6, 4.4, 4.9, 4.7, 1.0, 4, 2, 4], [0, 0, 0, 0, 6.1, 4.7, 6.5, 5.3, 0.0, 4, 5, 3], [0, 0, 0, 0, 5.5, 5.1, 6.2, 4.7, 1.0, 2, 3, 6], [0, 0, 0, 0, 6.7, 6.5, 7.0, 5.6, 1.0, 7, 5, 3], [0, 0, 0, 0, 5.4, 5.2, 5.0, 5.8, 1.0, 1, 3, 5], [0, 0, 0, 0, 5.3, 4.8, 4.8, 5.3, 0.0, 3, 4, 4], [0, 0, 0, 0, 8.0, 8.4, 10.0, 8.5, 0.0, 10, 6, 2]]
lstEsper = [[0, 0, 0, 10], [0, 0, 0, 10], [0, 0, 10, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 10, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 10], [0, 10, 0, 0], [0, 0, 0, 10], [0, 0, 0, 10], [0, 0, 0, 10], [0, 0, 10, 0], [0, 0, 0, 10], [0, 0, 0, 0], [10, 0, 0, 0]]

intervalorMenor = -10
intervaloMaior = 10
geracoes = 150
rede = [12, 9, 4]


copia = []

def exibir(resultado, lstEsper):
    print('\n\n')
    print('melhr =>', resultado[1])
    print('Esper =>', lstEsper[0])
    print('Saída =>', resultado[0][0]['saida'])
    print('Pesos =>', resultado[0][0]['pesos'])

melhorPeso = [[[-14.74709, '+'], [0.0, '*'], [-26.08216, '/'], [10.96804, '*'], [-1.35728, '*'], [14.19443, '*'], [-18.47998, '*'], [-6.68642, '*'], [12.60589, '+'], [-5.15765, '/'], [-4.43546, '/'], [-21.13065, '/']], [[6.22369, '*'], [6.46873, '-'], [3.59293, '+'], [6.28231, '/'], [6.5496, '+'], [-10.03752, '*'], [4.2411, '-'], [1.12109, '-'], [-112.80502, '/']], [[-10.69215, '/'], [-28.36409, '-'], [3.13731, '*'], [9.00135, '+']]]

registro = 0

while True:

    #resultado = treinar()
    resultado = otimizar(melhorPeso, 100 )
    #resultado = analisaInfluenciaMicro(melhorPeso)

    if menor == -1:
        menor = float(resultado[1])
        melhorPeso = resultado[0][0]['pesos']

    elif float(resultado[1]) < float(menor):
        exibir(resultado, lstEsper)

        menor = float(resultado[1])
        melhorPeso = resultado[0][0]['pesos']

    registro += 1
    print('Tenta => {}\r'.format(registro), end='')


#if registro % 5 == 0:
#    corte += 3
#    if corte > 30:
#        corte = 1
#    

#elif registro % 511 == 0:
#    

#else: