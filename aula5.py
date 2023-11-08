adicao = 10 + 10
print('Adição', adicao)

subtracao = 10 - 5
print('Subtração', subtracao)

multiplicacao = 10 * 10
print("Multiplicação", multiplicacao)

divisao = 10 / 2.2  # sempre vai ser float
print('Divisão', divisao)

divisao_inteira = 10 // 2.2
print ('Divisão inteira', divisao_inteira)

exponenciacao = 2 ** 10
print('Exponenciação', exponenciacao)

modulo = 25  % 5  # resto da divisão
print('Módulo', modulo)

print(10 % 8 == 0)
print(16 % 8 == 0)

concatenacao = 'A' + 'B' + 'C'
print(concatenacao)

concatenacao = 'Lucas' + ' ' + 'Cinigalia'
print(concatenacao) 

a_dez_vezes = 'A' * 10
tres_vezes_lucas = 3 * 'Lucas'
print(a_dez_vezes)
print(tres_vezes_lucas)

conta_1 = 1 + 1 ** 5 + 5
print(conta_1)
conta_2 = (1 + 1) ** (5 + 5)
print(conta_2)
conta_3 = (1 + (0.5 + 0.5)) ** (5 + 5)
print(conta_3)
conta_4 = (1 + (0.5 + 0.5)) ** 5 + 5
print(conta_4)

nome = 'Lucas Cinigalia'
altura = 1.80
peso = 70
imc = peso / (altura ** 2)
print(nome)
print(altura)
print(peso)
print(imc)
print(nome, 'tem', altura, 'de altura,', 'pesa', peso, 'quilos e seu IMC é', imc, sep= ' ')

print(nome, 'tem', altura, 'de altura,')
print('pesa', peso, 'quilos e seu IMC é')
print(imc)

linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso:.1f} quilos e seu imc é'
linha_3 = f'{imc:.2f}'
print(linha_1)
print(linha_2)
print(linha_3)

dinheiro = 1364973275.300
dinheiro_1 = f'{dinheiro:,.3f}'
print(dinheiro_1)

a = 'A'
b = 'B'
c = 1.1
string = 'a={} b={} c={:.2f}'
formato = string.format(a, b, c)
print(formato)

nome = input ('Qual o seu nomel? ')
print(f'o seu nome é {nome=}')

numero_1 = input ('Digite um numero, ')                
numero_2 = input ('Digite outro numero, ')
print(f'A soma do primeiro e do segundo numero é: {numero_1 + numero_2}')
# Nesse caso foi feita a concatenação ao inves de fazer a soma, pois estão como string.

numero_1 = int(input('Digite um numero, '))
numero_2 = int(input('Digite outro numero, '))
print(f'A soma do primeiro e do segundo numero é: {numero_1 + numero_2}')
# Nesse caso foi feita a soma, pois foi feita a conversão do tipo para int, porem isso não é o recomendado a se fazer.

numero_1 = input ('Digite um numero, ')                
numero_2 = input ('Digite outro numero, ')
int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)
print(f'A soma do primeiro e do segundo numero é: {int_numero_1 + int_numero_2}')
# Isso seria o recomendado a fazer, pois assim seria possivel fazer a checagem mesmo que o usuario não tenha digitado corretamente.
# Dessa forma o código não vai quebrar no inicio, pois sera possivel digitar letras e numeros.

porta = input('Você quer entrar ou sair? ')
if porta == 'entrar':   print('Você entrou no sistema')
elif porta == 'sair':     print('Você saiu do sistema')