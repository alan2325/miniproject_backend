# main.py
import user
from ticket import TicketBooking

def main():
    ticket_booking = TicketBooking()
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if user.register_user(username, password):
                print("Registration successful!")
            else:
                print("Username already exists!")
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if user.login_user(username, password):
                print("Login successful!")
                while True:
                    print("1. Book Ticket")
                    print("2. View Tickets")
                    print("3. Logout")
                    user_choice = input("Enter your choice: ")
                    if user_choice == '1':
                        source = input("Enter source: ")
                        destination = input("Enter destination: ")
                        ticket = ticket_booking.book_ticket(username, source, destination)
                        print(f"Ticket booked successfully! Ticket ID: {ticket['ticket_id']}")
                    elif user_choice == '2':
                        tickets = ticket_booking.view_tickets(username)
                        if tickets:
                            print("Your tickets:")
                            for ticket in tickets:
                                print(f"Ticket ID: {ticket['ticket_id']}, Source: {ticket['source']}, Destination: {ticket['destination']}")
                        else:
                            print("No tickets found.")
                    elif user_choice == '3':
                        print("Logged out.")
                        break
                    else:
                        print("Invalid choice!")
            else:
                print("Invalid username or password!")
        elif choice == '3':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()