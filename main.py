from Client import Client
from Account import Account

class Main:
    pass

## c1 = Client("Brenda Barbosa Silva", "(61) 7277-4561")
c1 = Client()
c1.set_info("Brenda Barbosa Silva", "(61) 7277-4561")
account1 = Account(c1.get_name(), 6565, 0)


print(f"{account1.holder}\nNumero: {account1.number}\nSaldo: {account1.balance}")