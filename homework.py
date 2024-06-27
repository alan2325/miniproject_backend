L=[['reg','name','eng','mal','maths','bio','phy','che'],
    [12345,'alal',50,40,55,34,73,47],
    [67890,'aro',43,65,45,51,33,63]]
while True:
    print("\n1.Login \n2.cancle")
    a=int(input("Enter your choice : "))
    
    

    if a==1:
        reg=int(input("Enter regester number : "))
        name=str(input("Enter name : ")) 
        f=0
        for i in L:
            if reg==i[0] and name==i[1]: 
                f=1
                print("You have successfully logined")
                for row in L:
                    # print("\t".join(map(str,row)))
                    print("Marks are : ",i[2],i[3],i[4],i[5],i[6],i[7])

                    break
            if f==0:
                print("ID not found")
    else:
                    
                print("INVALID INPUT !")
    