# Tipos INT e FLOAT

# ->TIPO INT 
# NÃO POSSUI VIRGULA  
print(10)
print(-10)
print(0, end="\n\n")

#  ->TIPO FLOAT
# POSSUI PONTO FLUTUANTE, CASAS DEPOIS DA VIRGULA

print(1.1, 1.2, sep=", ")
print(0.1, 0.2)
print(10.1, -10.3, end="\n\n")

# A FUNÇÃO type MOSTRA O TIPO QUE O PYTHO INFERIU AO VALOR

print(type(10))
print(type('10'))
print(type(10.0), type(-10.0), type(0.0))