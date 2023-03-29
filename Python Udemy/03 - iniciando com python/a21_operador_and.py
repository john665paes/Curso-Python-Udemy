
# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor



# Avaliação de curto circuito
print(True and False and True) #Na prinmeira opção FALSA a condição para a execução
print(True and 0 and True) 


entrada = input('[E]ntrar | [S]air: ')
if entrada == 'E':
    print('Digite a senha!')
    senha_digitada = input('Senha: ') 
elif entrada == 'S':
    print('Sair do login!')

senha_permitida = '123'
# essa condição valia todas as opções
if entrada =='E' and senha_digitada == senha_permitida:
    print('Login feito com sucesso!')
else:
    print('Login incorreto!')    