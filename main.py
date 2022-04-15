import constants
import options
client_pin = ''
client_name = ''
while client_name not in constants.CLIENTS_INFO.keys():
    client_name = input('Please enter your name.  ')
    if client_name not in constants.CLIENTS_INFO.keys():
        print('not registered in our database')

br = 0
while client_pin != constants.get_pin(client_name):
    if br >= 3:
        print('Credit card blocked')
        quit()
    client_pin = input(f'Please enter your pin. You have {3-br} attempts.')
    br += 1
print(f'Welcome {client_name}.\n1 -> withdraw\n2 -> deposit\n3 -> check balance\n4 -> quit')
while True:
    client_input = str(input('enter 1/2/3/4 \n'))
    try:
        if client_input == '1':
            options.withdraw(int(input('Please enter amount \n')), client_name)
        if client_input == '2':
            options.deposit(int(input('Please enter amount \n')), client_name)
        if client_input == '3':
            options.check_balance(client_name)
        if client_input == '4':
            quit()
    except ValueError:
        print('Please enter valid number!')
