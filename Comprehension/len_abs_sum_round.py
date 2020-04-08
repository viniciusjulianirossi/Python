"""
len(), abs(), sum(), round()

# len() retrona o tamanho (ou seja, o numero de itens) de um iteravel.

# só para revisar

print(len("Geek University"))

print(len([1,2,3,5,6]))

print(len((1,2,3,5,6)))

print(len({1,2,3,6,5}))

print(len({"a": 1, "b": 2, "c":3, "d": 4}))

print(len(range(0,10)))

# Por debaixos dos panos, quando utilizamos a função len() o Python faz o seguinte.

# Dunder len
print('Geek University'.__len__())

# abs() retorna o valor absoluto de um numero inteiro ou real. De forma basica, seria o seu valor real sem o sinal , retorna numero positivo

print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))


# sum

recebe como parametro um iteravel, podendo recebe um valor inicial, e retorna a soma total dos elementos, incluido o valor inicial

obs: o valor inicial default = 0

# exemplo sum

print(sum([1,2,3,4,5]))

print(sum([1,2,3,4,5], 5))

print(sum([3.145,5.678]))

print(sum((1,2,3,4,5)))

print(sum({1,2,3,4,5}))

print(sum({"a": 1, "b" : 2 ,"c": 3, "d": 4, "e" : 5}.values()))

# round() retorna um numero arrendondado para n digito de precisão apos a cada decimal. Se a precisao nao for informado o retorna o inteiro mais proximo da entrada

"""

# Exemplo Round()

print(round(10.2))
print(round(10.5))
print(round(10.6))
print(round(1.21212121121,2))
print(round(1.2999999,2))
print(round(1.2999999))














