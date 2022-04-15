
CLIENTS_INFO = {'client1': ['1010', 1000], 'client2': ['1337', 1548], 'client3': ['1234', 3456],
                'client4': ['7543', 2582],  'client5': ['3476', 2099]}


def get_pin(client_name: str):
    return CLIENTS_INFO[client_name][0]


def get_balance(client_name: str):
    return CLIENTS_INFO[client_name][1]

