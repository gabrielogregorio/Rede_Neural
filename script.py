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

listaEntradas = [[12, 14, 28],[-12, 5, 8],[-1, 5, 1]]
lstEsper = [[459.1999999999998],[120.0],[145.59999999999997]]

intervalorMenor = -10
intervaloMaior = 10
geracoes = 200
rede = [5, 6, 3, 1]
menor = -1
registro = 0

copia = []
melhorPeso = [[[-9.97976, '/'], [-9.88599, '/'], [-5.13934, '/'], [6.83292, '+'], [-8.87351, '/']], [[-10.04444, '-'], [-5.00752, '+'], [8.86596, '/'], [-6.93024, '/'], [3.04694, '*'], [-7.12338, '-']], [[-2.03406, '-'], [-3.96055, '+'], [5.84042, '/']], [[0.9754, '-']]]

while True:
    #resultado = treinar()
    #resultado = otimizar(melhorPeso, 99 )
    resultado = analisaInfluenciaMicro(melhorPeso)

    if menor == -1:
        menor = resultado[1]
        melhorPeso = resultado[0][0]['pesos']

    if float(resultado[1]) < float(menor):
        print(resultado, resultado[1])
        menor = float(resultado[1])
        melhorPeso = resultado[0][0]['pesos']

    registro += 1
    print('{}\r'.format(registro),end='')
