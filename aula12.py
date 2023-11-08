#Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True
print(not False) # True
print(not True) # False


#Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 
#  L u c a s
# -5-4-3-2-1
nome = 'Lucas'
print('Lc' in nome)

nome = input('Qual o seu nome? ')
encontrar = input('Qual ou quais letras deseja encontrar? ')
if encontrar in nome:
    print(f'{encontrar} está no {nome}')
if encontrar not in nome:
    print(f'{encontrar} não está no {nome}')
