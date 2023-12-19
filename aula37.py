"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""

# def Print(a, b, c):
    # print('Varias 1')
    # print('Varias 2')
    # print('Varias 3')
    # print('Varias 4')


# def imprimir(a, b, c):
#     print(a, b, c)


# imprimir(1, 2, 3)
# imprimir(4, 5, 6)

def saudacao(nome = 'Sem nome'):
    print(f'Olá, {nome}!')

saudacao('Lucas') 
saudacao('João')
saudacao()