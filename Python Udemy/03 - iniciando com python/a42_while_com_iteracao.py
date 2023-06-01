""" atividade:
    *Qual a letra apareceu mais vezes na frase?
"""

frase = 'O Python é uma linguagem de programação ' \
    'Multiparadigma '\
    'Python foi criado por Guido Van Rossum.' 
    
    # .upper() upper deixa uma str toda em Maiusculo

print(frase)
print(frase.count('A')) # o método Count retorna o número de elementos com o valor especificado.

cont = 0
while cont < len(frase):
    letra_atual = frase[cont]
    x_letra_apareceu = frase.count(letra_atual)
    print(letra_atual, x_letra_apareceu)
    cont += 1