"""
    Bank Management System - Python OOP
    Features: Create Account, Login, Deposit, Withdraw, Transfer
"""
import uuid
import hashlib
from datetime import datetime

class Transaction:
    def __init__(self, transaction_type, amount, balance_after, description=""):
        self.transaction_id = str(uuid.uuid4())[:8].upper()
        self.transaction_type = transaction_type
        self.amount = amount
        self.balance_after = balance_after
        self.description = description
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return (f"[{self.timestamp}] {self.transaction_type:<10} "
                f"Amount: ${self.amount:>10.2f}  "
                f"Balance: ${self.balance_after:>10.2f}  "
                f"{self.description}")

class Account:
    def __init__(self, owner_name, password, initial_deposit=0.0):
        self.account_number = self._generate_account_number()
        self.owner_name = owner_name
        self._password_hash = self._hash_password(password)
        self._balance = initial_deposit
        self.transactions = []
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if initial_deposit > 0:
            txn = Transaction("DEPOSIT", initial_deposit, self._balance, "Initial deposit")
            self.transactions.append(txn)

    def _generate_account_number(self):
        return "ASDA -" + str(uuid.uuid4())[:8].upper()

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, password):
        return self._password_hash == self._hash_password(password)

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self._balance += amount
        txn = Transaction("DEPOSIT", amount, self._balance)
        self.transactions.append(txn)
        return txn

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self._balance:
            raise ValueError(f"Insufficient funds. Available balance: ${self._balance:.2f}")
        self._balance -= amount
        txn = Transaction("WITHDRAW", amount, self._balance)
        self.transactions.append(txn)
        return txn

    def _internal_transfer_out(self, amount, target_account_number):
        self._balance -= amount
        txn = Transaction("TRANSFER OUT", amount, self._balance,
                          f"To {target_account_number}")
        self.transactions.append(txn)
        return txn

    def _internal_transfer_in(self, amount, source_account_number):
        self._balance += amount
        txn = Transaction("TRANSFER IN", amount, self._balance,
                          f"From {source_account_number}")
        self.transactions.append(txn)
        return txn

    def get_statement(self):
        lines = [
            f"\n{'='*65}",
            f"  ACCOUNT STATEMENT",
            f"{'='*65}",
            f"  Account Number : {self.account_number}",
            f"  Account Holder : {self.owner_name}",
            f"  Created On     : {self.created_at}",
            f"  Current Balance: ${self._balance:.2f}",
            f"{'='*65}",
        ]
        if not self.transactions:
            lines.append("  No transactions found.")
        else:
            lines.append(f"  {'DATE':<20} {'TYPE':<12} {'AMOUNT':>12}  {'BALANCE':>12}  NOTE")
            lines.append(f"  {'-'*61}")
            for txn in self.transactions:
                lines.append(f"  {txn.timestamp:<20} {txn.transaction_type:<12} "
                              f"${txn.amount:>10.2f}  ${txn.balance_after:>10.2f}  {txn.description}")
        lines.append(f"{'='*65}\n")
        return "\n".join(lines)

    def __str__(self):
        return (f"Account[{self.account_number}] - Owner: {self.owner_name} "
                f"- Balance: ${self._balance:.2f}")


class Bank:
    def __init__(self, bank_name="PyBank"):
        self.bank_name = bank_name
        self._accounts = {}          # account_number -> Account
        self._logged_in_account = None

    # ── Create Account ────────────────────────────────────────────────
    def create_account(self, owner_name, password, initial_deposit=0.0):
        if not owner_name.strip():
            raise ValueError("Owner name cannot be empty.")
        if len(password) < 4:
            raise ValueError("Password must be at least 4 characters.")
        if initial_deposit < 0:
            raise ValueError("Initial deposit cannot be negative.")

        account = Account(owner_name.strip(), password, initial_deposit)
        self._accounts[account.account_number] = account
        print(f"\n✅ Account created successfully!")
        print(f"   Account Number : {account.account_number}")
        print(f"   Account Holder : {account.owner_name}")
        print(f"   Opening Balance: ${account.balance:.2f}")
        return account

    # ── Login ──────────────────────────────────────────────────────────
    def login(self, account_number, password):
        account = self._accounts.get(account_number)
        if not account:
            raise ValueError("Account not found.")
        if not account.verify_password(password):
            raise ValueError("Incorrect password.")
        self._logged_in_account = account
        print(f"\n✅ Welcome back, {account.owner_name}! Login successful.")
        return account

    def logout(self):
        if self._logged_in_account:
            print(f"\n👋 Goodbye, {self._logged_in_account.owner_name}!")
            self._logged_in_account = None
        else:
            print("No active session.")

    def _require_login(self):
        if not self._logged_in_account:
            raise PermissionError("You must be logged in to perform this action.")
        return self._logged_in_account

    # ── Deposit ────────────────────────────────────────────────────────
    def deposit(self, amount):
        account = self._require_login()
        txn = account.deposit(amount)
        print(f"\n✅ Deposit successful!")
        print(f"   Deposited : ${amount:.2f}")
        print(f"   Balance   : ${account.balance:.2f}")
        return txn

    # ── Withdraw ───────────────────────────────────────────────────────
    def withdraw(self, amount):
        account = self._require_login()
        txn = account.withdraw(amount)
        print(f"\n✅ Withdrawal successful!")
        print(f"   Withdrawn : ${amount:.2f}")
        print(f"   Balance   : ${account.balance:.2f}")
        return txn

    # ── Transfer ───────────────────────────────────────────────────────
    def transfer(self, target_account_number, amount):
        sender = self._require_login()
        if sender.account_number == target_account_number:
            raise ValueError("Cannot transfer to the same account.")
        if amount <= 0:
            raise ValueError("Transfer amount must be greater than zero.")
        if amount > sender.balance:
            raise ValueError(f"Insufficient funds. Available: ${sender.balance:.2f}")

        receiver = self._accounts.get(target_account_number)
        if not receiver:
            raise ValueError(f"Target account '{target_account_number}' not found.")

        sender._internal_transfer_out(amount, target_account_number)
        receiver._internal_transfer_in(amount, sender.account_number)

        print(f"\n✅ Transfer successful!")
        print(f"   Sent To   : {receiver.owner_name} ({target_account_number})")
        print(f"   Amount    : ${amount:.2f}")
        print(f"   Balance   : ${sender.balance:.2f}")

    # ── Statement ──────────────────────────────────────────────────────
    def view_statement(self):
        account = self._require_login()
        print(account.get_statement())

    def check_balance(self):
        account = self._require_login()
        print(f"\n💰 Current Balance: ${account.balance:.2f}")


# ── Interactive CLI Menu ───────────────────────────────────────────────────────

def print_menu(logged_in=False):
    print(f"\n{'─'*40}")
    if not logged_in:
        print("  🏦  BANK MANAGEMENT SYSTEM")
        print("─" * 40)
        print("  1. Create Account")
        print("  2. Login")
        print("  0. Exit")
    else:
        print("  🏦  MAIN MENU  (Logged In)")
        print("─" * 40)
        print("  3. Deposit")
        print("  4. Withdraw")
        print("  5. Transfer")
        print("  6. View Statement")
        print("  7. Check Balance")
        print("  8. Logout")
        print("  0. Exit")
    print("─" * 40)


def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("  ⚠️  Please enter a valid number.")


def main():
    bank = Bank("PyBank")

    # --- seed demo accounts for easy testing ---
    demo1 = bank.create_account("Alice Johnson", "alice123", 1000.00)
    demo2 = bank.create_account("Bob Smith",    "bob456",   500.00)
    print(f"\n  📌 Demo accounts created for testing:")
    print(f"     Alice : {demo1.account_number}  password: alice123")
    print(f"     Bob   : {demo2.account_number}  password: bob456")
    # -------------------------------------------

    while True:
        print_menu(logged_in=bank._logged_in_account is not None)
        choice = input("  Enter choice: ").strip()

        try:
            if choice == "1":
                print("\n── Create New Account ──")
                name    = input("  Full Name        : ").strip()
                pwd     = input("  Password         : ").strip()
                deposit = get_float("  Initial Deposit  : $")
                bank.create_account(name, pwd, deposit)

            elif choice == "2":
                print("\n── Login ──")
                acc_no = input("  Account Number : ").strip()
                pwd    = input("  Password       : ").strip()
                bank.login(acc_no, pwd)

            elif choice == "3":
                print("\n── Deposit ──")
                amount = get_float("  Amount : $")
                bank.deposit(amount)

            elif choice == "4":
                print("\n── Withdraw ──")
                amount = get_float("  Amount : $")
                bank.withdraw(amount)

            elif choice == "5":
                print("\n── Transfer ──")
                target = input("  Target Account Number : ").strip()
                amount = get_float("  Amount                : $")
                bank.transfer(target, amount)

            elif choice == "6":
                bank.view_statement()

            elif choice == "7":
                bank.check_balance()

            elif choice == "8":
                bank.logout()

            elif choice == "0":
                print("\n👋 Thank you for using PyBank. Goodbye!\n")
                break

            else:
                print("  ⚠️  Invalid option. Please try again.")

        except (ValueError, PermissionError) as e:
            print(f"\n  ❌ Error: {e}")


if __name__ == "__main__":
    main()