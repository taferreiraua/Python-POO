from SistemaBancario import Conta


class ContaEspecial(Conta):
    def __init__(self, numero: str):
        super().__init__(numero)
        self.__bonus = 0

    def renderBonus(self):
        super().creditar(self.__bonus)
        self.__bonus = 0

    def creditar(self, valor: float):
        self.__bonus = self.__bonus + (valor * 0.01)
        super().creditar(valor)
        

# Pergunta: Qual o saldo da conta?
if __name__ == '__main__':
    conta = Conta("31.345-X")
    
    conta.creditar(20)

    especial = ContaEspecial("31.567-X")
    
    conta.creditar(20) # Até aqui, o objeto "conta" possui saldo 40

    conta = especial # Aqui "conta" passa a ser a conta "31.567-X", com saldo 0
    
    conta.creditar(20) # Resposta: a conta possui saldo 20!
    
