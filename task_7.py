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
        quantity INT
    )
''')

while True:
    print('\n1. Add product\n2. Update product\n3. Delete\n4. Search\n5. View all\n6. Buy\n7. Exit')
    try:
        ch = int(input('Enter your choice: '))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if ch == 1:
        try:
            l = int(input("Enter the number of products to add: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        for _ in range(l):
            print('_' * 50)
            try:
                p_id = int(input('Enter product ID: '))
                name = input('Enter name: ')
                price = int(input('Enter price: '))
                quantity = int(input("Enter quantity: "))
            except ValueError:
                print("Invalid input. Please enter valid data.")
                continue

            cursor.execute('''
                INSERT INTO product (p_id, name, price, quantity)
                VALUES (%s, %s, %s, %s)
            ''', (p_id, name, price, quantity))
            em.commit()

    elif ch == 2:
        try:
            p_id = int(input("Enter the ID of the product to update: "))
            cursor.execute("SELECT * FROM product WHERE p_id = %s", (p_id,))
            product = cursor.fetchone()

            if product:
                print('_' * 50)
                new_name = input(f'Enter new name (current: {product[1]}): ')
                new_price = int(input(f'Enter new price (current: {product[2]}): '))
                new_quantity = int(input(f'Enter new quantity (current: {product[3]}): '))

                cursor.execute('''
                    UPDATE product
                    SET name = %s, price = %s, quantity = %s
                    WHERE p_id = %s
                ''', (new_name, new_price, new_quantity, p_id))
                em.commit()
                print("Updated successfully!")
            else:
                print("Product ID not found.")
        except ValueError:
            print("Invalid input. Please enter valid data.")

    elif ch == 3:
        try:
            p_id = int(input("Enter the ID of the product to delete: "))
            cursor.execute("DELETE FROM product WHERE p_id = %s", (p_id,))
            em.commit()
            print("Deleted successfully!")
        except ValueError:
            print("Invalid input. Please enter a valid ID.")

    elif ch == 4:
        try:
            p_id = int(input("Enter the ID of the product to search: "))
            cursor.execute("SELECT * FROM product WHERE p_id = %s", (p_id,))
            product = cursor.fetchone()

            if product:
                print('_' * 50)
                print(f'ID: {product[0]}')
                print(f'Name: {product[1]}')
                print(f'Price: {product[2]}')
                print(f'Quantity: {product[3]}')
            else:
                print("Product ID not found.")
        except ValueError:
            print("Invalid input. Please enter a valid ID.")

    elif ch == 5:
        cursor.execute("SELECT * FROM product")
        products = cursor.fetchall()

        if products:
            while True:
                try:
                    viewch = int(input('View by:\n1. Order\n2. Like\n3. Group By\n4. Exit\nEnter your choice: '))

                    if viewch == 1:
                        while True:
                            try:
                                print('Order by:\n1. ID\n2. Name\n3. Exit')
                                och = int(input('Enter your choice: '))

                                if och == 1:
                                    cursor.execute("SELECT * FROM product ORDER BY p_id")
                                elif och == 2:
                                    cursor.execute("SELECT * FROM product ORDER BY name")
                                elif och == 3:
                                    break
                                else:
                                    print("Invalid choice. Please try again.")
                                    continue

                                products = cursor.fetchall()
                                print("{:<10}{:<20}{:<10}{:<10}".format("ID", "Name", "Price", "Quantity"))
                                print('-' * 50)
                                for p in products:
                                    print("{:<10}{:<20}{:<10}{:<10}".format(p[0], p[1], p[2], p[3]))
                                print()

                            except ValueError:
                                print("Invalid input. Please enter a valid number.")

                    elif viewch == 2:
                        while True:
                            try:
                                print('Like by:\n1. ID\n2. Name\n3. Exit')
                                lch = int(input('Enter your choice: '))

                                if lch == 1:
                                    ch = input('Enter ID pattern to search (e.g., "1"): ')
                                    cursor.execute('SELECT * FROM product WHERE p_id LIKE %s ORDER BY price DESC', (f'%{ch}%',))
                                elif lch == 2:
                                    ch = input('Enter name pattern to search (e.g., "Bla"): ')
                                    cursor.execute('SELECT * FROM product WHERE name LIKE %s ORDER BY price DESC', (f'%{ch}%',))
                                elif lch == 3:
                                    break
                                else:
                                    print("Invalid choice. Please try again.")
                                    continue

                                data = cursor.fetchall()
                                print('{:<10}{:<20}{:<10}{:<10}'.format('ID', 'Name', 'Price', 'Quantity'))
                                print('-' * 50)
                                if data:
                                    for row in data:
                                        print("{:<10}{:<20}{:<10}{:<10}".format(row[0], row[1], row[2], row[3]))
                                else:
                                    print('No matching records found')

                            except ValueError:
                                print("Invalid input. Please enter a valid number.")

                    elif viewch == 3:
                        cursor.execute('SELECT name, MAX(price) AS max_price FROM product GROUP BY name')
                        data = cursor.fetchall()
                        print('{:<20}{:<10}'.format('Name', 'Max Price'))
                        print('-' * 30)
                        if data:
                            for row in data:
                                print("{:<20}{:<10}".format(row[0], row[1]))
                        else:
                            print('No data available')
                    elif viewch == 4:
                        break
                    else:
                        print("Invalid choice. Please try again.")
                
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

        else:
            print("No product found.")

    elif ch == 6:
        try:
            name = input("Enter the product name to buy: ")
            quantity = int(input("Enter the quantity to buy: "))

            cursor.execute("SELECT * FROM product WHERE name = %s", (name,))
            product = cursor.fetchone()

            if product:
                p_id, p_name, price, stock = product
                if stock >= quantity:
                    total_price = price * quantity
                    new_stock = stock - quantity

                    cursor.execute('''
                        UPDATE product
                        SET quantity = %s
                        WHERE p_id = %s
                    ''', (new_stock, p_id))
                    em.commit()
                    print(f"Purchase successful! Total price: {total_price}")
                else:
                    print("Insufficient stock.")
            else:
                print("Product not found.")
        except ValueError:
            print("Invalid input. Please enter a valid quantity.")

    elif ch == 7:
        break

    else:
        print("Invalid choice. Please try again.")

cursor.close()
em.close()
