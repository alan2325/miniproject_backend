data=[{'op':'yes','uname':'cab1','pswd':987,'email':'cab1@gmail.com','pno':'123456700','livloc':'ekm','tno':'kl5b123'},
      {'op':'yes','uname':'cab2','pswd':876,'email':'cab2@gmail.com','pno':'998766789','livloc':'ktm','tno':'kl6b123'},
      {'op':'yes','uname':'cab3','pswd':765,'email':'cab3@gmail.com','pno':'123467812','livloc':'vkm','tno':'kl7b123'},
      {'op':'no','uname':'user1','pswd':123,'email':'u1@gmail.com','pno':'123456789','livloc':'ktm','headloc':'vkm'},
      {'op':'no','uname':'user2','pswd':234,'email':'u2@gmail.com','pno':'987654321','livloc':'vkm','headloc':'vkm'},
      {'op':'no','uname':'user3','pswd':345,'email':'u3@gmail.com','pno':'123454321','livloc':'ekm','headloc':'vkm'},]

while True:
    # Display the menu
    print("1.Regester \n2. Login \n3.Cancle")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        op=str(input("Are you intrested in working as uber driver : \n1.Yes \n2.No"))
        data.append({'op':op})
        if choice == 1:
            uname=str(input("Enter the name : "))
            pswd=int(input("Enter password : "))
            email=str(input("Enter your place : "))
            pno=int(input("Enter your phone number : "))
            livloc=str(input("Share your location : "))
            tno=str(input("Enter your taxi regestration number : "))
            data.append({'name':uname,'pswd':pswd,'email':email,'pno':pno,'livloc':livloc,'tno':tno})
        elif choice == 2:
            uname=str(input("Enter the name : "))
            pswd=int(input("Enter password : "))
            email=str(input("Enter your place : "))
            pno=int(input("Enter your phone number : "))
            livloc=str(input("Share your current location : "))
            data.append({'name':uname,'age':pswd,'place':email,'pno':pno,'livloc':livloc})
        else:
            print("Invalid input")
    if choice == 2:
        uname = input("Enter your name : ")
        pswd = int(input("Enter password : "))
       
        
        found = False
        for student in data:

            
