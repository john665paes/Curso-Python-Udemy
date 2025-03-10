# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))

#Metodo __init__()

class   Pessoa:
    #o Self representa o proprio objeto
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade


p1 = Pessoa('Johnatan', 'Paes', 32)  # Instancia da classe pessoa

print(p1.nome, p1.sobrenome, p1.idade, "anos")