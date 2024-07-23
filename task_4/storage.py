donors = [
    {"id": 1, "name": "John Doe", "blood_group": "A+", "contact": "123-456-7890"},
    {"id": 2, "name": "Alice Smith", "blood_group": "A+", "contact": "123-456-7891"},
    {"id": 3, "name": "Bob Brown", "blood_group": "A-", "contact": "123-456-7892"},
    {"id": 4, "name": "Charlie Davis", "blood_group": "B+", "contact": "123-456-7893"},
    {"id": 5, "name": "Eve Clark", "blood_group": "B+", "contact": "123-456-7894"},
    {"id": 6, "name": "Grace Lee", "blood_group": "AB+", "contact": "123-456-7895"},
    {"id": 7, "name": "Henry Martin", "blood_group": "AB-", "contact": "123-456-7896"},
    {"id": 8, "name": "Ivy Nelson", "blood_group": "O+", "contact": "123-456-7897"},
    {"id": 9, "name": "Jack White", "blood_group": "O+", "contact": "123-456-7898"},
    {"id": 10, "name": "Kathy Harris", "blood_group": "O-", "contact": "123-456-7899"}
]
users = {
    "admin": "123"
}

def initialize_storage():
    global donors
    donors = []