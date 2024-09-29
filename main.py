from Client import Client
from Account import Account

class Main:
    pass

c1 = Client()
account1 = Account()

c1.set_info('Brenda Barbosa', '1195741-5216')
account1.set_info(c1.get_name(), c1.get_phone_number())

account1.deposit(1000.00)
account1.withdrawal(500.00)
print(account1.bankStatement())