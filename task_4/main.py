from menu import display_menu
from donor import add_donor, view_donors, update_donor, delete_donor,search_donors_by_name, search_donors_by_blood_group, display_search_results
from auth import reg,login
from storage import initialize_storage

def main():
    initialize_storage()


    



    if not login():
        print("Login failed. Exiting the system.")
        return
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_donor()
        elif choice == '2':
            view_donors()
           
            while True:
                print("\nBlood Bank Management System")
                print("============================")
                print("1. View All Donors")
                print("2. Search Donor by Name")
                print("3. Search Donor by Blood Group")
                print("4. Exit")
            
                choice = input("Enter your choice: ")
            
                if choice == '1':
                    view_donors()
                elif choice == '2':
                    name = input("Enter the donor name to search: ")
                    results = search_donors_by_name(name)
                    display_search_results(results)
                elif choice == '3':
                    blood_group = input("Enter the blood group to search: ")
                    results = search_donors_by_blood_group(blood_group)
                    display_search_results(results)
                elif choice == '4':
                    print("Exiting the system. Goodbye!")
                    break
                else:
                    print("Invalid choice! Please try again.")



        elif choice == '3':
            update_donor()
        elif choice == '4':
            delete_donor()
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()