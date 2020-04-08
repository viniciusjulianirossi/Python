"""Erros mais comuns em Python.

É importante prestar atenção e aprnder a ler as saidas de erros geradas pela execucao no nosso código.

Os erros mais comuns:

1- Systaxerrros - Ocorre quando o Python encontra um erro de sintaxe. Ou seja, voce escreveu algo que o Python não reconhece como parte da linguaguem

Exemplos SyntaxError

a) def funcao:
    print("Geek University")

b) None = 1

c) return


2- NameErros Ocorre quando uma variavel ou funcao não foi definida

# Exemplos de NameErros

a) print(geek)

b) geek()

c) a = 18

    if a < 10:
        msg = "é maior que 10"
    print(msg)


3- TypeError - Ocorre quando uma função/operação é aplicada a um tipo erro

# Exemplos de TypeErrros

a) print(len(5))

b) print("geek" + [])

4 - IndexErros - Ocorre  quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando um indice invalido

Exemplo de IndexError

a) lista = ["Geek"]

print(lista[1])
print(lista[0][10])

5- ValueError- Ocorre quando uma função/operação built-in(integrada) recebe um argumento com o tipo correto mas o valor inapropriado

# Exemplo de ValueError

a) print(int("Geek"))

b) print(float("Geek"))

6 - KeyError - Ocorre quando tentamos acessar um dicionaior com uma chave que não existe

Exemplo KeyError

a) dic = {}
print(dic["geek"])

b) 
dic = {"python" : "university"}
print(dic["geek"])


7 - AttributeError - Ocorre quando uma variavel não tem um atributo/função.

Exemplo de AttributeError

a)tupla = (11,2,31,4)
print(tupla.sort())

8- IndextationErro - Ocorre quando não respeitamos a indentação do Python (4 espaços)

# Exemplo de IndentationError:

a) def nova():
print("Geek")

b) for i in range(10):
i + 1


Obs: Exception e Errros são sinonimos na programação.

Obs: Importante ler e prestar atenção na saida de erro.
"""



