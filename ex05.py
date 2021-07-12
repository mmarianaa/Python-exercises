# Exercício 05

# Solicite o preço de uma mercadoria e o percentual de desconto.
# Exiba o valor do desconto e o preço a pagar

mercadoria = float(input('Insira o preço de mercadoria: '))
desconto = float(input('Insira o valor do desconto: '))

calculo_desconto = mercadoria * desconto / 100
valor_final = mercadoria - calculo_desconto

print('O valor do desconto é de R$', calculo_desconto)
print('Valor a pagar é de R$', valor_final)
