'''Utilizando o sistema de transporte do Exercício 1, crie testes unitários em Python com pytest:

Teste se um objeto Carro(5) possui capacidade igual a 5.
Teste se o método mover() de Carro retorna a string correta.
Teste se o método mover() de Bicicleta retorna a string correta.
Crie também um teste de falha proposital para verificar se a criação de um Carro com capacidade negativa (Carro(-3)) 
gera um erro ou comportamento esperado.'''


from run import Carro, Bicicleta
import pytest

@pytest.fixture
def objeto_carro():
    return Carro(capacidade=5)

@pytest.fixture
def objeto_bicicleta():
    return Bicicleta(capacidade=2)

def test_capacidade_carro(objeto_carro):
    assert objeto_carro.capacidade == 5

def test_mover_carro(objeto_carro):
    assert objeto_carro.mover() == 'O carro está se movendo com até 5 passageiros.'

def test_capacidade_bicicleta(objeto_bicicleta):
    assert objeto_bicicleta.capacidade == 2

def test_mover_bicicleta(objeto_bicicleta):
    assert objeto_bicicleta.mover() == 'A bicicleta está se movendo com 2 pessoas.'

def test_capacidade_negativa():
    with pytest.raises (ValueError):
        Carro(-3)
