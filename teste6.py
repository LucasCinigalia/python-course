# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

# Crie uma função fala se um número é par ou impar.
# Retorne se o número é par ou impar.

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicacao = multiplicar(3, 6, 7, 8, 2, 9, 23)
print(multiplicacao)


def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'O seu numero é um numero par.'
    return f'O seu numero é um numero impar.'

print(par_impar(3275839))
print(par_impar(23))
print(par_impar(12))
print(par_impar(98))