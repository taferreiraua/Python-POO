class Banco:
    def __init__(self):
        self.contas = list()

    def cadastrar(self, conta: Conta):
        self.contas.append(conta)
        
    def procurar_conta(self, numero: str):
        achou = False
        for i, conta in enumerate(self.contas):
            if conta.get_numero() == numero:
                achou = True
                return conta
        if achou is False:
            print('Conta inexistente!')
            
    def creditar(self, numero: str, valor: float):
        conta = self.procurar_conta(numero)
        if conta:
            conta.creditar(valor)
        else:
            print('Conta inexistente!')
        
    def debitar(self, numero: str, valor: float):
        conta = self.procurar_conta(numero)
        if conta:
            conta.debitar(valor)
        else:
            print('Conta inexistente!')
        
    def saldo(self, numero: str):
        conta = self.procurar_conta(numero)
        if conta:
            return conta.get_saldo()
        else:
            print('Conta inexistente!')
        
    def transferir(self, origem: str, destino: str, valor: float):
        conta_origem = self.procurar_conta(origem)
        conta_destino = self.procurar_conta(destino)
        
        if not conta_origem:
            print('Conta origem inexistente!')
        if not conta_destino:
            print('Conta destino inexistente!')
        else:
            conta_origem.debitar(valor)
            conta_destino.creditar(valor)
            

# cadastrando contas no banco e testando os metodos implementados acima
if __name__ == '__main__':
    conta_1 = Conta('24.765-1')
    conta_2 = Conta('21.802-3')
    
    banco = Banco()
    
    banco.cadastrar(conta_1)
    banco.cadastrar(conta_2)
    
    banco.creditar(conta_1.get_numero(), 200)
    
    banco.transferir(conta_1.get_numero(), conta_2.get_numero(), 100)
    
    saldo_conta_1 = banco.saldo(conta_1.get_numero())
    saldo_conta_2 = banco.saldo(conta_2.get_numero())
    
    print(f'Conta 1: {saldo_conta_1}\nConta 2: {saldo_conta_2}')
    
