# L=[[000,'admin'],
#    ['reg','name','eng','mal','maths','bio','phy','che'],
#    [12345,'alal',50,40,55,34,73,47],
#    [67890,'aro',43,65,45,51,33,63]]
# # L=[[12345,'alal',[50,40,55,34,73,47]],
# #     [67890,'aro',[43,65,45,51,33,63]]]
# while True:
#     # print("\n1.Login \n2.cancle")
#     a=int(input("\n1.Login \n2.cancle \nEnter your choice : "))
    
    

#     if a==1:
#         reg=int(input("Enter regester number : "))
#         name=str(input("Enter name : ")) 
#         f=0
#         for i in L:
#             if reg==i[0] and name==i[1]: 
#                 f=1
#                 print("You have successfully logined .")
#                 for row in L:
#                     print()
#                     print("Your results are : \n")
#                     print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format("English","Malayalam","Maths","biology","physics","chemistry"))
#                     print('_'*60)
#                     # print("\t".join(map(str,row)))
#                     print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format(i[2],i[3],i[4],i[5],i[6],i[7]))    
#                     # print("Marks are : ",i[2],i[3],i[4],i[5],i[6],i[7])
#                     # print("marks are : ",i[3])

#                     break
#             if f==0:
#                 print("ID not found")
#     elif a==2:
#          print("You had exited .")
#          break
#     elif a==3:
#         name=str(input("Enter name : ")) 
#         reg=int(input("Enter password : "))
       
#         f=0
#         for i in L:
#             if reg==i[0] and name==i[1]: 
#                 f=1
#                 b=int(input("\n1.Add student \n2.view student \n3.Exit \nEnter your choice : "))
#                 if b==1:
#                     reg=int(input("Enter student regester number : "))
#                     name=str(input("Enter student name : "))
#                     eng=int(input("Enter mark in english : "))
#                     mal=int(input("Enter mark in malayalam : "))
#                     maths=int(input("Enter mark in maths : "))
#                     bio=int(input("Enter mark in biology : "))
#                     phy=int(input("Enter mark in physics : "))
#                     che=int(input("Enter mark in chemistry : "))
                        
#                     L.append([ reg,name,eng,mal,maths,bio,phy,che])
                    
#                 # elif b==2:
#                 #     # for i in L:
#                 #         print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format("English","Malayalam","Maths","biology","physics","chemistry"))
#                 #         print('_'*60)
#                 #         # print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
                      
#                 #         break
#                 # elif b==3:
#                 #     break
#         if f==0:   
#             print("ID not found")            
        
#     else:
                    
#                 print("INVALID INPUT !")
    

# List of students and their marks
L = [
    [000, 'admin'],
    ['reg', 'name', 'eng', 'mal', 'maths', 'bio', 'phy', 'che'],
    [12345, 'alal', 50, 40, 55, 34, 73, 47],
    [67890, 'aro', 43, 65, 45, 51, 33, 63]
]

while True:
    # Display the menu
    print("\n1. Login")
    print("2. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        # User login
        reg = int(input("Enter register number: "))
        name = input("Enter name: ")
        
        found = False
        for student in L:


            if reg == 000 and name == 'admin':
                while True:
                    print("\nAdmin Menu:")
                    print("1. Add student")
                    print("2. View all students")
                    print("3. Logout")
                    admin_choice = int(input("Enter your choice: "))
                    
                    if admin_choice == 1:
                        reg = int(input("Enter register number: "))
                        name = input("Enter student name: ")
                        eng = int(input("Enter mark in English: "))
                        mal = int(input("Enter mark in Malayalam: "))
                        maths = int(input("Enter mark in Maths: "))
                        bio = int(input("Enter mark in Biology: "))
                        phy = int(input("Enter mark in Physics: "))
                        che = int(input("Enter mark in Chemistry: "))
                        
                        L.append([reg, name, eng, mal, maths, bio, phy, che])
                        print(f"Student {name} added successfully!")
                    
                    elif admin_choice == 2:
                        print("\nAll Students' Marks:")
                        print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format("Register", "Name", "English", "Malayalam", "Maths", "Biology", "Physics", "Chemistry"))
                        print('_' * 70)
                        for student in L[2:]:  # Skip the first two entries for the header and admin
                            print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format(student[0], student[1], student[2], student[3], student[4], student[5], student[6], student[7]))
                    
                    elif admin_choice == 3:
                        print("Admin logged out.")
                        break
                    
                    # else:
                    #     print("Invalid choice. Please try again.")


        
            elif reg == student[0] and name == student[1]:
                    found = True
                    print("You have successfully logged in.")
                    
                    # Display student marks
                    print("\nYour results are:")
                    print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format("Register", "Name", "English", "Malayalam", "Maths", "Biology", "Physics", "Chemistry"))
                    print('_' * 70)
                    print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format(student[0], student[1], student[2], student[3], student[4], student[5], student[6], student[7]))
                    break
        
        if not found:
            print("ID or name not found.")
    
    elif choice == 2:
        print("You have exited.")
        break
    
    else:
        print("INVALID INPUT!")

    # Admin menu
        # if reg == 000 and name == 'admin':
        #     while True:
        #         print("\nAdmin Menu:")
        #         print("1. Add student")
        #         print("2. View all students")
        #         print("3. Logout")
        #         admin_choice = int(input("Enter your choice: "))
                
        #         if admin_choice == 1:
        #             # Add a new student
        #             reg = int(input("Enter register number: "))
        #             name = input("Enter student name: ")
        #             eng = int(input("Enter mark in English: "))
        #             mal = int(input("Enter mark in Malayalam: "))
        #             maths = int(input("Enter mark in Maths: "))
        #             bio = int(input("Enter mark in Biology: "))
        #             phy = int(input("Enter mark in Physics: "))
        #             che = int(input("Enter mark in Chemistry: "))
                    
        #             L.append([reg, name, eng, mal, maths, bio, phy, che])
        #             print(f"Student {name} added successfully!")
                
        #         elif admin_choice == 2:
        #             # View all students
        #             print("\nAll Students' Marks:")
        #             print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format("Register", "Name", "English", "Malayalam", "Maths", "Biology", "Physics", "Chemistry"))
        #             print('_' * 70)
        #             for student in L[2:]:  # Skip the first two entries for the header and admin
        #                 print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format(student[0], student[1], student[2], student[3], student[4], student[5], student[6], student[7]))
                
        #         elif admin_choice == 3:
        #             print("Admin logged out.")
        #             break
                
        #         else:
        #             print("Invalid choice. Please try again.")
