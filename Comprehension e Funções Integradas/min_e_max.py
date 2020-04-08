"""
Min e Max

max() Retorna o maior valor em um iteravel ou o maior de dois ou mais elemento, nao importa se é uma lista, tupla,set e dicionario


lista= [1,8,4,99,34,129]
print(max(lista))

tupla = (1,8,4,99,34,129)
print(max(tupla))

conjunto_set = {1,8,4,99,34,129}
print(max(conjunto_set))

dicionario= {"a": 1,"b": 8, "c": 4, "d": 99, "e": 34, "f" :129}
print(max(dicionario)) # chave

dicionario= {"a": 1,"b": 8, "c": 4, "d": 99, "e": 34, "f" :129}
print(max(dicionario.values())) # valor


# Faça um programa que receba dois valores do usuario e mostre o maior

val1 = int(input("Digite o primeiro valor: "))
val2 = int(input("Digite o o segundo valor: "))

print(max(val1, val2))

print(max("a", "ab" , "abc"))

print(max("a", "c", "b", 'g'))

print(max("Geek University"))

min()Retorna o menor valor em um iteravel ou o menor de dois ou mais elemento, nao importa se é uma lista, tupla,set e dicionario

# outros exemplo

nomes =["Arya", "Samsom","Dora" ,"Tim", "Ollivander" ]

print(max(nomes)) # tim
print(min(nomes)) # arya

print(max(nomes, key=lambda nome: len(nome))) #Ollivander
print(min(nomes, key=lambda nome: len(nome)))# Tim

"""


musicas = [
    {"titulo": "Thunderstruck", "tocou" : 3},
    {"titulo": "Dead Skin Mask", "tocou" : 2},
    {"titulo": "Back in Black", "tocou" : 4},
    {"titulo": "Too old to rock'in'roll,too ynoung to die", "tocou" : 32},
    ]


print(max(musicas, key=lambda musica: musica["tocou"]))
print(min(musicas, key=lambda musica: musica["tocou"]))



#DESAFIO!! Imprima somente o titulo da musica mais e menos tocada

print(max(musicas, key=lambda musica: musica["tocou"])["titulo"])
print(min(musicas, key=lambda musica: musica["tocou"])["titulo"])

#DESAFIO ! como encontra a musica mais tocada e a menos tocada sem usar max(), min() e lambda?


max = 0
for musica in musicas:
    if musica["tocou"] > max:
        max = musica["tocou"]

for musica in musicas:
    if musica["tocou"] ==max:
        print(musica["titulo"])  

min = 99999
for musica in musicas:
    if musica["tocou"] < min:
        min = musica["tocou"]

for musica in musicas:
    if musica["tocou"] == min:
        print(musica["titulo"])  
