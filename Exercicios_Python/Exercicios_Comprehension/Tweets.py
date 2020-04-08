#Verificar a quantidade de usuarios inativos, quantidade de tweets, numero de usuarios ativos, medias de tweets por usuario ativos,
from functools import reduce

usuarios = [
    {"usuername": "samuel", "tweets": ["eu adoro bolos", "eu adoro pizza", "gosto de gato" ,"Amanha é sexta"]},
    {"usuername": "carla", "tweets": ["eu amo meu gato" , "Adoro peixe"]},
    {"usuername": "jeff", "tweets": ["Sextou!!" , "Jorge e matheus"]},
    {"usuername": "bob123", "tweets": []},
    {"usuername": "doggo", "tweets": ["eugosto de cachorros", "Vou sair hoje"]},
    {"usuername": "gat", "tweets": []},
    {"usuername": "henrique", "tweets": ["eu adoro bolos", "eu adoro pastel"]},
    {"usuername": "Hugo", "tweets": ["eu amo meu gato"]},
    {"usuername": "Keff", "tweets": []},
    {"usuername": "bob456", "tweets": []},
    {"usuername": "diggo", "tweets": ["eugosto de cachorros", "Naõ vou sair hoje", "Quintou" , "Amanha é feriado" ,"Python melhor linguagem"]},
    {"usuername": "gateel", "tweets": []}
]

# Total de inativos
inativos = list(filter(lambda x: len(x["tweets"]) == 0, usuarios))
print(f"Quantidade de usuarios inativo são {len(inativos)}!" if len(inativos) > 1 else f'Quantidade de usuarios inativo é {len(inativos)}!')

# Total de tweets
def numeros_de_tweets(x):
    lista = []
    for num in x:        
        lista.append(len(num['tweets']))
    return lista

total_de_tweets = reduce(lambda x, y: x+y , numeros_de_tweets(usuarios))

print(f"Total de tweets foi de {total_de_tweets}!")
 

# Medias de tweets por usuario ativos

total_usuario_ativo = len(usuarios) - len(inativos)
print(f'Total de usuario ativos são de {total_usuario_ativo}!')

# Medias de tweets por usuarios ativos:

media_por_usuario = total_de_tweets / total_usuario_ativo
print("Média de tweets por usuario ativo é de {:.2f}!".format(media_por_usuario))













