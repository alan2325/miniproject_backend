# from storage import users


# def login():
#     username = input("Enter username: ")
#     password = input("Enter password: ")
    
#     if username in users and users[username] == password:
#         print("Login successful!")
#         return True
#     else:
#         print("Invalid username or password.")
#         return False


from storage import users

def reg():
    username = input("Enter new username: ")
    if username in users:
        print("Username already exists. Please choose another one.")
        return False
    
    password = input("Enter password: ")
    users[username] = password
    print("Registration successful!")
    return True

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username in users and users[username] == password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False
