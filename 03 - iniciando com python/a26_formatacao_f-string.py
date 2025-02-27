"""
Formatação básica de string
s - string
d - int
f - float
.<número de digitos>f
x ou X - Hexadecimal
(Caractere)(><^)(Quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""

var = 'a b c'
print(f'{var}')
# Posso preecher espaços no pad com 
# algum caracter ou com espaço
print(f'{var:º>10}')
print(f'{var:&<10}')
print(f'{var:-^13}')#Para centralizar o print
print(f'{1000.65125445:.3f}')

# o Sinal de positivo descrito na formatção 
# indica que o numero deverá ser exibido 
# como positivo ou negativo
print(f'{1000.65125445:+,.2f}')

#Hexadecimal 
print(f'O exadecimal de 1500 é {1500:08X}')