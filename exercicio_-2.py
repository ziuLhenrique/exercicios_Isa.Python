#-2: Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são: 
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
#  Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
#  e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

lista = ['Telefonou para a vítima?:', 'Esteve no local do crime?:', 'Mora perto da vitima?:', 'Devia para a vitima?:', 'Já trabalhou para a vítima?:']
cont = perg1 = perg2 = 0
for item in lista:
    pergunta  = ' '
    while pergunta not in "SN":
        pergunta = str(input(f'{item}')).upper()
        cont += 1
        if cont == 2 and pergunta == 'S':
            break
print('suspeita')
        
   
