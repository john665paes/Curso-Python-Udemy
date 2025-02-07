nome = 'John'
alt = 1.77
peso = 79
imc = peso / (alt*alt)

print(f'{nome} tem {alt} de altura')
print(f'Pesa {peso} e seu IMC é {imc:.2f}')

if imc < 18.5:
    print(f'{nome} Menor que 18,5: abaixo do peso')
elif 18.5 <= imc < 25:
    print(f'{nome} Entre 18,5 e 24,9: peso normal')
elif 25 <= imc < 30:
    print(f'{nome} Entre 25 e 29,9: sobrepeso')
elif 30 <= imc < 40:
    print(f'{nome} Igual ou acima de 30: obesidade')
else:
    print(f'{nome} esta com obesidade morbida')
