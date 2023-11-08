"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Lucas'
preco = 1000.97869734
variavel = '%s, o preco é R$%.2 f' % (nome, preco)
print(variavel)