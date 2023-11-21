"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavra = 'arroz'
letra_acertadas = ''
número_de_tentativas = 0

while True:
    letra = input('Digite uma letra: ')
    número_de_tentativas += 1

    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra in palavra:
        letra_acertadas += letra

    palavra_formada = ''
    for letra_secreta in palavra:
        if letra_secreta in letra_acertadas:
            palavra_formada += letra_secreta
        else: 
            palavra_formada += '*'

    print('palavra formada: ', palavra_formada)

    if palavra_formada == palavra:
        print('Você ganhou!')
        print('Tentativas: ', número_de_tentativas)

    letra_acertadas = ''
    número_de_tentativas = 0