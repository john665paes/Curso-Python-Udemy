"""
Iterando strings com while

*ITERAVEL - Um objeto capaz de retornar seus membros um de cada vez.
"""
nome = 'Johnatan Paes'

nomeTam = len(nome)
print(nome)
print(nomeTam, 'caracteres')
cont = 0
novo_nome = '*'

while cont < nomeTam:
    
        # Essa parte fiz para testar como seria a impressão 
        # print(cont)
        # print(nome[cont], cont)
        
        # AQUI SERÁ INSERIDO A ITERAÇÃO NA NOVA VARIAVEL MAIS UMA '*'
        novo_nome += nome[cont] + '*'
        cont +=1
        print(novo_nome) #para testar inserindo cada iteração

print(novo_nome)
