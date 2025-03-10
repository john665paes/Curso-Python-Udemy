#Métodos em instâncias de Classes Python

#Usar o exemplo da classe Carro

# OBS:  Hard Coded - Dados fixos foi escrito diretamente no codigo.

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca=marca
        self.modelo = modelo
        self.ano = ano  

    def acelerar(self):
        print(f'{self.modelo} Acelerou, o ano dele é {self.ano} e ainda corre')
    
    def freiar(self):
        print(f'{self.modelo} Freiou, quase saiu da pista')
        

c1 = Carro('wolkswagen', 'fusca', 1969)

c1.acelerar()
c1.freiar()


