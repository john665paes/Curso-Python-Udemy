# Operadores in(entre) e not in(Não está entre)
# Strings são iteráveis(que se repetem, é possivél navegar item por item)
#  0  1  2  3 
#  j  o  h  n
# -4 -3 -2 -1

nome = 'john' 
# pegando as letras da variável pelo indice
print(nome[0],nome[-1])
print(nome[1], nome[-2])
print(nome[2], nome[-3])
print(nome[3], nome[-4])

print(10 * '-')

print('Checando com "in" e "not in" se os dados estão na variável')

print(10 * '-')
print('jo' in nome) #verdadeiro
print('z' in nome) #falso
print(10 * '-')
print('jo' not in nome) #Falso
print('z' not in nome) #Verdadeiro

print(10 * '-')

palavra = input('Digite uma palavra: ')

encontrarP = input('O que deseja encontrar na palavra: ')

if encontrarP in palavra:
    print(f'{encontrarP} está em {palavra}')
else:
    print(f'{encontrarP} não está em {palavra}')
