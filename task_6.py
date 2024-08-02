while True:
    print('\n1. Add\n2. Update\n3. Display\n4. Delete\n5. Exit')
    ch = int(input('Enter your choice: '))

    if ch == 1:
        name=str(input("Enter name of the product : "))
        stock=int(input("Enter stock : "))

    elif ch == 2:
        print()