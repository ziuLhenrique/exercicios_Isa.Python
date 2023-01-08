#4- Valide e corrija o número de telefone. Faça um programa que leia um número de telefone,
#e corrija o número no caso deste conter somente 7 dígitos, adicionando o '9' na frente.
#O usuário pode informar o número com ou sem o traço separador.
#Valida e corrige número de telefone
#Telefone: 461-0133
#O telefone possui 9 dígitos. Vou acrescentar o dígito nove na frente.
#Telefone corrigido sem formatação: 34610133
#Telefone corrigido com formatação: 93461-0133

phone = str(input('Número de telefone por favor: '))
n = len(phone)


if n == 8:
    print('\033[1;32mVALIDA E CORRIGE NÚMERO DE TELEFONE.\033[1;39m')
    print(f'telefone: {phone[:4]}-{phone[5:]}')
    print('O telefone possui 9 digitos. Vou acrecentar o digito 9 na frente.')
    
    if phone == phone:
        print(f'Telefone corrigido sem formatação: {phone}')

    if n == 8 :
        print(f'Telefone corrigido com formatação: 9{phone[:4]}-{phone[4:]} ')

elif n > 9:
    print('\033[1;31merro\033[1;39m')
    print('Digite sem o traço por favor, até atualizarmos o software')
else:
    print(phone)

#if len(phone) == 8:
    #print()