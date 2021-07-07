# Exercício 13

# Determine se um ano é bissexto.
# Anos divisiveis por 4 são bissextos.
# Divisiveis por 100 não são, mas divisiveis por 400 são.

ano = int(input('Digite um ano: '))

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print('É ano bissexto.')
else:
    print('Não é ano bissexto.')
