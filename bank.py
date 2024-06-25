
user=[['alal',21,'alal@gmail.com',1234567890,'asppwd',0],
        ['blabla',33,'bla@.com',987654321,'psd',500]]
while True:
    print("1.Regester \n2.Login \n3.cancle")
    a=int(input("Enter your choice : "))
    
    

    if a==1:
       
        name=str(input("Enter your name : "))
        age=int(input("Enter your age : "))
        email=input("Enter email:  ")
        phone=int(input("Enter contact number : "))
        pswd=str(input("Enter password"))
        user.append([name,age,email,phone,pswd,0])

    elif a==2:
        
        email=input("Enter email:  ")
        pswd=str(input("Enter password : ")) 
        f=0
        for i in user:
            if email==i[2] and pswd==i[4]: 
                f=1
                print("You have successfully logined")
        
                while True:
                    print("1.Balance \n2.Deposit \n3.Withdraw \n4.Logout")
                    a=int(input("Enter your choice : "))

                    if a==1:
                        print("Your balance is : ",i[5])


                    elif a==2:
                        depo=int(input("Enter your deposit amount : "))
                        i[5]+=depo



                    elif a==3:
                        wid=int(input("Enter your withdraw amount : "))
                        if i[5]>=wid:

                            i[5]-=wid
                        else :
                            print("Insuficient balnce")

                    
                    elif a==4:
                        print("You had logouted")
                        break

                    else:
                        print("INVALID INPUT !")

    
                
        if f==0:
            print("Invalid email or password")
        




    elif a==3:
            print("You had exited")
            break
    
    else:
        print("INVALID INPUT !")
