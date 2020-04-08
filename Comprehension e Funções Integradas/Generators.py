"""
Tuple comprehension...porque elas se chama generators


nomes = ["Carlos", "Camila", "Carla", "Cassioano", "Cristina", "vanessa"]
print(any([nome[0] == 'C' for nome in nomes]))

# Poderiamos ter feito utilizando Generators

nomes = ["Carlos", "Camila", "Carla", "Cassioano", "Cristina", "vanessa"]

print(any(nome[0] == "C" for nome in nomes))

# List Comprehension

res = [nome[0] == "C" for nome in nomes]
print(type(res))
print(res)


res = (nome[0] == "C" for nome in nomes)
print(type(res))
print(res)

# Qual é a utilizada de gestziseof -> retorna a quantidade de bytes em memoria do elemento passado como parametro
from sys import getsizeof # pega o tamanho de

print(getsizeof("Geek"))
print(getsizeof("university"))
print(getsizeof(9))
print(getsizeof(91))
print(getsizeof(912312312321))
print(getsize(True))

from sys import getsizeof

# Gerando uma lista de numero com list comprehension

# List
list_comp = getsizeof([x * 10 for x in range(1000)])


# Set
set_comp = getsizeof({x * 10 for x in range(1000)})


# Dict
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# Generator
gen = getsizeof(x * 10 for x in range(1000))

print("Para fazer a mesma tarefa gastamos em memoria")
print(f"Lista {list_comp} bytes")
print(f"Set {set_comp} bytes")
print(f"Dicionario {dict_comp} bytes")
print(f"Generator {gen} bytes")
"""



# EU posso iterar no Generator Expression? Sim!

gen = (x * 10 for x in range(1000))
print(gen)


for num in gen:
    print(num)





