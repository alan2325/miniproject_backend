# data=[
#     {'op':1,'uname':'cab1','pswd':987,'email':'cab1@gmail.com','pno':'123456700','livloc':'ekm','tno':'kl5b123'},
#     {'op':1,'uname':'cab2','pswd':876,'email':'cab2@gmail.com','pno':'998766789','livloc':'ktm','tno':'kl6b123'},
#     {'op':1,'uname':'cab3','pswd':765,'email':'cab3@gmail.com','pno':'123467812','livloc':'vkm','tno':'kl7b123'},
#     {'op':2,'uname':'user1','pswd':123,'email':'u1@gmail.com','pno':'123456789','livloc':'ktm','headloc':'vkm','time':'1pm'},
#     {'op':2,'uname':'user2','pswd':234,'email':'u2@gmail.com','pno':'987654321','livloc':'vkm','headloc':'ekm','time':'2pm'},
#     {'op':2,'uname':'user3','pswd':345,'email':'u3@gmail.com','pno':'123454321','livloc':'ekm','headloc':'ktm','time':'3pm'},
# ]

# while True:
#     # Display the menu
#     print("1.Register \n2.Login \n3.Cancel")
#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         # Registration
#         op = int(input("Are you interested in working as an Uber driver?\n1.Yes\n2.No\nEnter your choice: "))
        
#         if op == 1:
#             uname = input("Enter the name: ")
#             pswd = int(input("Enter password: "))
#             email = input("Enter your email: ")
#             pno = input("Enter your phone number: ")
#             tno = input("Enter your taxi registration number: ")
#             data.append({'op': 1, 'uname': uname, 'pswd': pswd, 'email': email, 'pno': pno, 'tno': tno})
#             print("Registration successful!")
        
#         elif op == 2:
#             uname = input("Enter the name: ")
#             pswd = int(input("Enter password: "))
#             email = input("Enter your email: ")
#             pno = input("Enter your phone number: ")
#             data.append({'op': 2, 'uname': uname, 'pswd': pswd, 'email': email, 'pno': pno})
#             print("Registration successful!")
        
#         else:
#             print("Invalid input")
    
#     elif choice == 2:
#         uname = input("Enter your name: ")
#         pswd = int(input("Enter password: "))
        
#         found = False
#         for entry in data:
#             if entry['uname'] == uname and entry['pswd'] == pswd:
#                 found = True
#                 print("Login successful!")
                
#                 if entry['op'] == 1:  # Cab driver
#                     while True:
#                         cab_choice = int(input("1.View bookings\n2.Add details\n3.Logout\nEnter your choice: "))
                        
#                         if cab_choice == 1:
#                             # Implement view bookings functionality
#                             print("User name : ")
#                             print("destination : ")
#                             print("Time of departure :")
#                             print("Earning : ")



#                             #need notification , when the user booked cab
                        
#                         elif cab_choice == 2:
#                             livloc = input("Share your current location: ")
#                             # Add location to data
#                             entry['livloc'] = livloc
#                             print("Location added successfully.")
                        
#                         elif cab_choice == 3:
#                             print("Logout successful.")
#                             break
                        
#                         else:
#                             print("Invalid input")
                
#                 elif entry['op'] == 2:  # User
#                     while True:
#                         u_choice = int(input("1.Book taxi\n2.View details\n3.Logout\nEnter your choice: "))
                        
#                         if u_choice == 1:
#                             livloc = input("Share your current location: ")
#                             if entry['livloc'] == livloc:        #####live location of taxi




#                                 headloc = input("Where do you want to go: ")
#                                 time = input("Enter the time you want taxi to arrive: ")
#                                 data.append({'livloc': livloc, 'headloc': headloc, 'time': time})
#                                 print("Booking successful!")
#                             else :
#                                 ("Sorry,No taxi is avialable")





                        
#                         elif u_choice == 2:
#                             # Implement view details functionality
#                             print("Taxi driver name : ")
#                             print("Taxi driver number :")
#                             print("cab cost : ")
                        
#                         elif u_choice == 3:
#                             print("Logout successful.")
#                             break
                        
#                         else:
#                             print("Invalid input")
        
#         if not found:
#             print("Invalid inputs. Please try again.")
    
#     elif choice == 3:
#         print("Exiting...")
#         break
    
#     else:
#         print("Invalid choice. Please enter a valid option.")




#2





# data=[
#     {'ekm':20,'ktm':25,'vkm':23},
#     {'op':1,'uname':'cab1','pswd':987,'email':'cab1@gmail.com','pno':'123456700','livloc':'ekm','tno':'kl5b123'},
#     {'op':1,'uname':'cab2','pswd':876,'email':'cab2@gmail.com','pno':'998766789','livloc':'ktm','tno':'kl6b123'},
#     {'op':1,'uname':'cab3','pswd':765,'email':'cab3@gmail.com','pno':'123467812','livloc':'vkm','tno':'kl7b123'},
#     {'op':2,'uname':'user1','pswd':123,'email':'u1@gmail.com','pno':'123456789','livloc':'ktm','headloc':'vkm','time':'1pm'},
#     {'op':2,'uname':'user2','pswd':234,'email':'u2@gmail.com','pno':'987654321','livloc':'vkm','headloc':'ekm','time':'2pm'},
#     {'op':2,'uname':'user3','pswd':345,'email':'u3@gmail.com','pno':'123454321','livloc':'ekm','headloc':'ktm','time':'3pm'},
# ]



# while True:
#     # Display the menu
#     print("1.Register \n2.Login \n3.Cancel")
#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         # Registration
#         op = int(input("Are you interested in working as an Uber driver?\n1.Yes\n2.No\nEnter your choice: "))
        
#         if op == 1:
#             uname = input("Enter the name: ")
#             pswd = int(input("Enter password: "))
#             email = input("Enter your email: ")
#             pno = input("Enter your phone number: ")
#             tno = input("Enter your taxi registration number: ")
#             data.append({'op': 1, 'uname': uname, 'pswd': pswd, 'email': email, 'pno': pno, 'tno': tno, 'livloc': ''})
#             print("Registration successful!")
        
#         elif op == 2:
#             uname = input("Enter the name: ")
#             pswd = int(input("Enter password: "))
#             email = input("Enter your email: ")
#             pno = input("Enter your phone number: ")
#             data.append({'op': 2, 'uname': uname, 'pswd': pswd, 'email': email, 'pno': pno, 'livloc': '', 'headloc': '', 'time': ''})
#             print("Registration successful!")
        
#         else:
#             print("Invalid input")
    
#     elif choice == 2:
#         uname = input("Enter your name: ")
#         pswd = int(input("Enter password: "))
        
#         found = False
#         for entry in data:
#             if entry['uname'] == uname and entry['pswd'] == pswd:
#                 found = True
#                 print("Login successful!")
                
#                 if entry['op'] == 1:  # Cab driver
#                     while True:
#                         cab_choice = int(input("1.View bookings\n2.Add details\n3.Logout\nEnter your choice: "))
                        
#                         if cab_choice == 1:
#                             # Implement view bookings functionality
#                             print("Your bookings:")
#                             for booking in data:
#                                 if booking.get('livloc') == entry['livloc'] and booking.get('headloc'):
#                                     print(f"User name: {booking['uname']}")
#                                     print(f"Destination: {booking['headloc']}")
#                                     print(f"Time of departure: {booking['time']}")
#                                     print("Earning: ",livloc*headloc)  # Example earning calculation
#                                     print()
#                             # Notify when a user books a cab (suggested implementation)
#                             # Check if a new booking is made
#                             for booking in data:
#                                 if booking.get('livloc') and booking.get('headloc') and booking.get('time'):
#                                     print(f"New booking by {booking['uname']} at {booking['time']}: {booking['livloc']} to {booking['headloc']}")
                        
#                         elif cab_choice == 2:
#                             livloc = input("Share your current location: ")
#                             entry['livloc'] = livloc
#                             print("Location added successfully.")
                        
#                         elif cab_choice == 3:
#                             print("Logout successful.")
#                             break
                        
#                         else:
#                             print("Invalid input")
                
#                 elif entry['op'] == 2:  # User
#                     while True:
#                         u_choice = int(input("1.Book taxi\n2.View details\n3.Logout\nEnter your choice: "))
                        
#                         if u_choice == 1:
#                             livloc = input("Share your current location: ")
#                             if any(driver['livloc'] == livloc for driver in data if driver['op'] == 1):  # Check if taxi is available
#                                 headloc = input("Where do you want to go: ")
#                                 time = input("Enter the time you want taxi to arrive: ")
#                                 data.append({'op': 2, 'uname': uname, 'pno': pno, 'livloc': livloc, 'headloc': headloc, 'time': time})
#                                 print("Booking successful!")
#                             else:
#                                 print("Sorry, no taxi is available at your location.")
                        
#                         elif u_choice == 2:
#                             print("Taxi details:")
#                             for driver in data:
#                                 if driver['op'] == 1 and driver['livloc']:
#                                     print(f"Taxi driver name: {driver['uname']}")
#                                     print(f"Taxi driver number: {driver['pno']}")
#                                     # print(f"Cab cost: $10")  # Example cost calculation
#                                     print(f"Cab cost:" ,livloc * headloc)
                                    
#                                     cancle=("1.Exit \n2.Cancle cab") #notify cab driver if cancled
#                                     if cancle == 1:
#                                         break
#                                     elif cancle == 2 :
#                                         #  give option to cancle cab
#                                         #notify cab driver if cancled
#                                     else :
#                                         print("invalid input")
#                         elif u_choice == 3:
#                             print("Logout successful.")
#                             break
                        
#                         else:
#                             print("Invalid input")
        
#         if not found:
#             print("Invalid inputs. Please try again.")
    
#     elif choice == 3:
#         print("Exiting...")
#         break
    
#     else:
#         print("Invalid choice. Please enter a valid option.")


#3




data=[
    {'ekm':20,'ktm':25,'vkm':23},
    {'op':1,'uname':'cab1','pswd':987,'email':'cab1@gmail.com','pno':'123456700','livloc':'ekm','tno':'kl5b123'},
    {'op':1,'uname':'cab2','pswd':876,'email':'cab2@gmail.com','pno':'998766789','livloc':'ktm','tno':'kl6b123'},
    {'op':1,'uname':'cab3','pswd':765,'email':'cab3@gmail.com','pno':'123467812','livloc':'vkm','tno':'kl7b123'},
    {'op':2,'uname':'user1','pswd':123,'email':'u1@gmail.com','pno':'123456789','livloc':'ktm','headloc':'vkm','time':'1pm'},
    {'op':2,'uname':'user2','pswd':234,'email':'u2@gmail.com','pno':'987654321','livloc':'vkm','headloc':'ekm','time':'2pm'},
    {'op':2,'uname':'user3','pswd':345,'email':'u3@gmail.com','pno':'123454321','livloc':'ekm','headloc':'ktm','time':'3pm'},
]

while True:
    # Display the menu
    print("1.Register \n2.Login \n3.Cancel")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        # Registration
        op = int(input("Are you interested in working as an Uber driver?\n1.Yes\n2.No\nEnter your choice: "))
        
        if op == 1:
            uname = input("Enter the name: ")
            pswd = int(input("Enter password: "))
            email = input("Enter your email: ")
            pno = input("Enter your phone number: ")
            tno = input("Enter your taxi registration number: ")
            data.append({'op': 1, 'uname': uname, 'pswd': pswd, 'email': email, 'pno': pno, 'tno': tno, 'livloc': ''})
            print("Registration successful!")
        
        elif op == 2:
            uname = input("Enter the name: ")
            pswd = int(input("Enter password: "))
            email = input("Enter your email: ")
            pno = input("Enter your phone number: ")
            data.append({'op': 2, 'uname': uname, 'pswd': pswd, 'email': email, 'pno': pno, 'livloc': '', 'headloc': '', 'time': ''})
            print("Registration successful!")
        
        else:
            print("Invalid input")
    
    elif choice == 2:
        uname = input("Enter your name: ")
        pswd = int(input("Enter password: "))
        
        found = False
        for entry in data:
            if entry['uname'] == uname and entry['pswd'] == pswd:
                found = True
                print("Login successful!")
                
                if entry['op'] == 1:  # Cab driver
                    while True:
                        cab_choice = int(input("1.View bookings\n2.Add details\n3.Logout\nEnter your choice: "))
                        
                        if cab_choice == 1:
                            # Implement view bookings functionality
                            print("Your bookings:")
                            for booking in data:
                                if booking.get('livloc') == entry['livloc'] and booking.get('headloc'):
                                    print(f"User name: {booking['uname']}")
                                    print(f"Destination: {booking['headloc']}")
                                    print(f"Time of departure: {booking['time']}")
                                    # Calculate fare based on distance
                                    fare = abs(data[0][entry['livloc']] - data[0][booking['headloc']]) * 10  # Example fare calculation
                                    print(f"Fare: ${fare}")
                                    print()
                            # Notify when a new booking is made
                            for booking in data:
                                if booking.get('livloc') and booking.get('headloc') and booking.get('time'):
                                    print(f"New booking by {booking['uname']} at {booking['time']}: {booking['livloc']} to {booking['headloc']}")
                        
                        elif cab_choice == 2:
                            livloc = input("Share your current location: ")
                            entry['livloc'] = livloc
                            print("Location added successfully.")
                        
                        elif cab_choice == 3:
                            print("Logout successful.")
                            break
                        
                        else:
                            print("Invalid input")
                
                elif entry['op'] == 2:  # User
                    while True:
                        u_choice = int(input("1.Book taxi\n2.View details\n3.Logout\nEnter your choice: "))
                        
                        if u_choice == 1:
                            livloc = input("Share your current location: ")
                            if any(driver['livloc'] == livloc for driver in data if driver['op'] == 1):  # Check if taxi is available
                                headloc = input("Where do you want to go: ")
                                time = input("Enter the time you want taxi to arrive: ")
                                data.append({'op': 2, 'uname': uname, 'pno': pno, 'livloc': livloc, 'headloc': headloc, 'time': time})
                                print("Booking successful!")
                            else:
                                print("Sorry, no taxi is available at your location.")
                        
                        elif u_choice == 2:
                            print("Taxi details:")
                            for driver in data:
                                if driver['op'] == 1 and driver['livloc']:
                                    print(f"Taxi driver name: {driver['uname']}")
                                    print(f"Taxi driver number: {driver['pno']}")
                                    # Calculate fare based on distance
                                    fare = abs(data[0][livloc] - data[0][headloc]) * 10  # Example fare calculation
                                    print(f"Cab cost: ${fare}")
                                    
                                    cancel = int(input("1.Exit \n2.Cancel cab\nEnter your choice: "))
                                    if cancel == 2:
                                        # Cancel the booking
                                        data.remove(driver)
                                        print("Booking canceled successfully.")
                                    elif cancel != 1:
                                        print("Invalid input.")
                                        
                        elif u_choice == 3:
                            print("Logout successful.")
                            break
                        
                        else:
                            print("Invalid input")
        
        if not found:
            print("Invalid inputs. Please try again.")
    
    elif choice == 3:
        print("Exiting...")
        break
    
    else:
        print("Invalid choice. Please enter a valid option.")

