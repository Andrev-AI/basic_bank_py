# main.py
import json
import os
import random
from datetime import datetime

# Global database
db = {}

# Function to load the JSON database
def load_db():
    global db
    if not os.path.exists("db.json") or os.stat("db.json").st_size == 0:
        schema = {
            "clientes": [],  # Keep original key
            "contas": [],    # Keep original key
            "transacoes": [] # Keep original key
        }
        with open("db.json", "w", encoding="utf-8") as data:
            json.dump(schema, data, indent=4, ensure_ascii=False)
    with open("db.json", "r", encoding="utf-8") as data:
        db = json.load(data)

# Function to validate input data
def validate_data(input, type):
    if type == "name":
        if not input or not all(part.isalpha() for part in input.strip().split()):
            print("Error: Invalid name. Must contain only letters and spaces.")
            return False
        return True
    elif type == "cpf":
        if not input.isdigit() or len(input) != 11:
            print("Error: Invalid CPF. Must contain 11 numeric digits.")
            return False
        return True
    elif type == "email":
        if "@" not in input or not input.endswith(".com"):
            print("Error: Invalid email. Must contain '@' and end with '.com'.")
            return False
        return True
    elif type == "phone":
        if not input.isdigit() or len(input) < 10:
            print("Error: Invalid phone. Must contain at least 10 digits.")
            return False
        return True
    elif type == "password":
        if len(input) < 6:
            print("Error: Invalid password. Must contain at least 6 characters.")
            return False
        return True
    return False

# Function to create client and account
def create_client(name, cpf, email, phone, password):
    global db
    if not all([
        validate_data(name, "name"),
        validate_data(cpf, "cpf"),
        validate_data(email, "email"),
        validate_data(phone, "phone"),
        validate_data(password, "password")
    ]):
        print("Error: Could not create client. Please verify entered data.")
        return

    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    new_client = {
        "id": len(db["clientes"]) + 1,  # Use original key
        "name": name,
        "cpf": cpf,
        "email": email,
        "phone": phone,
        "registration_date": current_datetime
    }
    db["clientes"].append(new_client)  # Use original key

    new_account = {
        "id": len(db["contas"]) + 1,  # Use original key
        "client_id": new_client["id"],
        "account_number": random.randint(10000, 99999),
        "account_type": "Checking",
        "balance": 0.0,
        "opening_date": current_datetime,
        "status": "Active",
        "password": password
    }
    db["contas"].append(new_account)  # Use original key

    with open("db.json", "w", encoding="utf-8") as data:
        json.dump(db, data, indent=4, ensure_ascii=False)
    print("Client and account created successfully!")

# Function for client login
def sign_in(login_input, password):
    global db

    # Check if client exists
    found_client = None
    for client in db["clientes"]:  # Use original key
        if login_input == client["cpf"] or login_input == client["email"]:
            found_client = client
            break

    if not found_client:
        print("Error: User not found.")
        return

    # Check if the linked account has the correct password
    for account in db["contas"]:  # Use original key
        if account["client_id"] == found_client["id"]:
            if password == account["password"]:
                print(f"Welcome, {found_client['name']}! Login successful.")
                account_info(account, found_client)
                return
            else:
                print("Error: Invalid password.")
                return

    print("Error: Account not found.")

# Function to manage account information
def account_info(account, client):
    global db
    while True:
        print(f"\nAccount: {account['account_number']}\nBalance: $ {account['balance']:.2f}")
        options = input("1 - Withdraw\n2 - Deposit\n3 - Transfer\n4 - Statement\n5 - Settings\n6 - Exit\nChoose an option: ")
        if options == "1":
            amount = float(input("Enter the amount to withdraw: "))
            if amount > account["balance"]:
                print("Error: Insufficient balance.")
            else:
                account["balance"] -= amount
                db["transacoes"].append({  # Use original key
                    "account_id": account["id"],
                    "type": "Withdrawal",
                    "amount": amount,
                    "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
                print(f"Withdrawal of $ {amount:.2f} completed successfully.")
        elif options == "2":
            amount = float(input("Enter the amount to deposit: "))
            account["balance"] += amount
            db["transacoes"].append({  # Use original key
                "account_id": account["id"],
                "type": "Deposit",
                "amount": amount,
                "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            print(f"Deposit of $ {amount:.2f} completed successfully.")
        elif options == "3":
            dest_account_number = int(input("Enter the destination account number: "))
            amount = float(input("Enter the amount to transfer: "))
            if amount > account["balance"]:
                print("Error: Insufficient balance.")
            else:
                for dest_account in db["contas"]:  # Use original key
                    if dest_account["account_number"] == dest_account_number:
                        account["balance"] -= amount
                        dest_account["balance"] += amount
                        db["transacoes"].append({  # Use original key
                            "account_id": account["id"],
                            "type": "Transfer",
                            "amount": amount,
                            "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        })
                        print(f"Transfer of $ {amount:.2f} completed successfully.")
                        break
                else:
                    print("Error: Destination account not found.")
        elif options == "4":
            print("\nStatement:")
            for transaction in db["transacoes"]:  # Use original key
                if transaction["account_id"] == account["id"]:
                    print(f"{transaction['type']} of $ {transaction['amount']:.2f} on {transaction['datetime']}")
        elif options == "5":
            config_option = input("1 - Change password\n2 - Change email\n3 - Change phone\n4 - Back\nChoose an option: ")
            if config_option == "1":
                new_password = input("Enter the new password: ")
                if validate_data(new_password, "password"):
                    account["password"] = new_password
                    print("Password changed successfully.")
                else:
                    print("Error: Invalid password.")
            elif config_option == "2":
                new_email = input("Enter the new email: ")
                if validate_data(new_email, "email"):
                    client["email"] = new_email
                    print("Email changed successfully.")
                else:
                    print("Error: Invalid email.")
            elif config_option == "3":
                new_phone = input("Enter the new phone: ")
                if validate_data(new_phone, "phone"):
                    client["phone"] = new_phone
                    print("Phone changed successfully.")
                else:
                    print("Error: Invalid phone.")
            elif config_option == "4":
                continue
            else:
                print("Invalid option.")
        elif options == "6":
            print("Exiting...")
            break
        else:
            print("Invalid option.")

        with open("db.json", "w", encoding="utf-8") as data:
            json.dump(db, data, indent=4, ensure_ascii=False)

# Load database
load_db()