import constants


def withdraw(amount: int, client: str):
    if amount > constants.get_balance(client):
        return print('No enough money in credit card')

    constants.CLIENTS_INFO[client][1] = constants.get_balance(client) - amount
    print(f'{amount}$ were withdrawn!')


def deposit(amount: int, client: str):
    constants.CLIENTS_INFO[client][1] = constants.get_balance(client) + amount
    print(f'{amount}$ were deposited')


def check_balance(client: str):
    print(f'Your balance is {constants.CLIENTS_INFO[client][1]}$')
