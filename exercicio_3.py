#3- Conte os espaços e vogais: Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
#quantos espaços em branco existem na frase.
#quantas vezes aparecem as vogais a, e, i, o, u.

frase = str(input('ESCREVA:->')).lower()
voga1= frase.count('a')
voga2 = frase.count('e') 
voga3 = frase.count('i')
voga4 = frase.count('o')
voga5 = frase.count('u')
espaco = frase.count(' ')

print(f'''A frase tem ({voga1}) letra (a)
A frase tem ({voga2}) letra (e)
A frase tem ({voga3}) letra (i)            
A frase tem ({voga4}) letra (o)  
A frase tem ({voga5}) letra (u)             
A frase {frase} tem {espaco} espaços em branco''')
    



