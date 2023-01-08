#Programa nome ao contrario em maiúsculas. Faça um prograque permita ao usuário
# digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando
#somente letras maiúsculas.Dica lembre-se que ao informar onome o usuário pode digitar 
#letras maiúsculas ou minúsculas.

print('='*40)
print('PROGRAMA NOME AO CONTRARIO EM MAIÚSCULA')
print('='*40)
nome =  str(input('Digite se nome: ')).upper()
name = nome[::-1]
for n in name:
    print(n)
print('THE END')
