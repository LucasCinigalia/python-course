nome = 'Lucas'
altura = 1.80
peso = 70
imc = peso / altura ** 2
print(nome, 'tem', altura, 'de altura,')
print('pesa', peso, 'quilos e seu IMC é')
print(imc)

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso:.2f} quilos e seu imc é'
linha_3 = f'{imc: .2f}'
print(linha_1)
print(linha_2)
print(linha_3)
 

a = 'AAA'
b = 'B'
c = 1.5
string = 'a={0}, b{1}, c{2:.3f} '
formato = string.format(a, b, c)

print(formato)

string = 'b={1}, a={0}, c={2}, b={1}, c={2:.3f} '
formato = string.format(a, b, c)

print(formato)
