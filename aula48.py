# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
# set_1 = set() # Vazio
# set_1 = {'Lucas', 1, 2, 3} # Com dados
#-----------------------


# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# lista_1 = [1, 2 , 3, 3, 3, 3, 3, 3, 1]
# set_1 = set(lista_1)
# lista_2 = list(set_1)
# print(lista_2)

# set_1 = set('Lucas')
# print(set_1)

# set_1 = {1, 2, 3, 4}
# # print(4 in set_1)
# for numero in set_1:
#     print(numero)
#-------------------------



# Métodos úteis:
# add, update, clear, discard
# set_1 = set()
# set_1.add('lucas')
# set_1.add(1)
# set_1.update(('Ola mundo', 1, 2, 3, 4))
# # set_1.clear()
# set_1.discard('Ola mundo')
# print(set_1)
#---------------------------


# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
# set_1 = {1, 2, 3}
# set_2 = {2, 3, 4}
# set_3 = set_1 | set_2
# set_3 = set_1 & set_2
# set_3 = set_1 - set_2
# set_3 = set_1 ^ set_2
# print(set_3)
#----------------------------


# Exemplo de uso dos sets
letras = set()
while True:
    letra = input('Digite')
    letras.add(letra.lower())

    if 'l' in letras:
        print('Parabens')
        break

    print(letras)
 
    
