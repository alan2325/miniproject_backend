
class Accessory:
    def __init__(self, accessory_id, name, price):
        self.accessory_id = accessory_id
        self.name = name
        self.price = price

class AccessoryManager:
    def __init__(self):
        self.accessories = {}

    def add_accessory(self, accessory_id, name, price):
        if accessory_id in self.accessories:
            print("Accessory ID already exists.")
        else:
            self.accessories[accessory_id] = Accessory(accessory_id, name, price)
            print("Accessory added successfully.")

    def remove_accessory(self, accessory_id):
        if accessory_id in self.accessories:
            del self.accessories[accessory_id]
            print("Accessory removed successfully.")
        else:
            print("Accessory ID not found.")

    def view_accessories(self):
        if not self.accessories:
            print("No accessories available.")
        else:
            for accessory_id, accessory in self.accessories.items():
                print(f"ID: {accessory_id}, Name: {accessory.name}, Price: ${accessory.price}")

    def borrow_accessory(self, user, accessory_id):
        if accessory_id in self.accessories:
            print(f"Accessory '{self.accessories[accessory_id].name}' borrowed by {user.username}.")
        else:
            print("Accessory ID not found.")

    def return_accessory(self, user, accessory_id):
        if accessory_id in self.accessories:
            print(f"Accessory '{self.accessories[accessory_id].name}' returned by {user.username}.")
        else:
            print("Accessory ID not found.")
