"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""


numero = input('Digite um número inteiro: ')

try:
    numero_inteiro = int(numero)
    numero_resto_0 = numero_inteiro % 2
    if numero_resto_0 == 0: 
        print('Seu número é par!')
    else:
        print('Seu número é impar!')

except:
    print('O que você digitou não é um número inteiro.')
    
    
    
    
    
horario = input('Que horas são? ')

try: 
    horario_int = int(horario)
    if horario_int >= 0 and horario_int <= 11:
        print('Bom dia')
    elif horario_int >= 12 and horario_int <= 17:
        print('Boa tarde')
    elif horario_int >= 18 and horario_int <= 23:
        print('Boa noite')
    else: 
        print('Desculpa, não conheço essa hora')
except:
    print('Digite apenas numeros inteiros')    




nome = input('Qual é o seu primeiro nome? ')
nome_len = len(nome)

if nome_len >= 1:
    if nome_len <= 4:
        print('Seu nome é curto')
    elif nome_len >= 5 and nome_len <= 6:
        print('Seu nome é normal')
    elif nome_len > 6:
        print('Seu nome é muito grande')
else:
    print('Digite pelo menos uma letra')