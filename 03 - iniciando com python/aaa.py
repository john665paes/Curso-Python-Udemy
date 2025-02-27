r,d =input("").split()
resistencia, dano, ataque = int(r), int(d), 0

while True:
    resistencia = resistencia-dano
    ataque += 1
    dano -= 1
    if resistencia<1:
        print(f"Oponente derrotado com {ataque} ataques")
        break
    elif(dano<=0):
        print("f")
        break
    


