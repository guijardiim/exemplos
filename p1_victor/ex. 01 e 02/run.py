
'''Implemente um sistema de transporte em Python utilizando classes abstratas:

Crie uma classe abstrata Transporte com um atributo capacidade, um método abstrato mover() e um método concreto info() que exibe a capacidade.
Crie duas subclasses:
Carro, que imprime "O carro está se movendo com até X passageiros".
Bicicleta, que imprime "A bicicleta está se movendo com até X pessoas".
No programa principal, crie objetos das duas subclasses, adicione-os em uma lista e invoque mover() e info() para cada um.'''

from abc import ABC, abstractmethod

class Transporte(ABC):
    
    def __init__(self, capacidade):
        if capacidade < 0:
            raise ValueError('A capacidade não pode ser menor que 0!')
       
        else:
            self.capacidade = capacidade

    @abstractmethod
    def mover(self):
        pass

    def info(self):
        return (f'Capacidade: {self.capacidade}')
    

class Carro(Transporte):
    
    def mover(self):
        return(f'O carro está se movendo com até {self.capacidade} passageiros.')

class Bicicleta(Transporte):
    def mover(self):
        return (f'A bicicleta está se movendo com {self.capacidade} pessoas.')
    
def main():
    lista_objetos = [
                    Carro(capacidade=5),
                    Bicicleta(capacidade=2)
                    ]
     
    for objeto in lista_objetos:
        print(objeto.info())
        print(objeto.mover())

main()
'''carro = Carro(capacidade=5)
bicicleta = Bicicleta(capacidade=2)
carro.mover()
print(bicicleta.mover())'''