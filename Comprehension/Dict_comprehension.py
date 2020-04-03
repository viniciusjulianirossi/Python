chaves = "ABCDEF"
numeros = [1,2,3,4,5,6]

dicionario = {chaves[i]: numeros[i] for i in range(0,6)}

print(dicionario)

quadrado = {chave: valor ** 2 for chave, valor in dicionario.items()}
cubica = {chave: valor ** 3 for chave, valor in dicionario.items()}

print(quadrado)
print(cubica)