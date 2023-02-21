class Bank:
    clients = {}

    def get_balance(self, client_name: str) -> str:
        if client_name not in self.clients:
            return "ERROR"
        return str(self.clients[client_name])

    def deposit(self, client_name: str, amount_money: int) -> None:
        if client_name not in self.clients:
            self.clients[client_name] = amount_money
        else:
            self.clients[client_name] += amount_money

    def transfer(self, client_from: str, client_to: str, amount_money: int) -> None:
        if client_from not in self.clients:
            self.clients[client_from] = 0

        if client_to not in self.clients:
            self.clients[client_to] = 0

        self.clients[client_from] -= amount_money
        self.clients[client_to] += amount_money

    def withdraw(self, client_name: str, amount_money: int) -> None:
        if client_name not in self.clients:
            self.clients[client_name] = 0

        self.clients[client_name] -= amount_money

    def income(self, percent: int) -> None:
        for client_name in self.clients.keys():
            if self.clients[client_name] > 0:
                self.clients[client_name] += int(self.clients[client_name]*(float(percent)/100.0))


def command(bank: Bank, command: str) -> None:
    commands = command.split(" ")
    if commands[0] == "BALANCE":
        client_balance = bank.get_balance(commands[1])
        print(client_balance)
    elif commands[0] == "DEPOSIT":
        bank.deposit(client_name=commands[1], amount_money=int(commands[2]))
    elif commands[0] == "WITHDRAW":
        bank.withdraw(client_name=commands[1], amount_money=int(commands[2]))
    elif commands[0] == "TRANSFER":
        bank.transfer(client_from=commands[1], client_to=commands[2], amount_money=int(commands[3]))
    elif commands[0] == "INCOME":
        bank.income(int(commands[1]))


if __name__ == "__main__":
    bank = Bank()

    with open("input.txt") as f:
        for line in f:
            command(bank, line.strip())
