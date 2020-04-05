"""
Reduce

OBS: A partir do Python 3+ a função  reduce() não é mais umna função integrada (built-in) Agora temos que importar e utilizar esta função a parti do modulo 'functools'


Guido van Rossum: Utilize a função reduce() se vc realmente precisa dela. Em todo o caso, 99% das vezes um loop for é mais legivel.

Para entederu o reduce()

Imagine que vc tem uma coleção de dados 

dados = [a1, a2, a3 ..... an]

e voce tem uma função que recebe dois parametros:

def função(x, y):
    return x * y

Assim como map() e filter(), a funçao reduce() recebe dois parametros: a função e o iteravel.

A função reduce(), funciona da seguida forma:
    Passo 1: res1 = f(a1, a2) # aplica a função nos dois primeiros elementos da coleção e guarda o resultado.
    Passo 2: res2 = f(res1, a3) # aplica a função  passando o resultadd anterior + o 3º elemento e guarda o resultado.

    Isso é repetido até o final
    passo 3: res3 = f(res2, a4)

Ou seja, em cada passo ela aplica a função passando como primeiro argumento o resultado da aplicação anterior. No final reduce() irá retorna o resultado final.

Alternativamente, poderiamos ver a função reduce() como:
funcao(funcao(funcao(a1,a2), a3), a4)....).an)

"""
# Como funciona na pratica, vamos utilziar a função reduce() para multiplicar todos os numeros de uma lista

from functools import reduce

dados = [2, 3, 4 , 5, 7, 9, 23, 29, 30, 30]

# Para utilizar a função reduce() precisamos de uma função que receba dois parametros

multi = lambda x, y : x *y

res = reduce(multi, dados)
print(res)


#Utilizando o Loop Form

res = 1
for n in dados:
    res = res * n
print(res)    
