numeros = [1,2,3,4,5,6]

pares = [num for num in numeros if num% 2 ==0]

impares = [num for num in numeros if not num% 2 ==0]

X_or_O = [ "X" if num%2 ==0 else "0" for num in numeros] 

calc = [num ** 2 for num in numeros]

tabuleiro = [[x for x in range(1,5)] for valor in range(1,3)]


print(calc)
print(pares)
print(impares)
print(tabuleiro)
print(X_or_O)



