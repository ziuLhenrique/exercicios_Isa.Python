#1- Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do 
#seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou 
#diferentes no conteúdo.
print('\033[1;36m-'*60)
string1 = str(input('Digite uma string: ')).strip()
string2 = str(input('Digite outra string: ')).strip()

str1_1 = ''.join(string1).split()
str2_2 = ''.join(string2).split()


str1 = len(string1) - string1.count(' ')
str2 = len(string2) - string2.count(' ')


print('\033[4;33m',string1, len(string1) - string1.count(' '))
print(string2,len(string2) - string2.count(' '))
print(' ')

if str1 == str2:
    print(f'\033[1;36mA string1 \033[4;32m({string1}) \033[1;36mcontem \033[4;32m({str1}) \033[1;36mcaracteres e a string2 \033[4;32m({string2}) \033[1;36mcontem \033[4;32m({str2}) \033[1;36mcaracteres tambem.') 
    print('_'*60)
else:
    print(f'\033[1;36mO comprimento das strings não são iguais a string \033[4;31m({string1}) \033[1;36mcontem \033[4;31m({str1}) \033[1;36mcaracteres e a string \033[4;31m({string2}) \033[1;36mcontem \033[4;31m({str2}).')
    print('_'*60)
if str1_1 == str2_2 :
    print(f'\033[1;36mAs etrings \033[4;32m({str1_1})\033[1;36me a string -> \033[4;32m({str2_2}) \033[1;36msão IGUAIS')
    print('_'*60)
else:
    print(f'\033[1;36mAs strings  \033[4;31m({str1_1}) \033[1;36me a -> \033[4;31m({str2_2}) \033[1;36mpossuem conteúdo diferente não são IGUAIS')
    print('_'*60)