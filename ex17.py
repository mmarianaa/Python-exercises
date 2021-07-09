# Exercício 17

# Faça um Programa que leia três números e mostre o maior e o menor deles.

x = int(input('Digite o primeiro numero: '))
y = int(input('Digite o segundo numero: '))
z = int(input('Digite o terceiro numero: '))

# Achando o maior numero
maior = x

if (y > maior):
    maior = x
if (z > maior):
    maior = z

print('O maior numero é: ', maior)

# Achando o menor numero
menor = x

if (y < menor):
    menor = x
if (z < menor):
    menor = z

print('O menor numero é: ', menor)
