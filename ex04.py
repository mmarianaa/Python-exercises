# Exercício 04

# Faça um programa que calcule o aumento de um salário.
# Ele deve solicitar o valor do salário e a porcentagem
# do aumento. Exiba o valor do aumento e do novo salário.

salario = int(input('Digite o valor do salario: '))
aumento = int(input('Digite o valor do aumento em porcentagem: '))

calculo_aumento = salario * aumento / 100
calculo_salario = salario + calculo_aumento

print('O valor do aumento é de R$', calculo_aumento)
print('O novo salário é de R$', calculo_salario)
