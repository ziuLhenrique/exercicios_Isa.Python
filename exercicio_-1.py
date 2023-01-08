#-1:Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário
# informe um valor válido.
print(' ')
print('''\033[4;36mDigite uma nota
entre 0 e 10.
''')
valor = 11
while valor > 10 or valor < 0:
    valor = int(input('\033[4;36mDigite uma nota de 0 a 10 por favor: '))

    if valor > 10 or valor < 0:
        print('\033[4;31mNúmero digitado invalido. O digito tem que ser entre 0 e 10')

    else:
        print('\033[4;32mNúmero validado! thanks')
    