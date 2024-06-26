l=[1,2,3,4,5,6,3,4,5,6]
find=int(input("Enter the no : "))
c=l.count(find)
pos=0
while c>0:
    p=l.index(find,pos)
    print(p)
    pos=p+1
    c-=1




    # or
# position=[]
# for index in range(len(l)):
#     if l[index] == find:
#           position.append(index)    
# if position:
#     print(f"position is : {position}")
if find in l:
      print()  
else:
        print("INVALID INPUT !")
    