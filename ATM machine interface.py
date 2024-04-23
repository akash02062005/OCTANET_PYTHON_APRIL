def authenticate(user_id, pin):
    user_ID = ['020605']
    PIN = ['2005']
    name= ['Akash S']  
    if user_id in user_ID:
        index =user_ID.index(user_id)
        if pin ==PIN[index] and name[index] == 'Akash S':
            return True
    return False

def withdraw(balance, transactions):
    print("Withdraw funds from the user's account.")
    amount = float(input("Enter amount to withdraw: "))
    if amount > 0 and balance >= amount:
        balance = balance - amount
        print("Withdrawal successful.")
        print("Remaining balance:",balance)
    else:
        print("Insufficient funds or invalid amount.")

def deposit(balance, transactions):
    print("Deposit funds into the user's account.")
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance = balance + amount
        print("Deposit successful.")
        print("Current balance:",balance)
    else:
        print("Invalid amount.")

def transfer(balance, transactions):
    "Transfer funds from the user's account to another account."
    recipient_id = input("Enter recipient's user ID: ")
    amount = float(input("Enter amount to transfer: "))
    if amount > 0 and balance >= amount:
        balance = balance - amount
        print("Transfer successful.")
        print("Remaining balance:",balance)
    else:
        print("Insufficient funds or invalid amount.")
def transaction_history(transactions):
    "Display transaction history for the user's account."
    print("Transaction History:")
    if transactions:
        for index, transaction in enumerate(transactions, start=1):
            print(index,transaction)
    else:
        print("No transactions yet.")

def main():
    print("Welcome to Indian Bank ATM")
    user_id = input("Enter your user ID: ")
    pin = input("Enter your PIN: ")
    if authenticate(user_id, pin):
        print("Welcome, Akash S!")  
        balance = 2000  
        transactions = []
        
        while True:
            print("\nATM Menu:")
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Transfer")
            print("4. Transaction History")
            print("5. Quit")
            choice = input("Enter your choice: ")
            
            if choice == '1':
                withdraw(balance, transactions)
            elif choice == '2':
                deposit(balance, transactions)
            elif choice == '3':
                transfer(balance, transactions)
            elif choice == '4':
                transaction_history(transactions)
            elif choice == '5':
                print("Thank you for using the ATM")
                break
            else:
                print("Invalid choice. Please try again.")


main()
