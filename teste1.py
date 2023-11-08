primeiro_valor = input ('Digite um valor: ')
segundo_valor = input('Digite outro número: ')

if primeiro_valor != segundo_valor:     
    print(f'primeiro valor = {primeiro_valor} é diferente do segundo valor = {segundo_valor}')
elif primeiro_valor == segundo_valor:    
    print('primeiro valor é igual ao segundo valor')

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:      
    print('primeiro valor =', primeiro_valor, 'é maior do que segundo valor =', segundo_valor)
elif segundo_valor > primeiro_valor:    
    print('segundo valor =', segundo_valor, 'é maior que o primeiro valor = ', primeiro_valor)


entrar = input('Voce quer entrar ou sair? ')
if entrar == 'entrar':
    print('Você entrou!')
    
nome = input('Qual o seu nome? ')
print('Seja bem vindo,', nome)