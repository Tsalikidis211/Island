def update_balance(balance):
    with open("tsalikidis.txt", "w") as f:
        f.write(f"Tsalikidhs -Nikolaos- {balance}$")

def get_balance():
    with open("tsalikidis.txt", "r") as f:
        return float(f.read().split(' ')[-1].replace('$', ''))

def deposit():
    amount = float(input("Enter deposit amount: "))
    balance = get_balance() + amount
    update_balance(balance)
    print(f"New balance: {balance}$")

def withdraw():
    amount = float(input("Enter withdrawal amount: "))
    balance = get_balance()
    if amount <= balance:
        update_balance(balance - amount)
        print(f"New balance: {balance - amount}$")
    else:
        print("Insufficient balance!")

def menu():
    print("1. Change balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check balance")

def main():
    while True:
        menu()
        choice = input("Choose option: ")

        if choice == '1':
            new_balance = float(input("Enter new balance: "))
            update_balance(new_balance)
            print(f"Balance updated to: {new_balance}$")
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            print(f"Current balance: {get_balance()}$")
        else:
            print("Invalid option.")

        if input("Continue? (y/n): ").lower() != 'y':
            break

    print("Exit.")

if __name__ == "__main__":
    main()
