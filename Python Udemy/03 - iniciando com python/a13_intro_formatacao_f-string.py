# INTRO Formatação as f-string
nome = 'John'
alt = 1.75
peso = 85
imc = peso / (alt*alt)

# inseri o "f" antes da str e foi formatado o texto com variaveis 
linha1 = f'{nome} tem {alt} de altura'
print(linha1)

linha2= f'Pesa {peso} e seu IMC é {imc:.2f}'
print(linha2)