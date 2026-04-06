class Conta:
    def __init__(self,titular, id, saldo):
        self.titular = titular
        self.id = id
        self.saldo = saldo
    def Deposito(self, valor):
        if valor <= 0:
            return "Seu depósito precisa ser maior que 0"
        else:
            self.saldo += valor
            return f'Olá {self.titular}, seu depósito de R${valor}, foi efetuado, seu novo saldo é de R${self.saldo}'
    def Saque(self, valor):
        if valor > self.saldo:
            return "Saldo insuficiente"
        else:
           self.saldo -= valor
           return f'Olá {self.titular}, seu saque de R${valor}, foi efetuado, seu novo saldo é de R${self.saldo}'


x1 = Conta("Gustavo", 1000,  5000)
print(x1.Deposito(500))
          
x2 = Conta("Jorge", 2000, 14000)
print(x2.Saque(5000))