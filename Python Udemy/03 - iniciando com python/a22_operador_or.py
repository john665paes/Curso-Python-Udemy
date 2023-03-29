# Operador Lógico
# and (e) or(ou) not(não)
# or - Qualquer condição verdadeira valida toda expressão
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

# Avaliação de curto circuito
print(True or 1 or True)

# teste direto na linha
senha = input('digite a senha: ') or 'sem senha'

print(senha)



# programa de teste
entrada = input('[E]ntra | [S]air: ')

senha_esperada = '123'

if entrada == 'E' or entrada =='e':
    senha = input('Senha: ')
    if senha==senha_esperada:
        print('Login feito com sucesso!')
    else:
        print('senha incorreta')
elif entrada=='S' or entrada=='s':
    print('Logout feito com sucesso')





