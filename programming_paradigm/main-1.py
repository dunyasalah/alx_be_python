import sys
from enhanced_bank_account import EnhancedBankAccount

def main():
    account = EnhancedBankAccount(100, 0.05)  # 5% interest

    if len(sys.argv) < 2:
        print("Usage: python main-1.py <command>:<amount>")
        print("Commands: deposit, withdraw, display, interest")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    elif command == "interest":
        account.apply_interest()
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()