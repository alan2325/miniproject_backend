print("1.Add employ\n2.View employ \n3.Update employ\n4.Delete employ\n5.Exit")
worker=[[123,'alal',21,4,'alal@gmail.com',1234567890],
        [321,'blabla',33,7,'bla@.com',987654321]]
while True:
    a=int(input("Enter your choice : "))
    
    

    
    if a==1:
        W_id=int(input("Enter employee ID : "))
        w_name=str(input("Enter your name : "))
        w_age=int(input("Enter your age : "))
        w_exp=int(input("Enter the experience : "))
        w_email=input("Enter email:  ")
        w_phone=int(input("Enter contact number : "))
        worker.append([ W_id,w_name,w_age,w_exp,w_email,w_phone])

       


    elif a==2:
        
             
            for i in worker:
                print("Details of employee : ")
                print()
                print("Employe ID is : ",i[0])
                print("Names of the employe :",i[1]) 
                print("Age is : ",i[2])
                print("Experience of employee : ",i[3])
                print("E-mail : ",i[4])
                print("Phone number : ",i[5])
                print()
    elif a==3:
        old_id=int(input("Enter ID needed to be updated : "))
        f=0
        for i in (worker):
            if old_id==i[0]:

                f=1
                w_name=str(input("Enter your name : "))
                w_age=int(input("Enter your age : "))
                w_exp=int(input("Enter the experience : "))
                w_email=input("Enter email:  ")
                w_phone=int(input("Enter contact number : "))

                i[1]=w_name
                i[2]=w_age
                i[3]=w_exp
                i[4]=w_email
                i[5]=w_phone

                
        if f==0:
            print("ID not found")
                     
       

    elif a==4:
            d=int(input("Enter ID needed to be deleted: "))
            f=0
            for i in range(len(worker)):
                if d==worker[i][0]:  
                    f=1
                    del worker[i]    
                    print("Employee details succesfully deleted")   
                    break               

            if f==0:
                print("ID not found")
            else:
                print("Updated worker list :")
                 
                for i in worker:
                    
                    print()
                    print("Employe ID is : ",i[0])
                    print("Names of the employe :",i[1]) 
                    print("Age is : ",i[2])
                    print("Experience of employee : ",i[3])
                    print("E-mail : ",i[4])
                    print("Phone number : ",i[5])
                    print()

    elif a==5:
            print("You had exited")
            break
            
    else:
        print("INVALID INPUT !")



        