"""
Iterável -> str, range, etc(__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador

"""
#  for letyra in texto:

texto = 'John' #iterável
iterador = next(texto) #iterator

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break

""" Isso é exatamente o que o for faz por baixo dos panos"""