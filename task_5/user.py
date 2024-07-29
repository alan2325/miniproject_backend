
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class UserManager:
    def __init__(self):
        self.users = {}

    def register_user(self, username, password):
        if username in self.users:
            print("Username already exists.")
        else:
            self.users[username] = User(username, password)
            print("User registered successfully.")

    def login_user(self, username, password):
        if username in self.users and self.users[username].password == password:
            print("Login successful.")
            return self.users[username]
        else:
            print("Invalid username or password.")
            return None
