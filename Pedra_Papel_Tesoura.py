from random import choice
from colorama import Fore
from colorama import init


def linhas():
    print("--" * 29)

def mostrar_escolhas(usuario, escolha): 
    if usuario == 1:
        usuario = "Pedra"
        print(f"| Voce escolheu {usuario} e o computador escolheu {escolha}.")
    elif usuario == 2:
        usuario = "Papel"
        print(f"| Voce escolheu {usuario} e o computador escolheu {escolha}.")
    elif usuario == 3:
        usuario = "Tesoura"
        print(f"| Voce escolheu {usuario} e o computador escolheu {escolha}.")
   


jogada = [{1 : "Pedra" }, {2 : "Papel"}, { 3 : "Tesoura"}]

linhas()
print("|              Jogo Pedra, Papel e Tesoura               |")
linhas()
print("| Escolha uma das opções abaixo:                         | \n| 1 - Pedra                                              | \n| 2 - Papel                                              |  \n| 3 - Tesoura                                            |")
linhas()


sair = str
usuario = str
pontos_pessoa = 0
pontos_pc = 0
empates = 0

while sair != "S":

    while usuario is str or usuario > 3:
        try:
            usuario = int(input("| Digite o numero desejavel: 1, 2 ou 3: "))
            linhas()
        except:
            print(Fore.RED + "| Digite somente o numero!" , Fore.RESET)            
            linhas()
        

    computador = choice(jogada)
    escolha = str(list(computador.values())).strip("[]'")
    chave = int(str(list(computador.keys())).strip("[]'"))

    if usuario == chave:
        mostrar_escolhas(usuario, escolha)
        print(Fore.MAGENTA + "| Deu empate!", Fore.RESET)              
        empates += 1
        

    elif usuario == 1 and chave == 2:
        mostrar_escolhas(usuario, escolha)
        print(Fore.RED + "| Voce perdeu", Fore.RESET)                  
        pontos_pc += 1

        
    elif usuario == 1 and chave == 3:
        mostrar_escolhas(usuario, escolha)
        print(Fore.GREEN + "| Voce ganhou!",Fore.RESET)   
        pontos_pessoa += 1
            
        
    elif usuario == 2 and chave == 3:
        mostrar_escolhas(usuario, escolha)
        print(Fore.RED + "| Voce perdeu!",Fore.RESET)   
        pontos_pc += 1
                
        
    elif usuario == 2 and chave == 1:
        mostrar_escolhas(usuario, escolha)
        print(Fore.GREEN + "| Voce ganhou!",Fore.RESET)   
        pontos_pessoa += 1
                       

    elif usuario == 3 and chave == 1:
        mostrar_escolhas(usuario, escolha)
        print(Fore.RED + "| Voce perdeu!",Fore.RESET)   
        pontos_pc += 1
        

    elif usuario == 3 and chave == 2:
        mostrar_escolhas(usuario, escolha)
        print(Fore.GREEN + "| Voce ganhou!",Fore.WHITE)
        pontos_pessoa += 1
        
   
    
    sair = input("| Digite S para sair ou enter para continuar: ").upper() 
    
    linhas()
    usuario = str



print(Fore.BLUE + "--" * 29)
print(Fore.BLUE + "|                    Resultado Final                     |")
print(Fore.BLUE +f"| Total que o usuario ganhou {pontos_pessoa}                           |")
print(Fore.BLUE +f"| Total que o computador ganhou {pontos_pc}                        |")
print(Fore.BLUE +
      f"| Total de empates {empates}                                     |")
print(Fore.BLUE + "--" * 29)





    
    
















