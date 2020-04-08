"""
Filter

Serve para filtrar dados de uma determinada coleção

valores = 1, 2, 3, 4, 5, 6

media = sum(valores) / len(valores)

print(media)

# Biblioteca para trabalhar com dados estatisticos
import statistics

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
# Calculando a media dos dados utilizando a função mean()

media = statistics.mean(dados)
print(f"A media é {media}")
# Assim como a função map(), a filter() recebe dois parametros, sendo uma função e um iteravel.

res = filter(lambda x: x > media, dados)
print(type(res))
print(list(res))


paises = ["", "Argentina", "", "Brasil" , "Chile" , "", "Colombia", "" , "Equador", "", "", "Vezenuela"]



print(list(res))

paises = ["", "Argentina", "", "Brasil" , "Chile" , "", "Colombia", "" , "Equador", "", "", "Vezenuela"]


# res = filter(None, paises)
res = filter(lambda pais:  len(pais) != 0, paises)

print(list(res))

"""

# A diferença entre Map e filter é:
# na Map() recebe dois parametros, uma função e um iteravel e retorna um objeto mapenaod a função para cada elemento iteravel
# filter() recebeis parametros, uma função e um iteravel e retorna um objeto filtrando os elementos de acordo com a função.

#Exemplo mais complexo:

usuarios = [
    {"usuername": "samuel", "tweets": ["eu adoro bolos", "eu adoro pizza"]},
    {"usuername": "carla", "tweets": ["eu amo meu gato"]},
    {"usuername": "jeff", "tweets": []},
    {"usuername": "bob123", "tweets": []},
    {"usuername": "doggo", "tweets": ["eugosto de cachorros", "Vou sair hoje"]},
    {"usuername": "gat", "tweets": []}
    ]


# Filtrar os usuarios que estão inativos no Twitter

print(type(usuarios))

print(usuarios[0])
print(usuarios[0]["tweets"])
print(len(usuarios[0]["tweets"]))



# Forma 1
# inativo = list(filter(lambda u: len(u["tweets"]) == 0, usuarios))

# Forma 2

inativo = filter(lambda u: not u["tweets"], usuarios)
print(list(inativo))


# como combinar filter() e map()

nomes = ["Vanessa", "Ana" , "Maria"]
# devemos criar uma lista contendo " sua instrutruta é  + nome da instrutura, desde que cada nome tenha menos de 5 caracteres


lista = list(map(lambda nome: f"Sua instrutorau é {nome}", filter(lambda x: len(x) < 5, nomes)))

print(lista)

