# Faça um programa que calcule e mostre a média aritmética de N notas
print(' ')
print('\033[1;36m°'*25,'MÉDIA ARITMÉTICA DE  NOTAS','°'*25)

quantidade = int(input('Digite a quantidade de notas que deseja calcular: '))
cont = soma = 0
while cont < quantidade:
    notas = float(input(f'Digite a ({cont+1}) nota: '))
    cont += 1
    soma += notas
    divizor = soma / cont

print(f'\033[4;32mSua média é de {divizor:.2f} ->  End, thanks!')

