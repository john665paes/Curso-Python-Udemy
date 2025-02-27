"""
Laços Internos
while (enquanto) dentro de while
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> O cod nunca tem fim

"""

qtd_linhas = 5
qtd_Colunas = 5

linha = 1

while linha <= qtd_linhas:
    col = 1

    while col <=qtd_Colunas:
        print(f'{linha=} {col=}')
        col += 1

    linha += 1

print('Acabou.')
