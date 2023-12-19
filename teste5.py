"""
Faça uma lista de compras com listas 
O usuario deve ter a possobilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de indices inexistentes na lista.
"""

lista = []

import os

while True:
    print('Escolha uma opção:')
    pergunta = input('[I]nserir, [A]pagar, [L]istar: ')
    pergunta_x = pergunta.upper()

    if pergunta_x == 'I':
        os.system('clear')
        inserir = input('O que você deseja inserir? ')
        lista.append(inserir)
        continue

    if pergunta_x == 'A':
        os.system('clear')
        apagar = input('O que você deseja apagar? ')
        try:
            indice = int(apagar)
            del lista[indice]
            print('Você apagou', apagar, 'da lista')
        except IndexError:
            print('Não foi possivel apagar esse indice')
        except TypeError:
            print('Não foi possivel apagar esse indice')
            continue

    if pergunta_x == 'L':
        os.system('clear')
        for numero, item in enumerate(lista):
            print(numero, item)
        continue

    else:
        print('Esse digito não é válido!')


