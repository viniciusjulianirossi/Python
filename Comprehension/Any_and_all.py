"""
Any e All

all() retorna True se todos os elementos do iteravel são verdadeiros ou ainda se o iteravel está vazio
"""

# Exemplo all()
print(all([0,1,2,3,4,3])) # Todos os numeros são verdadeiro: False
print(all([1,2,3,4,3])) # Todos os numeros são verdadeiro: True
print(all([])) #Todos os numeros são verdadeiro: True
print(all({1,2,3,4,3})) # Todos os numeros são verdadeiro: True

nomes = ["Carlos", "Camila", "Carla", "Cassioano" , "Cristina" ]

print(all([nome[0] == 'C' for nome in nomes]))


print(all([letra for letra in "eio" if letra in "aeiou"])) # Obs: um iteravel vazio convertido é False, mas o all() entende como True


print(all([num for num in [4,2,10,6,8] if num%2 == 0]))


"""
Any, Retorna True se qualquer elemento do iteraval for verdadeiro, se o iteravel estiver vazio, retorna True

Any- "algum"
"""

print(any([1,2,3,4,5,6])) # True
print(any([0,0,0,0,0])) # False
print(any([0,0,0,0,1])) # True

nomes = ["Carlos", "Camila", "Carla", "Cassioano", "Cristina" , "vanessa"]

print(any([nome[0] == 'a' for nome in nomes ]))
print(any([num for num in [4,2,10,6,8,9] if num %2 == 0]))
