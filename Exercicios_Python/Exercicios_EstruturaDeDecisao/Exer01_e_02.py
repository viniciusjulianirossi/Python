"""1 - Faça um Programa que peça dois números e imprima o maior deles."""
lista = []

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))

lista.append(num1)
lista.append(num2)


print("O numero maior é entre {} e {} é {}".format(num1,num2, max(lista)))


"""2 -Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo."""


num1 = int(input("Digite um numero: "))
if num1 >= 0:
    print(f"O numero {num1} é Positivo!")
else:
    print(f"O numero {num1} é Negativo!")