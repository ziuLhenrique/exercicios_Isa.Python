# Faça um programa que leia cinco números e mostre o maior e o menor deles.
print(' ')
print('\033[4;32m~'*25,'MAIOR Ou menor?','~'*25)
cont = 0
maior = menor = 0
while cont < 5:
    num = int(input(f'Digite o {cont+1} número: '))
    cont += 1
    if cont == 1:
        maior = menor = num
    
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
print(f'\033[4;39mO número maior é ({maior}) e o menor é ({menor})')
print('FIM')
