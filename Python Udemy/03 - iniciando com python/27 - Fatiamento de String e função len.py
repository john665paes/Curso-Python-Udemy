"""
Fatiamento de String e função len
 012345678
 olá mundo
-987654321

Fatiamento [i:f:p] [::]
obs.: A função len() retorna a qtd de caracteres da string
"""

var = 'olá mundo'
# Fatiei a variavel e idiquei um indice de 
# busca com final desejado
print(var[-4:8])

# fatiando com indic e passo 
print(var[0:9:4])

# com indicies negativos
# com o passo negativo ele começa a printar de 
# traz para frente
print(var[-1: -10:-1])