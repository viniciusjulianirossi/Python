"""
Levantanod os proprios erros com o raise

raise -> Lança exceções 

OBS: o raise não é uma função. É uma palavra reservada, assim como def ou qualquer outra em Python. 

Para simplificar, pense no raise como sendo util para que possamos criar nossas proprias exceções e mensagens de erro.

A forma gerar de utilização é:

raise TipoErro("Mensagem do Erro")

# Exemplo Real

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError("Texto precisa ser uma string")
    if type(cor) is not str:
        raise TypeError("Cor precisa ser uma string")
    print(f"o texto {texto} será impresso na cor {cor}")


colore("Geeek" , 4)  

# Exemplo refatorado

def colore(texto, cor):
    cores = ("verde", "amarelo" , "azul" , "branco")
    
    if type(texto) is not str:
        raise TypeError("Texto precisa ser uma string")
    if type(cor) is not str:
        raise TypeError("Cor precisa ser uma string")
    if cor not in cores:
        raise ValueError(f"A cor não esta na lista de cores : {cores}")
    print(f"o texto {texto} será impresso na cor {cor}")


colore("Geeek" , "vermelho")  

obs: o raise, assim como o return, finaliza a função. Ou seja, nada aposi o raise é executado

"""

# Exemplo Real

def colore(texto, cor):
    cores = ("verde", "amarelo" , "azul" , "branco")
    
    if type(texto) is not str:
        raise TypeError("Texto precisa ser uma string")
    if type(cor) is not str:
        raise TypeError("Cor precisa ser uma string")
    if cor not in cores:
        raise ValueError(f"A cor não esta na lista de cores : {cores}")
    print(f"o texto {texto} será impresso na cor {cor}")


colore("Geeek" , "vermelho")  


