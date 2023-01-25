from SistemaBancario import Conta


class Conta:
    def __init__(self, numero: str):
        self.__numero = numero
        self.__saldo = 0
        
    def creditar(self, valor: float):
        self.__saldo += valor
        
    def debitar(self, valor: float):
        self.__saldo -= valor
        
    def get_numero(self):
        return self.__numero
    
    def set_numero(self, numero: str):
        self.__numero = numero
        
    def get_saldo(self):
        return self.__saldo
        
    def set_saldo(self, saldo: float):
        self.__saldo = saldo
        
        
# Criando uma conta
if __name__ == '__main__':
    conta_exemplo = Conta('27.098-5')
    conta_exemplo.creditar(280)
    conta_exemplo.debitar(80)
    print(conta_exemplo.get_saldo())
