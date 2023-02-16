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
print(f'{var:. >10}')
print(f'{var: <10}')
print(f'{var: ^9}')
print(f'{1000.65125445:.3f}')