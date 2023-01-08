#-3: Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor
#  a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
cont = aluno = aluno1 = aluno2 = 0
while True:
    nota = float(input(f'Digite a ({cont+1}) nota: '))
    cont += 1
    aluno1 += nota / 4
    aluno2 += nota / 4
    
    if cont == 4:
        print(f'Nota do ({aluno+2}) aluno.')
        cont = 0
        aluno += 1
    
    if cont == 4 and aluno1 >= 7.0 or aluno2 >= 7.0:
        break
print(f'A media do primeiro aluno é {aluno1}')

        
    
    





































'''
aluno_1 = 0
aluno_2 = 0
cont = 0
while True:
    nota = float(input(f'Digite a ({cont+1}) nota: '))
    cont += 1
    aluno_1 += nota
    
    
    if cont == 4 or cont == 8 or cont == 12 or cont == 16 or cont == 20 or cont == 24 or cont == 28 or cont == 32 or cont == 36 or cont == 40:
        print('_'*40)
    if cont == 4:
        d1 = aluno_1 / 4 
        print(d1)
        
    if cont == 8:
        d2 =  s2 / 4
        print(s2)
'''

    