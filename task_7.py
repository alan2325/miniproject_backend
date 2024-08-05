import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="alan",
        password="alan2325",
        database="supermarket"
    )

# CREATE DATABASE supermarket;

# USE supermarket;



# CREATE TABLE products (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(100) NOT NULL,
#     price DECIMAL(10, 2) NOT NULL,
#     quantity INT NOT NULL
# );
def insert_product(name, price, quantity):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)",
        (name, price, quantity)
    )
    conn.commit()
    cursor.close()
    conn.close()
def update_product(product_id, name=None, price=None, quantity=None):
    conn = connect()
    cursor = conn.cursor()
    query = "UPDATE products SET"
    fields = []
    values = []

    if name:
        fields.append(" name = %s")
        values.append(name)
    if price:
        fields.append(" price = %s")
        values.append(price)
    if quantity:
        fields.append(" quantity = %s")
        values.append(quantity)

    query += ",".join(fields) + " WHERE id = %s"
    values.append(product_id)
    
    cursor.execute(query, tuple(values))
    conn.commit()
    cursor.close()
    conn.close()
def delete_product(product_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
    conn.commit()
    cursor.close()
    conn.close()
def buy_product(product_id, quantity):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT quantity, price FROM products WHERE id = %s", (product_id,))
    result = cursor.fetchone()
    
    if result:
        available_quantity, price = result
        if available_quantity >= quantity:
            new_quantity = available_quantity - quantity
            cursor.execute("UPDATE products SET quantity = %s WHERE id = %s", (new_quantity, product_id))
            conn.commit()
            total_cost = price * quantity
            print(f"Purchase successful! Total cost: ${total_cost}")
        else:
            print("Not enough stock available.")
    else:
        print("Product not found.")
    
    cursor.close()
    conn.close()
def main():
    while True:
        print("\nSupermarket Management System\n1. Insert Product\n2. Update Product\n3. Delete Product\n4. Buy Product\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            insert_product(name, price, quantity)
        elif choice == '2':
            product_id = int(input("Enter product ID to update: "))
            name = input("Enter new name (leave blank to keep unchanged): ")
            price = input("Enter new price (leave blank to keep unchanged): ")
            quantity = input("Enter new quantity (leave blank to keep unchanged): ")
            update_product(
                product_id,
                name if name else None,
                float(price) if price else None,
                int(quantity) if quantity else None
            )
        elif choice == '3':
            product_id = int(input("Enter product ID to delete: "))
            delete_product(product_id)
        elif choice == '4':
            product_id = int(input("Enter product ID to buy: "))
            quantity = int(input("Enter quantity to buy: "))
            buy_product(product_id, quantity)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

main()