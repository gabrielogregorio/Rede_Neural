from neural import RedeNeural

pesos = [[[1, '+'], [-1, '/']], [[1, '*'], [-3, '-'], [-9, '-']], [[1, '-'], [4, '/']]]

rede = [2, 3, 2]
entradas = [2, 4]

s = RedeNeural(rede, entradas, pesos)
print('saida', s.reden())
print('entrada :',entradas)