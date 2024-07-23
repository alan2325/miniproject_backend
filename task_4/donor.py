from storage import donors

def add_donor():
    donor_id = input("Enter Donor ID: ")
    for donor in donors:
        if donor["id"] == donor_id:
            print("Donor ID already exists. Please enter a unique ID.")
            return
    name = input("Enter Donor Name: ")
    blood_group = input("Enter Blood Group: ")
    contact = input("Enter Contact Number: ")
    donors.append({"id": donor_id, "name": name, "blood_group": blood_group, "contact": contact})
    print("Donor added successfully!\n")

def view_donors():
    if donors:
        print("\n{:<10} {:<20} {:<15} {:<15}".format("ID", "Name", "Blood Group", "Contact"))
        print("-" * 60)
        for donor in donors:
            print("{:<10} {:<20} {:<15} {:<15}".format(donor['id'], donor['name'], donor['blood_group'], donor['contact']))
        print("")
    else:
        print("\nNo donors found!\n")

def search_donors_by_name(name):
    results = [donor for donor in donors if name.lower() in donor['name'].lower()]
    return results

def search_donors_by_blood_group(blood_group):
    results = [donor for donor in donors if donor['blood_group'].lower() == blood_group.lower()]
    return results

def display_search_results(results):
    if results:
        print("\n{:<10} {:<20} {:<15} {:<15}".format("ID", "Name", "Blood Group", "Contact"))
        print("-" * 60)
        for donor in results:
            print("{:<10} {:<20} {:<15} {:<15}".format(donor['id'], donor['name'], donor['blood_group'], donor['contact']))
        print("")
    else:
        print("\nNo matching donors found!\n")        

def update_donor():
    donor_id = input("Enter Donor ID to update: ")
    for donor in donors:
        if donor["id"] == donor_id:
            print("Current Name: " + donor['name'])
            new_name = input("Enter new name (leave blank to keep current): ")
            donor["name"] = new_name or donor["name"]

            print("Current Blood Group: " + donor['blood_group'])
            new_blood_group = input("Enter new blood group (leave blank to keep current): ")
            donor["blood_group"] = new_blood_group or donor["blood_group"]

            print("Current Contact: " + donor['contact'])
            new_contact = input("Enter new contact (leave blank to keep current): ")
            donor["contact"] = new_contact or donor["contact"]

            print("Donor updated successfully!\n")
            return
    print("Donor not found!\n")

def delete_donor():
    donor_id = input("Enter Donor ID to delete: ")
    for donor in donors:
        if donor["id"] == donor_id:
            donors.remove(donor)
            print("Donor deleted successfully!\n")
            return
    print("Donor not found!\n")