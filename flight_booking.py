from abc import ABC, abstractmethod

class Passenger(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @abstractmethod
    def get_discount_percent(self):
        pass
    def get_type(self):
        return self.__class__.__name__.replace("Passenger","")

class RegularPassenger(Passenger):
    def get_discount_percent(self): return 0

class StudentPassenger(Passenger):
    def get_discount_percent(self): return 10

class Flight:
    def __init__(self, code, airline, source, destination, seats, fare):
        self.code = code; self.airline = airline
        self.source = source; self.destination = destination
        self.available_seats = seats; self.base_fare = fare
    def display(self):
        print(f"{self.code} | {self.airline} | {self.source} -> {self.destination} | Seats: {self.available_seats} | Fare: Rs.{self.base_fare}")

class Booking:
    def __init__(self, booking_id, flight, passenger, tickets):
        self.booking_id = booking_id; self.flight = flight
        self.passenger = passenger; self.tickets = tickets
        self.subtotal = self.flight.base_fare * self.tickets
        self.discount_percent = self.passenger.get_discount_percent()
        self.discount_amount = (self.subtotal * self.discount_percent) / 100
        self.final_amount = self.subtotal - self.discount_amount
    def display_summary(self):
        print(f"\nBooking confirmed!\nBooking ID: {self.booking_id}\nFlight: {self.flight.code} | {self.flight.source} to {self.flight.destination}\nPassenger: {self.passenger.name}\nPassenger type: {self.passenger.get_type()}\nTickets: {self.tickets}\nBase fare per ticket: Rs.{self.flight.base_fare}\nSubtotal: Rs.{self.subtotal}\nDiscount ({self.discount_percent}%): Rs.{self.discount_amount}\nFinal amount: Rs.{self.final_amount}\n")

class FlightBookingSystem:
    def __init__(self):
        self.flights = [
            Flight("PN101", "Kiran Air", "Pune", "Delhi", 20, 4000),
            Flight("MB202", "Kiran Air", "Mumbai", "Bengaluru", 30, 3500),
            Flight("PN303", "Kiran Air", "Pune", "Hyderabad", 25, 3000),
        ]
        self.bookings = []; self.booking_counter = 1001
    def display_flights(self):
        print("\n--- Available Flights ---")
        for f in self.flights: f.display()
    def find_flight(self, code):
        for f in self.flights:
            if f.code.lower() == code.lower(): return f
        return None
    def validate_booking(self, flight, name, age, tickets):
        if not flight: print("Booking failed: Invalid flight code."); return False
        if not name.strip(): print("Booking failed: Name blank."); return False
        if age <= 0 or tickets <= 0: print("Booking failed: Invalid age/tickets."); return False
        if tickets > flight.available_seats:
            print(f"Booking failed: Not enough seats. Available: {flight.available_seats}"); return False
        return True
    def book_flight(self):
        code = input("Enter flight code: "); flight = self.find_flight(code)
        name = input("Enter passenger name: ")
        try: age = int(input("Enter age: "))
        except: print("Age number me likho"); return
        ptype = input("Passenger type (Regular/Student): ").lower()
        try: tickets = int(input("Enter number of tickets: "))
        except: print("Tickets number me likho"); return
        passenger = StudentPassenger(name, age) if ptype == "student" else RegularPassenger(name, age)
        if not self.validate_booking(flight, name, age, tickets): return
        flight.available_seats -= tickets
        booking_id = f"BK{self.booking_counter}"; self.booking_counter += 1
        booking = Booking(booking_id, flight, passenger, tickets)
        self.bookings.append(booking); booking.display_summary()
    def view_booking(self):
        if not self.bookings: print("\nNo bookings found."); return
        self.bookings[-1].display_summary()

def main():
    system = FlightBookingSystem()
    print("Welcome to Kiran Air Booking")
    while True:
        print("\n1. View Flights\n2. Book Flight\n3. View Booking\n4. Exit")
        choice = input("Enter choice: ")
        if choice == "1": system.display_flights()
        elif choice == "2": system.book_flight()
        elif choice == "3": system.view_booking()
        elif choice == "4": print("Thank you for using Kiran Air Booking!"); break
        else: print("Invalid choice.")

if __name__ == "__main__": main()