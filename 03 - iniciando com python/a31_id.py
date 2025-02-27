#  A identidade do valor que está na memória
# o id busca o elemento na memoria do sistema o 
v1 = 'a'
print(id(v1))

v2 = 'ab'
print(id(v2),'espaço na memoria')

""" 
Flag(bandeira - Marca um local)
None = não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""
condicao = True

# Variavel sem valor
passou_if = None # Usando para saber se a variavel tem ou não um valor

if condicao:
    # A variavel só tera valor TRUE se entrar na condição
    passou_if = True
    print('Passou no if')
else:
    print('não passou')
# O is ou is not checa se é alguma coisa
print(passou_if, passou_if is None) 
print(passou_if, passou_if is not None)

if passou_if is None:
    print('Não passou no if')

