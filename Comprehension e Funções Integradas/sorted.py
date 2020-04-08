"""
Sorted

Obs: Não confunda, apensar do nome, com a função sort() que ja estudamos em listas. O sort() só funciona em listas.

Podemos utilizar o sorted() com qualquer iteravel.

Como o proprio nome diz: sorted() serve para ordernar elementos.

O sorted() sempre retorna uma lista com os elementos do iteravel ordenados

# Exemplo

numeros = (6,1,8,2)
print(numeros)

print(sorted(numeros)) # Ordena do menors para o maior

print(numeros)

# adicionando parametros ao sorted()

numeros = [6,1,8,2,6]
print(numeros)


print(tuple(sorted(numeros)))
print(set(sorted(numeros)))

print(sorted(numeros, reverse=True)) # do maior para o menor

# podemos utilziar o sorted() para coisas mais complexas


usuarios = [
    {"username": "samuel", "tweets": ["eu adoro bolos", "eu adoro pizza"]},
    {"username": "carla", "tweets": ["eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["eugosto de cachorros", "Vou sair hoje"]},
    {"username": "gat", "tweets": []}
]

print(usuarios)

# Ordenando por username - Ordem alfabetcica
print(sorted(usuarios, key=lambda usuario: usuario["username"]))

#Ordenando pelo numeros de Tweets do menor para o maior
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))

#Ordenando pelo numeros de Tweets do maior pelo menor
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"]),reverse=True))

"""

# Ultimo exemplo

musicas = [
    {"titulo": "Thunderstruck", "tocou" : 3},
    {"titulo": "Dead Skin Mask", "tocou" : 2},
    {"titulo": "Back in Black", "tocou" : 4},
    {"titulo": "Too old to rock'in'roll,too ynoung to die", "tocou" : 32},
    ]

# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica["tocou"]))

# Ordena do mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica["tocou"],reverse=True))

# Ordena musica com menos letra

print(sorted(musicas, key=lambda str: len(str["titulo"])))

# Ordena musica com mais letra
print(sorted(musicas, key=lambda str: len(str["titulo"]), reverse=True))
