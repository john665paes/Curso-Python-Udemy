""" atividade:
    *Qual a letra apareceu mais vezes na frase?
"""

frase = 'O Python é uma linguagem de programação ' \
    'Multiparadigma '\
    'Python foi criado por Guido Van Rossum.' 
    
    # .upper() upper deixa uma str toda em Maiusculo

print(frase)
print(frase.count('P')) # o método Count retorna o número de elementos com o valor especificado.

cont = 0
qtd_apareceu_mais_x = 0
letra_apareceu_mais_x = ''
while cont < len(frase):
    letra_atual = frase[cont]
    quantas_x_letra_apareceu_atual = frase.count(letra_atual)

    if letra_atual == ' ':
        cont += 1
        continue

    if qtd_apareceu_mais_x < quantas_x_letra_apareceu_atual:
        qtd_apareceu_mais_x = quantas_x_letra_apareceu_atual
        letra_apareceu_mais_x = letra_atual

    cont += 1

print(f'A letra que apareceu mais vezes foi '
      f'"{letra_apareceu_mais_x}" que apareceu '
      f'{qtd_apareceu_mais_x}x')