L=[[000,'admin'],
   ['reg','name','eng','mal','maths','bio','phy','che'],
   [12345,'alal',50,40,55,34,73,47],
   [67890,'aro',43,65,45,51,33,63]]
# L=[[12345,'alal',[50,40,55,34,73,47]],
#     [67890,'aro',[43,65,45,51,33,63]]]
while True:
    # print("\n1.Login \n2.cancle")
    a=int(input("\n1.Login \n2.cancle \nEnter your choice : "))
    
    

    if a==1:
        reg=int(input("Enter regester number : "))
        name=str(input("Enter name : ")) 
        f=0
        for i in L:
            if reg==i[0] and name==i[1]: 
                f=1
                print("You have successfully logined .")
                for row in L:
                    print()
                    print("Your results are : \n")
                    print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format("English","Malayalam","Maths","biology","physics","chemistry"))
                    print('_'*60)
                    # print("\t".join(map(str,row)))
                    print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format(i[2],i[3],i[4],i[5],i[6],i[7]))    
                    # print("Marks are : ",i[2],i[3],i[4],i[5],i[6],i[7])
                    # print("marks are : ",i[3])

                    break
            if f==0:
                print("ID not found")
    elif a==2:
         print("You had exited .")
         break
    elif a==3:
        name=str(input("Enter name : ")) 
        reg=int(input("Enter password : "))
       
        f=0
        for i in L:
            if reg==i[0] and name==i[1]: 
                f=1
                b=int(input("\n1.Add student \n2.view student \n3.Exit \nEnter your choice : "))
                if b==1:
                    reg=int(input("Enter student regester number : "))
                    name=str(input("Enter student name : "))
                    eng=int(input("Enter mark in english : "))
                    mal=int(input("Enter mark in malayalam : "))
                    maths=int(input("Enter mark in maths : "))
                    bio=int(input("Enter mark in biology : "))
                    phy=int(input("Enter mark in physics : "))
                    che=int(input("Enter mark in chemistry : "))
                        
                    L.append([ reg,name,eng,mal,maths,bio,phy,che])
                    
                # elif b==2:
                #     # for i in L:
                #         print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format("English","Malayalam","Maths","biology","physics","chemistry"))
                #         print('_'*60)
                #         # print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
                      
                #         break
                # elif b==3:
                #     break
        if f==0:   
            print("ID not found")            
        
    else:
                    
                print("INVALID INPUT !")
    