# Exercicios 06

c = float(input("Digite a temperatura Celsius para ser convertida em Fahrenheit: "))

f = (c*(9/5))+32

print(f"A temperatura {c} em Celsius convertida para Fahrenheit é {f}")
print()

# Exercicios 07

f = float(input("Digite a temperatura Fahrenheit  para ser convertida em Celsius: "))

c = 5*(f-32)/9

print(f"A temperatura {f} em Fahrenheit convertida para Celsius é {c}")
print()


# Exercicios 08

k = float(input("Digte a temperatura em Kelvin para ser convertida em Celsius: "))

c = k - 273.15

print("A temperatura {} em Kelvin convertida para Celsius é {:.2f}.".format(k,c))
print()


# Exercicios 09

c = float(input("Digte a temperatura Celsius em para ser convertida em Kelvin: "))

k = c + 273.15

print("A temperatura {} em Kelvin convertida para Celsius é {:.2f}.".format(c,k))
print()

# Exercicios 10

km_hora = float(input("Digite a velocidade em km/h (quilometors por hora) para ser convertida em m/s (metros por segundos): "))

metros_segundo = km_hora/3.6

print("A velocidade {:.0f}km/h convertida para metros por segundo são {:.2f}m/s.".format(
    km_hora, metros_segundo))

