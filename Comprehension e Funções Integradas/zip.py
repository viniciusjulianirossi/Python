"""
zip() Cria um iteravel(Zip object) que agrega elemento de cada um dois iteraveis passados como entradas em pares

# exemplo

lista1 = [1,2,3]
lista2 = [4,5,6]


zip1 = zip(lista1,lista2 , "abc")

print(zip1)
print(type(zip1))


# Sempre podemos gerar uma lista, tupla, ou dicionario
print(list(zip1))

zip1 = zip(lista1,lista2 , "abc")
print(tuple(zip1))

zip1 = zip(lista1,lista2 , "abc")
print(set(zip1))

zip1 = zip(lista1, lista2,)
print(dict(zip1))

# O zip() utiliza como parametro o menors tamanho em iteravel. Isso significa que se estiver trabalhando com iteraveis de tamanho diferetens, irar parar quando os elementos do menos iteravel acabar
lista3 = [7,8,9,10,11]

zip1= zip(lista1, lista2, lista3)
print(list(zip1))

# Podemos utilziar diferente itervaies como zip

tupla = 1,2,3,4,5

lista= [6,7,8,9,10]

dicionario = {"a": 11, "b" : 12, "c" : 13, "d" :14, "e": 15}

zt = zip(tupla, lista, dicionario.values())

print(list(zt))


# lista de tuplas
lista_tuplas = [(1,2,3), (4,5,6), (6,7,8),(9,10,11)]



print(list(zip(*lista_tuplas)))

"""

# Exemplo mais complexos

prova1 = [80,91,78]
prova2 = [98,89,53]
alunos = ["maria", "pedro", "carla"]

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}

print(final)

# Podemos utilizar o map()

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))

print(dict(final))

