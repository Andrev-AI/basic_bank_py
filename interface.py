from main import *
import json

def display():
    while True:
        print("="*80, "\nWelcome to aBANK! What you want to do?\n1 - Sign in \n2 - Sign up\n3 - Exit\n", "="*80)
        try:
            option = int(input("Choose an option: "))
        except ValueError:
            print("Error: Invalid choice. Enter a number between 1 and 3.")
            continue
        if option == 1:
            sign_in(
                login_input=input("Welcome back!\n CPF or email: "),
                password=input("Password: ")
            )
        elif option == 2:
            create_client(
                name=input("Hello! First, tell us your full Name: "),
                cpf=input("Now your CPF: "),
                email=input("Your e-mail to contact: "),
                phone=input("Phone Number: "),
                password=input("Choose a password: ")
            )
        elif option == 3:
            print("Exit")
            break
        else:
            print("Error: Invalid choice. Try again.")
        print(json.dumps(db, indent=4, ensure_ascii=False))

display()