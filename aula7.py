#   if    /     elif       /   else
#   se    /   se não se    /   se não   
porta = input('Você quer entrar ou sair? ')
if porta == 'entrar':   print('Você entrou no sistema')
elif porta == 'sair':     print('Você saiu do sistema')
else:   print('ERRO, você não digitou nem entrar e nem sair')

condicao1 = True
condicao2 = False
condicao3 = True
condicao4 = False
if condicao1:
    print('Codigo para condição 1')
elif condicao2:
    print('código para condição 2')
elif condicao3:
    print('código para condição 3')
elif condicao4:
    print('código para condição 4')

else:
    print('Nenhuma condição foi satisfeita')

if 10 == 10:
    print('Outro if')


print('fora do if')