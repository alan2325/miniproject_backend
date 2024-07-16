# ticket.py
class TicketBooking:
    def __init__(self):
        self.tickets = []

    def book_ticket(self, username, source, destination):
        ticket_id = len(self.tickets) + 1
        ticket = {
            'ticket_id': ticket_id,
            'username': username,
            'source': source,
            'destination': destination
        }
        self.tickets.append(ticket)
        return ticket

    def view_tickets(self, username):
        return [ticket for ticket in self.tickets if ticket['username'] == username]