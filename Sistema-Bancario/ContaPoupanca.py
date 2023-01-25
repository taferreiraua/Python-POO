class ContaPoupanca(Conta):
    def __init__(self, numero: str):
        super().__init__(numero)
        
    def render_juros(self, taxa):
        self.creditar(self.get_saldo() * taxa)


# transformando uma conta existente em uma conta poupanca
if __name__ == '__main__':
    conta_exemplo = Conta('21-907-1')
    conta_exemplo = ContaPoupanca(conta_exemplo.get_numero())
    
    conta_exemplo.creditar(1000)
    conta_exemplo.debitar(100)
    
    print(conta_exemplo.get_saldo())
    
    if isinstance(conta_exemplo, ContaPoupanca):
        conta_exemplo.render_juros(0.01)
    
    print(conta_exemplo.get_saldo())
