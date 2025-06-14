#simulating an atm
userdetails = {
    "username": "Jedidiah",
    "card_number": "1234567",
    "pin": "1234",
    "balance": 1000.00
}
#validating user details
validate_user = input("Enter your username: ")
if validate_user == userdetails["username"]:
    validate_card = input("Enter your card number: ")
    if validate_card == userdetails["card_number"]:
        validate_pin = input("Enter your pin: ")
        if validate_pin == userdetails["pin"]:
            print("Access granted.")
           #caerrying out Atm operations
            while True:
                print("Choose an option: ")
                print("1. Check Balance")
                print("2. Deposit Money")
                print("3. Withdraw Money")
                print("4. Exit")
                choice = input ("Enter your choice: (1-4): ")
                if choice == "1":
                    print (f"Your balance is: ${userdetails['balance']}")
                elif choice == "2":
                  amount = float(input("Enter amount to deposit: "))
                  userdetails["balance"] += amount
                  print("Deposit successful")
                elif choice == "3":
                  amount1 = float(input("Enter amount to withdraw"))
                  userdetails["balance"] -=amount
                  print("Withdrwal successful")
                else:
                    print("Thank you for your patronage. Have a nice day!")
                    break  
        else:
            print("Invalid pin.")#telling the user their pin is invalid
    else:
        print("Invalid card number.")#telling the user card number is invalid
else:
    print("Invalid username.")#telling the user their username is invalid

