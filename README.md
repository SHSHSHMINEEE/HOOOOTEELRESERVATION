from hotel_system import Hotel
from room import Room
from booking import Booking
from guest import Guest
from admin import Admin
from feedback import Feedback
from loyaltyprogram import LoyaltyProgram
from payment import Payment
from invoice import Invoice

def test_hotel_room_booking():
    print("\n========== Test: Hotel, Room & Booking ==========")
    room1 = Room(101, "Deluxe", 300.0, ["WiFi", "TV"], True, 4.5)
    room2 = Room(102, "Suite", 500.0, ["WiFi", "Jacuzzi"], True, 4.8)
    hotel = Hotel("Royal Stay", "Corniche", "Doha", "Open", "12345678", 4.7, [room1, room2])
    print(hotel)

    guest = Guest("G001", "Sara", "sara@gmail.com", "77712345", "Qatar", True, [], [], [])
    booking = Booking(1, guest, room1, "2025-03-25", "2025-03-28", 1, 0.0, True)
    booking.setTotalCharges(booking.calculateCharges())
    print(booking.confirmBooking())
    print(room1.bookRoom())
    print(booking)

def test_user_and_feedback():
    print("\n========== Test: Guest, Admin & Feedback ==========")
    guest = Guest("G002", "Ali", "ali@gmail.com", "55599887", "Qatar", True, [], [], [])
    print(guest.createAccount())
    print(guest.updateProfile())
    print(guest.viewReservation())

    admin = Admin("A001", "Manager Zayed", "admin@royalstay.com", "55667788", "Qatar", "Supervisor", ["edit_room", "delete_room"])
    print(admin.manageRooms())

    feedback = Feedback(1, 5.0, "Excellent service!", datetime.now())
    print(feedback.submitFeedBack())
    print(feedback)

def test_loyalty_program():
    print("\n========== Test: Loyalty Program ==========")
    guest = Guest("G003", "Mariam", "mariam@gmail.com", "55991100", "Qatar", True, [], [], [])
    loyalty = LoyaltyProgram(101, guest, 120)
    print(loyalty.displayReward())
    print(loyalty.updateRewards(30))
    print(loyalty)

def test_payment_and_invoice():
    print("\n========== Test: Payment & Invoice ==========")
    guest = Guest("G004", "Nasser", "nasser@gmail.com", "55334422", "Qatar", True, [], [], [])
    room = Room(103, "Standard", 250.0, ["WiFi"], True, 4.0)
    booking = Booking(2, guest, room, "2025-03-27", "2025-03-30", 1, 0.0, True)
    booking.setTotalCharges(booking.calculateCharges())

    payment = Payment(5001, booking.getTotalCharges(), "Credit Card", "Doha", "2025-03-24", "Completed")
    print(payment.processPayment())
    print(payment)

    invoice = Invoice(3001, booking, booking.getTotalCharges(), 10, 20.0)
    print(invoice.generateInvoice())
    print(invoice)

def main():
    test_hotel_room_booking()
    test_user_and_feedback()
    test_loyalty_program()
    test_payment_and_invoice()

main()

