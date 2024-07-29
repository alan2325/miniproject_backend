
from library import AccessoryManager
from user import UserManager


def main():
    accessory_manager = AccessoryManager()
    user_manager = UserManager()
    
    while True:
        print("\n1. Register\n2. Login\n3. Add Accessory\n4. View Accessories\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user_manager.register_user(username, password)
        
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = user_manager.login_user(username, password)
            if user:
                while True:
                    print("\n1. Borrow Accessory\n2. Return Accessory\n3. Logout")
                    user_choice = input("Enter your choice: ")
                    if user_choice == '1':
                        accessory_id = input("Enter accessory ID: ")
                        accessory_manager.borrow_accessory(user, accessory_id)
                    elif user_choice == '2':
                        accessory_id = input("Enter accessory ID: ")
                        accessory_manager.return_accessory(user, accessory_id)
                    elif user_choice == '3':
                        break
                    else:
                        print("Invalid choice.")
        
        elif choice == '3':
            accessory_id = input("Enter accessory ID: ")
            name = input("Enter accessory name: ")
            price = float(input("Enter accessory price: "))
            accessory_manager.add_accessory(accessory_id, name, price)
        
        elif choice == '4':
            accessory_manager.view_accessories()
        
        elif choice == '5':
            break
        
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
