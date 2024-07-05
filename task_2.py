data=[{'op':1,'uname':'cab1','pswd':987,'email':'cab1@gmail.com','pno':'123456700','livloc':'ekm','tno':'kl5b123'},
      {'op':1,'uname':'cab2','pswd':876,'email':'cab2@gmail.com','pno':'998766789','livloc':'ktm','tno':'kl6b123'},
      {'op':1,'uname':'cab3','pswd':765,'email':'cab3@gmail.com','pno':'123467812','livloc':'vkm','tno':'kl7b123'},
      {'op':2,'uname':'user1','pswd':123,'email':'u1@gmail.com','pno':'123456789','livloc':'ktm','headloc':'vkm','time':'1pm'},
      {'op':2,'uname':'user2','pswd':234,'email':'u2@gmail.com','pno':'987654321','livloc':'vkm','headloc':'ekm','time':'2pm'},
      {'op':2,'uname':'user3','pswd':345,'email':'u3@gmail.com','pno':'123454321','livloc':'ekm','headloc':'ktm','time':'3pm'},]

while True:
    # Display the menu
    print("1.Regester \n2.Login \n3.Cancle")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        #regestration
        op=int(input("Are you intrested in working as uber driver : \n1.Yes \n2.No"))
        data.append({'op':op})
        #cab regestration
        if choice == 1:
            uname=str(input("Enter the name : "))
            pswd=int(input("Enter password : "))
            email=str(input("Enter your place : "))
            pno=int(input("Enter your phone number : "))
            tno=str(input("Enter your taxi regestration number : "))
            data.append({'name':uname,'pswd':pswd,'email':email,'pno':pno,'tno':tno})
        #user regestration
        elif choice == 2:
            uname=str(input("Enter the name : "))
            pswd=int(input("Enter password : "))
            email=str(input("Enter your place : "))
            pno=int(input("Enter your phone number : "))            
            data.append({'name':uname,'age':pswd,'place':email,'pno':pno})
        else:
            print("Invalid input")
    elif choice == 2:
        uname = input("Enter your name : ")
        pswd = int(input("Enter password : "))
       
        
        found = False
        for s in data:
            if s['op'] == 2 and uname == s['uname'] and pswd == s[pswd]:
                        found = True
                        print("You have successfully logged in.")
                        
                        while True:
                            u_choice=int(input("1.Book taxi \n2.View details \n3.Logut \nEnter your choice : "))
                            if u_choice == 1:                                
                                livloc=str(input("Share your current location : "))
                                headloc=str(input("Where do you want to go : "))     
                                time=str(input("Enter the time you want taxi to arive"))   
                                data.append({'livloc':livloc,'headloc':headloc,'time':time})
                            elif u_choice == 2:
                                print(details&price) #booking details

                            elif u_choice == 3:
                                print("You had logouted")
                                break
                            else:
                                 print("Invalid input")

                            
                        
        
            elif s['op'] == 1 and uname == s['uname'] and pswd == s[pswd]:
                        found = True
                        print("You have successfully logged in.")
                        while True:
                            cab_choice = int(input("1.View booking \n2.Add details \n3.Logout \nEnter your choice : "))  
                            if cab_choice == 1:
                                print(details&price) #booking details

                            elif cab_choice == 2:
                                livloc=str(input("Share your current location : "))
                                data.append({'livloc':livloc})
                            elif cab_choice == 3:
                                print("You had logouted")
                                break
                            else:
                                 print("Invalid input")


    elif choice == 3:
        print("You had exited")
        break