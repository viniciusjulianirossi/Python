"""

Com o map, fazemos mapeamento de valores para função
"""

import math

def area(r):
    """ Calcula a areas de um circuilo com o raio 'R' """
    return math.pi * (math.pow(r,2))

print(area(2))
print(area(5.3))

raios = [2, 5 ,7.1, 0.3, 10, 44]

#Forma comum

areas  = []
for r in raios:
    areas.append((area(r)))
   
# forma 2 - Map
#map é uma função que recebe dois parametros: 1 é a função, o 2º é um iteravel

areas = map(area, raios)
print(type(areas))
print(list(areas))
print(list(areas)) # ** Zerado

# forma 3 - Map com Lambda
print(list(map((lambda r: math.pi *(r**2)), raios)))

#OBS: Apos utilizar a função map() depois da primeira utilização do resultado, ele zera.

# Para fixar - Map
# temos dados interaveis:
# dados: a1, a2, ....an
# Temos uma função:
# função: f(x)
# utilizamos a função map(f, dados) onde map ira 'mapear' cada elemento dos dados e aplciar a função
# o Map Object: f(a1), f(a2), f(...), f(an)

# MAIS UM EXEMPLO

cidades = [('Berlim' , 29), ("Cairo", 36), ("Buenos Aires", 19),("Lons Angels", 26), ("Tokio", 28),("Nova York", 28),("Londres", 22)]

print(cidades)

# F = 9/5 * C + 32

c_para_f = lambda dado: (dado[0], (9/5) * dado[1]+ 32)

print(list(map(c_para_f, cidades)))