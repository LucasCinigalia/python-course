"""Calculadora com While"""


while True:
    numero_1 = input("Digite um número: ")
    numero_2 = input("Digite outro número: ")
    operador = input("Digite um operador (+-/*): ")

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0
    
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2) 
        numeros_validos = True
    except:
        numeros_validos = None
        
        if numeros_validos is None:
            print('Um ou ambos os números digitados são inválidos.')
            continue
        
    operadores_validos = '+-/*'
    
    if operador not in operadores_validos:
        print('Operador invalido')
        continue
        
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
        
    if operador == '+':
        print(f'{num_1_float} + {num_2_float} = ', num_1_float + num_2_float)
        
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} = ', num_1_float - num_2_float)
        
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} = ', num_1_float / num_2_float)
        
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} = ', num_1_float * num_2_float)
        
        
    sair = input("Você quer sair? [s]im: ")
    sair= sair.lower()
    sair = sair.startswith('s')
    if sair is True :
        print('Você saiu.')
        break