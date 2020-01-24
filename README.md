# Aviso
Esse é um projeto experimental apenas para estudos. 

# Como Treinar a rede
Para fazer o treinamento dessa rede, é necessário ter um conjunto de dados de entradas, relacionando com os dados de saídas.

Também é necessário informar a rede com os neurônios que você quer usar. Vamos direto ao ponto.

```Python
# Importe a biblioteca de treino
from neural import Treino

'''Defina um intervalo de randomização. Neste caso, todos os pesos da rede
terão pesos entre -5 e 5'''
intervalorMenor = -5
intervaloMaior = 5

# Defina a rede, nesse caso, ela tem 2 entradas, 2 camadas no meio e 1 saída
rede = [2, 2, 1]

# Vai entrar 2 e 4 na rede
entradas = [2, 4]

# O Resultado esperado é 8
esperado = [8]

# Serão executadas 1000 redes com pesos aleatórios
geracoes = 1000

# Instância do treino
script = Treino(
    rede, intervalorMenor, intervaloMaior, esperado, entradas,
    geracoes)

'''Retorna a melhor rede dentre as 1000. Execute até encontrar o resultado
mais próximo do esperado. Depois teste a rede com outros valores, para
garantir que a rede está funcionando'''
print(script.treinarRede())

```

# Como testar uma rede
```Python
# Importe a biblioteca
from neural import RedeNeural

# Informe os pesos, de acordo com os pesos e a rede usada no treinamento
pesos = [[-6.918, 3.564], [2.09, 3.002], [-0.025]]

# Informe as entradas
entradas = [16, 32]

# Informe a rede, de acordo com os pesos e a rede usada no treinamento
rede = [2, 2, 1]

# Crie uma instância passando a rede, a entrada e os pesos
instancia = RedeNeural(rede, entradas, pesos)

# Exiba a saida associada aos pesos, a rede e as entradas
print(instancia.iniciar())

```

# Como otimizar a rede
Uma vez que a rede está se aproximando dos valores esperados, mesmo com múltiplos testes, nós precisamos otimizar a rede, para deixá-la mais exata. Como fazer isso?

```Python
# Importe a classe otimizar
from neural import Otimizar

# Defina uma rede, use a mesma do treino
rede = [2, 2, 1]

# Defina um resultado esperado, use a mesma do treino
esperado = [8]

# Defina uma entradas, use a mesma do treino
entradas = [2, 4]

'''Defina o melhor peso, após alguns testes no treino, você deve ter obtido
algum peso que funcionou muito bem, use ele.'''
melhorPeso = [[-6.918, 3.564], [2.09, 3.002], [-0.025]]

# Define quantas redes serão testadas de forma aleatória
geracoesOtimizacao = 10000

'''Define a região da otimização, basicamente, se o seu peso do neurônio vale
10, e a sua otimização por esteja em 100, o peso deste neurônio será escolhido
de forma aleatória entre "pesoNeuronio - pesoNeuronio / 100" e
"pesoNeuronio + pesoNeuronio / 100" ou vice versa no caso de número negativo.
Neste caso, o peso aleatório escolhido seria entre 9,9 e 10,1. Se o seu
resultado já está muito bom, mas você pretende otimizar ainda mais, coloque um
número bem mais alto para aumentar a precisão'''
otimizacaoPor = 1000

# Crie uma instância da otimização
instancia = Otimizar(
    rede, esperado, entradas, geracoesOtimizacao, melhorPeso,
    otimizacaoPor)

# Chame o método e ele retornará o melhor peso otimizado desta execução.
print(instancia.otimizarRede())

```
