"""
Repetições pt1
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira

"""
condicao = True

while condicao:
#    Repete a coindição até sert verdadeira
    valor = input('Sair ou continuar: ')
    print(f'Voce digitou {valor}')

    if valor == 'sair':
#   Para a execução quando encontra o break
        break# o brak procura o while mais próximo a ele

print('saiu!!!')