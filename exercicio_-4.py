# Faça um programa que, dado um conjunto de N números, determine o menor valor,o maior valor e a soma dos valores.
print(' ')
print('\033[4;32m--> Para parar o digito de números digite -->\033[1;31m[0]\033[4;32m<--')
num = 1
cont = soma = maior = menor = 0
while num > 0:
    num = int(input('Digite o número por favor: '))
    
    if num == 0:
        break
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
            
print(f'\033[4;36mO  maior valor é {maior} e o menor é {menor} e o total somado deu {soma}')
    




    


