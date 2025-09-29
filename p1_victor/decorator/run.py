'''Crie um decorator em Python chamado valida_positivo que verifica se todos os argumentos numéricos de uma função são positivos:

Se todos os argumentos forem válidos, a função deve ser executada normalmente.
Se algum argumento for negativo, deve ser levantado um ValueError.
Use esse decorator em pelo menos duas funções:
raiz_quadrada(x), que retorna a raiz quadrada de x.
divisao(a, b), que retorna o resultado de a / b.
Teste chamando as funções com valores positivos (funciona normalmente) e valores negativos (gera erro).'''
from math import sqrt

def valida_positivo(func):
    def wrapper(*args, **kwargs):
        pass
    return wrapper

def raizquadrada(numero):   
    return sqrt(numero)

def divisão(a, b):
    return a / b