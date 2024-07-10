# bookings=[{'user':'admin','password':000},
#           {'user':'user1','password':123}]

# while True:
#     # Display the menu
#     print("1.Regester \n2.Login \n3.Cancle")
#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#             uname=str(input("Enter the name : "))
#             pswd=int(input("Enter password : "))
#             email=str(input("Enter your place : "))
#             pno=int(input("Enter your phone number : "))
#             booking.append({'name':uname,'pswd':pswd,'email':email,'pno':pno})

#     if choice == 2:

#         # User login
#         username = input("\nEnter username: ")
#         password = input("Enter password: ")

#         found = False
#         for i in booking:


#             if password == '000' and username == 'admin':
#                 while True:
#                     print("\nAdmin Menu:")
#                     print("1.add a new tourist destination \n 2.view all bookings \n 3.exit \n")
#                     ch=int(input("Enter choice : "))






#         # for i in booking:
#         #     print("Welcome")
#         #     print("1.add a new tourist destination \n 2.book a tour \n 3.view all bookings \n 4.exit \n")
           
                    
#                     if ch=='1':
#                         name=input("enter the name of the destination:")
#                         country=input("enter the country:")
                        
#                     # elif ch=='2':
#                     #     print("\nbook a tour:")
#                     #     name=input("enter your name:")
#                     #     destination=input("enter the destination you want to book:")
#                     #     booking_date = input("Enter the booking date (YYYY-MM-DD): ")
#                     #     bookings.append({"name":name,"destination":destination, "booking_date": booking_date})
#                     #     print("booking successful\n")
                    
#                     elif ch=='2':
#                         print("\nall bookings:")
#                         if len(bookings) == 0:
#                             print("no booking yet\n")
#                         else:
#                             for booking in bookings:
#                                 print(f"Name: {booking['name']}, Destination: {booking['destination']}, Booking Date: {booking['booking_date']}")
#                             print()

                    
#                     elif ch == '3':
#                         print("\nExiting the system.")
#                         break
                    
#                     else:
#                         print("\nInvalid choice. Please enter a valid option .\n")
#             elif password==booking['user'] and username==booking[password]:
#                 print("1.Book a toor\n2.view booking details \n3.exit")
#                 ch=int(input("Enter choice :"))
#                 if ch == '1':
#                     print( )            #####book a tour
#                 elif ch == '2':
#                     print()                 #####view details
#                                             ### cancle booking
#                 elif ch =='3':
#                     print("Exited")
#                 else:
#                     print("Invalid input")













bookings = [{'user': 'admin', 'password': '000'},
            {'user': 'user1', 'password': '123'}]
users = []  # Initialize an empty list to store user registrations

while True:
    print("\nMain Menu:")
    print("1. Register\n2. Login\n3. Cancel")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        # User registration
        uname = input("Enter username: ")
        pswd = input("Enter password: ")
        email = input("Enter email: ")
        pno = input("Enter phone number: ")
        users.append({'name': uname, 'password': pswd, 'email': email, 'phone': pno})
        print("Registration successful.")

    elif choice == 2:
        # User login
        username = input("Enter username: ")
        password = input("Enter password: ")

        if any(user['name'] == username and user['password'] == password for user in users):
            print(f"Welcome, {username}!")

            if username == 'admin':
                while True:
                    print("\nAdmin Menu:")
                    print("1. Add a new tourist destination\n2. View all bookings\n3. Exit")
                    ch = input("Enter choice: ")

                    if ch == '1':
                        name = input("Enter the name of the destination: ")
                        country = input("Enter the country: ")
                        # Add functionality to add destination

                    elif ch == '2':
                        print("\nAll bookings:")
                        if len(bookings) == 0:
                            print("No bookings yet.")
                        else:
                            for booking in bookings:
                                print(f"Name: {booking['name']}, Destination: {booking['destination']}, Booking Date: {booking['booking_date']}")
                        print()

                    elif ch == '3':
                        print("\nExiting the admin menu.")
                        break

                    else:
                        print("\nInvalid choice. Please enter a valid option.\n")

            else:  # Regular user
                while True:
                    print("\nUser Menu:")
                    print("1. Book a tour\n2. View booking details\n3. Cancel booking\n4. Exit")
                    ch = input("Enter choice: ")

                    if ch == '1':
                        # Implement booking functionality
                        pass

                    elif ch == '2':
                        # Implement view booking details
                        pass

                    elif ch == '3':
                        # Implement cancel booking
                        pass

                    elif ch == '4':
                        print("\nExiting the user menu.")
                        break

                    else:
                        print("\nInvalid choice. Please enter a valid option.\n")

        else:
            print("Invalid username or password. Please try again.")

    elif choice == 3:
        print("Exiting the system.")
        break

    else:
        print("Invalid choice. Please enter a valid option.")






