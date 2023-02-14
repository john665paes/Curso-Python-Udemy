# Se um valor for maior que o outro deve ser exibido primeiro
# e vice versa, ou se for igual

valor1 = input('Digite um valor: ')
valor2 = input('Digite outro valor: ')

if valor1>valor2:
    print(f'{valor1=} é maior que {valor2=}')
elif valor2>valor1:
    print(f'{valor2=} é maior que {valor1=} ')
else:
    print(f'{valor1=} é igual a {valor2=}')