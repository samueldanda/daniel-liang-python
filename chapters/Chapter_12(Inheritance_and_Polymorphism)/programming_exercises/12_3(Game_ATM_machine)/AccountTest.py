import sys
from Account import Account


def main():
    accounts = [Account(id=i, balance=100) for i in range(10)]

    print(accounts)

    start(accounts)


def start(accounts):
    account_id = prompt_account_id()
    print_main_menu()
    choice = prompt_choice(1, 6)
    proces_choice(account_id, choice, accounts)


def prompt_account_id():
    account_id = int(input('Enter account id: '))
    return id


def print_main_menu():
    print('\nMain Menu')
    print('1: Add account')
    print('2: Remove account')
    print('3: Check balance')
    print('4: Withdraw')
    print('5: Deposit')
    print('6: Exit')


def proces_choice(account_id, choice, accounts):
    print('[[ type(account_id): {} account_id: {} ]]'.format(type(account_id), account_id))
    if choice == 1:
        account_id = len(accounts)
        accounts.append(Account(id=account_id, balance=100))
        print("Account added successfully")
        print("ID: " + str(accounts[account_id].get_id()))
        print("Balance: " + str(accounts[account_id].get_balance()))
        print(accounts)
    elif choice == 2:
        for account in accounts:
            print('[[ if {} == {} ]]'.format(account.get_id(), account_id))
            if account.get_id() == account_id:
                print('[[ Trying to remove account with details: {} ]]'.format(account))
                sys.exit()
        print('No account with this id {} found'.format(account_id))
    elif choice == 3:
        print('The balance is: {}'.format(accounts[account_id].get_balance()))
    elif choice == 4:
        amount = int(input('Enter amount to withdraw: '))
        if accounts[account_id].withdraw(amount):
            print('Withdrawn amount {}'.format(amount))
            print('Balance: {}'.format(accounts[account_id].get_balance()))
        else:
            print('Balance cannot be withdrawn')
    elif choice == 5:
        amount = int(input('Enter amount to deposit: '))
        accounts[account_id].deposit(amount)
        print('Deposited amount {}'.format(amount))
        print('Balance: {}'.format(accounts[account_id].get_balance()))
    elif choice == 6:
        print('Bye')
        sys.exit()

    start(accounts)


def prompt_choice(min_choice, max_choice):
    choice = eval(input('Enter a choice: '))

    if choice < min_choice or choice > max_choice:
        print('Invalid choice')
        prompt_choice(min_choice, max_choice)

    return choice


main()
