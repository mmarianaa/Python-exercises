# Exercício 6

# Calcule o tempo de uma viagem de carro.
# Pergunte a distância a percorrer e a velocidade média
# esperada para a viagem.

distancia = float(input('Digite a distância a ser percorrida (km): '))
velocidade = float(input('Digite a velocidade média (Km/h): '))

print('A viagem durará', (distancia/velocidade), 'horas')
