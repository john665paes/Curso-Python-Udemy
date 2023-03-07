"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = int(input('Digite um numero inteiro: '))
IMPAR = numero%2

if numero< 0:
    print(f'O número {numero} não é um numero inteiro')

elif IMPAR:
    print(f'o  número {numero} é ímpar')
    print(f'O resto da divisão de {numero} por 2 é {IMPAR}')
else:
    print(f'O número {numero} é par')