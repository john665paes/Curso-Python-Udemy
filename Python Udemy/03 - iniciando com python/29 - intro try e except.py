""" 
Introdução ao try/except

try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar

Obs: Com try/except consigo capturar um erro na exceção
"""

num_str = input("Informe um numero, vou dobrar esse valor: ")
# '.isdigit' chega se o usuário digitrou apenas numeros
print(num_str.isdigit())
print('O ".isdigit" identificou erro, não possui apenas numeros')

# try e except
# testo meu verificador de numero e se foi digitado
# STR o try pula para a mensagem do exept e não
# executa o resto do cod e estoura erro na tela
try:
    print('STR: ', num_str)
    num_float = float(num_str)
    print('Float: ', num_float)
    print(f'O dobro de {num_str} é {num_float * 2:.2f}')
    print('O "try" não identificou erro')
except:
    print('In not a number papitoo')