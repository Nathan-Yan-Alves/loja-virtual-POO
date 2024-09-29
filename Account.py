class Account:
    def __init__(self, holder = "", number = ""):
        self._balance = 0.0
        self._holder = holder
        self._number = number

    def set_info(self, holder, number):
        self._holder = holder
        self._number = number

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, balance):
        if(balance < 0):
            print("Saldo não pode ser negativo!")
        else:
            self._balance = balance

    def withdrawal(self, value):
        if(value <= self._balance):
            self._balance -= value
            print("Saque efetuado com sucesso!")
        else:
            print("Saldo insuficiente!")
    
    def deposit(self, value):
        if(value > 0):
            self._balance += value
            print("Depósito realizado com sucesso!")
        else:
            print("Valor do depósito inválido!")
    
    def bankStatement(self):
        return f"*Yan Bank*\nHolder: {self._holder}\nBalance: {self._balance}"