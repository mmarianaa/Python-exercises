# Exercício 09

# Escreva um programa que pergunte a quantidade de km percorridos
# por um carro alugado pelo usuário, assim como a quantidade de dias
# pelos quais o carro foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

km_percorridos = float(input('Digite a quantidade de km percorridos: '))
dias_alugado = float(input('Digite a quantidade de dias que alugou o carro: '))

print('O valor total a pagar é de: R$',
      (60 * dias_alugado + 0.15 * km_percorridos))
