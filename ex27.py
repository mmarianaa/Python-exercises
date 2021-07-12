# Exercício 27

# Calcule o fatorial de um numero N

x = int(input('Digite um numero: '))
fat = 1
while x > 0:
    fat = fat * x
    x = x - 1
print('O fatorial é %d' % fat)
