# Exercicios 11

metros_segundo = float(input(
    "Digite a velocidade em m/s (metros por segundos) para ser convertida em km/h (quilometros por hora) : "))

km_hora =  metros_segundo * 3.6

print("A velocidade {:.2f}m/s convertida para km são {:.0f}km/h.".format(metros_segundo,km_hora))
print() 

# Exercicios 12

milhas = float(input("Digite a distancia em milhas para converter em quilometros: "))

quilometros = 1.61 * milhas
print(f"{milhas} Milhas convertida para quilometros sao {quilometros}.")
print()
