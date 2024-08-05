import mysql.connector

# Establish database connection
em = mysql.connector.connect(
    host="localhost",
    user="alal",
    password="alal123",
    database="mydatabase"
)

cursor = em.cursor()

# Create table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS product (
        p_id INT PRIMARY KEY,
        name VARCHAR(100),
        price INT,
        quantity INT,
    )
''')

while True:
    print('\n1. Add product\n2. Update product\n3. Delete\n4. Search\n5. View all\n6. buy \n7. Exit')
    ch = int(input('Enter your choice: '))
    
    if ch == 1:
        l = int(input("Enter limit: "))
        for i in range(l):
            print('_' * 50)
            p_id = int(input('Enter product ID: '))
            name = input('Enter name: ')
            price = int(input('Enter price: '))
            stock =int(input("Enter quantity :"))
            cursor.execute('''
                INSERT INTO product (p_id, name, price, quantity)
                VALUES (%s, %s, %s, %s)
            ''', (p_id, name, price, stock))
            em.commit()

    elif ch == 2:
        p_id = int(input("Enter the ID of the product to update: "))
        cursor.execute("SELECT * FROM product WHERE p_id = %s", (p_id,))
        product = cursor.fetchone()
        
        if product:
            print('_' * 50)
            new_name = input(f'Enter new name (current: {product[1]}): ')
            new_price = int(input(f'Enter new price (current: {product[2]}): '))
            new_stock = input(f'Enter new quantity (current: {product[3]}): ')
           
            cursor.execute('''
                UPDATE product
                SET name = %s, price = %s, quantity = %s
                WHERE p_id = %s
            ''', (new_name, new_price, new_stock, p_id))
            em.commit()
            print("Updated successfully!")
        else:
            print("Product ID not found.")

    elif ch == 3:
        p_id = int(input("Enter the ID of the product to delete: "))
        cursor.execute("DELETE FROM product WHERE p_id = %s", (p_id,))
        em.commit()
        print("Deleted successfully!")

    elif ch == 4:
        p_id = int(input("Enter the ID of the product to search: "))
        cursor.execute("SELECT * FROM product WHERE p_id = %s", (p_id,))
        product = cursor.fetchone()
        
        if product:
            print('_' * 50)
            print(f'ID: {product[0]}')
            print(f'Name: {product[1]}')
            print(f'price: {product[2]}')
            print(f'quantity: {product[3]}')
           
        else:
            print("product ID not found.")

    elif ch == 5:
        cursor.execute("SELECT * FROM product")
        product = cursor.fetchall()
        
        if product:

            while True:
                viewch = int(input('View by :\n1. Order\n2. Like \n3. Group By\n4. Exit \nEnter your choice:'))


                if viewch == 1:



                    while True:
                        print('Order by :\n1. Id \n2. Name n3. Exit')
                        och = int(input('Enter your choice: '))
                        
                        if och ==1:
                            cursor.execute("select * from product order by p_id ")##or 'by name desc'
                            product = cursor.fetchall()
                
                            print("{:<10}{:<10}{:<10}{:<10}".format("Id","Name","Price","quantity")) ##print in a table
                            print('_'*60)
                            for p in product:
                                print("{:<10}{:<10}{:<10}{:<10}".format(p[0],p[1],p[2],p[3])) 
                            print()
                        elif och == 2:


                            cursor.execute("select * from product order by name ")##or 'by name desc'
                            product = cursor.fetchall()
                
                            print("{:<10}{:<10}{:<10}{:<10}".format("Id","Name","price","quantity")) ##print in a table
                            print('_'*60)
                            for p in product:
                                print("{:<10}{:<10}{:<10}{:<10}".format(p[0],p[1],p[2],p[3])) 
                            print()
                        elif och == 3:

                            break
                elif viewch == 2:
                    while True:
                        print('Like by :\n1. Id \n2. Name \n3. Exit')
                        lch = int(input('Enter your choice: '))
                        if lch == 1:
                            ch = input('Enter ID to search for in id (e.g., "1"): ')
                            cursor.execute('SELECT * FROM product WHERE p_id LIKE %s ORDER BY price DESC', (f'%{ch}%',))
                            data = cursor.fetchall()
                            print('{:<10}{:<10}{:<10}{:<10}'.format('ID', 'Name', 'price', 'quantity'))
                            print('-' * 75)
                            if data:
                                for row in data:
                                    print("{:<10}{:<10}{:<10}{:<10}".format(row[0], row[1], row[2], row[3]))
                            else:
                                print('No matching records found')



                        elif lch ==2:


                            ch = input('Enter ID to search for in name (e.g., "Bla"): ')
                            cursor.execute('SELECT * FROM product WHERE name LIKE %s ORDER BY price DESC', (f'%{ch}%',))
                            data = cursor.fetchall()
                            print('{:<10}{:<10}{:<10}{:<10}'.format('ID', 'Name', 'price', 'quantity'))
                            print('-' * 75)
                            if data:
                                for row in data:
                                    print("{:<10}{:<10}{:<10}{:<10}".format(row[0], row[1], row[2], row[3]))
                            else:
                                print('No matching records found')

                        elif lch ==3:
                            
                            break
                        else:
                            print("Invalid input !")


                elif viewch == 3:
                    while True:
                        cursor.execute('SELECT name, MAX(price) AS max_price FROM product GROUP BY name')
                        data = cursor.fetchall()
                        print('{:<20}{:<10}'.format('Name', 'Max price'))
                        print('-' * 30)
                        if data:
                            for row in data:
                                print("{:<20}{:<10}".format(row[0], row[1]))
                        else:
                            print('No data available')
                elif viewch == 4:
                    break
                else :
                    print("Invalid input !")
                
        else:
            print("No product found.")

    elif ch == 6:
        ch=input("Enter the product name to by")
        #buy product
        #if the product is out of stock, print it is out of stock
        #if it is avialable, input the quantity and calculate price
        #show the product quantity after buying

    elif ch == 7:
        break

    else:
        print("Invalid choice. Please try again.")

cursor.close()
em.close()
