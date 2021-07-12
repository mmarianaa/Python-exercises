# Exercício 15

# Código modificado do exercício passado (exercício 14) para que no caso
# de não tiver excesso na pesca apresentar a mensagem: Não há excesso

peso = float(input('Digite o peso da pesca: '))

excesso = multa = 0

if (peso > 50):
    excesso = peso - 50
    multa = excesso * 4
    print('A pesca teve excesso de %d e a multa no valor R$ %.2f' %
          (excesso, multa))
else:
    excesso = 0
    print('Não há excesso')
