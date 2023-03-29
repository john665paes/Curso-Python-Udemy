# Formantando usando o metodo format
a = '@@a'
b = 'b'
c = 1.1
string = 'a={} b={} c={}'
# buscando no format por indices
# por indices consigo dizer a posição que quero
string2 = 'a={0} b={2} c={1}'



formato = string.format(a, b, c)
formato2 = string2.format(a, b, c)
print(formato)
print(formato2)