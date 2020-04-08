"""
reversed

obs: Não confuda com a função reversed() que estudamos nas listas.

a função reserve() só funciona em listas.

Já a função reversed() funciona com qualquer iteravel.

Sua função é inverter o iteravel. 

A função reversed() retonra um iteraval chamado list reverse iterator

"""

# Exemplo

lista = [1, 2, 3, 4, 5]

res= reversed(lista)

print(res)
print(type(res))

# Podemos converter o leemento retorna para uma lista, tupla ou conjunto

# Lista
print(list(reversed(lista)))

# Tupla
print(tuple(reversed(lista)))

#Conjunto (set) em conjunto não é definido a ordem dos elementos
print(set(reversed(lista)))

# Podemos iterar sobre o reversed

for letra in reversed("Geek University"):
    print(letra, end="")

print()

# podemos fazer o mesmo sem o uso do for

print("".join(list(reversed("Geek University"))))

# ja vimos como fazer com isso maisfacil com o slice de string
print("Geek University"[::-1])

#Podemos tambem utilizar o reversed() para fazer um loop for reverso

for n in reversed(range(0,10)):
    print(n)

# utilizando o proprio range()

for n in range(9,0,-1):
    print(n)
