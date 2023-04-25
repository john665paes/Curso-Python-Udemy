"""
Iterando strings com while
"""
nome = 'Johnatan Paes'

nomeTam = len(nome)
print(nome)
print(nomeTam, 'caracteres')
cont = 0
while cont < int(nomeTam):
    novo_nome = '*'
    while cont < int(nomeTam):
        # Essa parte fiz para testar como seria a impresão 
        # print(cont)
        # print(nome[cont], cont)
        novo_nome += nome[cont] + '*'
        cont +=1

    print(novo_nome)
