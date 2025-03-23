class Hotel:
    """
    Represents a Hotel which consists of multiple rooms and basic details.
    """
    def __init__(self, name, location, city, status, phoneNumber, rating, roomList):
        self._name = name
        self._location = location
        self._city = city
        self._status = status
        self._phoneNumber = phoneNumber
        self._rating = rating
        self._roomList = roomList  # List of Room objects

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getLocation(self):
        return self._location

    def setLocation(self, location):
        self._location = location

    def getCity(self):
        return self._city

    def setCity(self, city):
        self._city = city

    def getStatus(self):
        return self._status

    def setStatus(self, status):
        self._status = status

    def getPhoneNumber(self):
        return self._phoneNumber

    def setPhoneNumber(self, phoneNumber):
        self._phoneNumber = phoneNumber

    def getRating(self):
        return self._rating

    def setRating(self, rating):
        self._rating = rating

    def getRoomList(self):
        return self._roomList

    def setRoomList(self, roomList):
        self._roomList = roomList

    def calculateAverageRating(self):
        # Placeholder for average rating calculation
        return self._rating

    def __str__(self):
        return f"Hotel: {self._name}\n
        Location: {self._location}, {self._city}\n
        Status: {self._status}\n
        Phone: {self._phoneNumber}\n
        Rating: {self._rating}\n
        Rooms Count: {len(self._roomList)}"


class Room:
    """
    Represents a Room in the Hotel.
    """
    def __init__(self, roomNumber, roomType, pricePerNight, amenities, availability, rate):
        self._roomNumber = roomNumber
        self._roomType = roomType
        self._pricePerNight = pricePerNight
        self._amenities = amenities  # List of amenities
        self._availability = availability
        self._rate = rate

    def getRoomNumber(self):
        return self._roomNumber

    def setRoomNumber(self, roomNumber):
        self._roomNumber = roomNumber

    def getRoomType(self):
        return self._roomType

    def setRoomType(self, roomType):
        self._roomType = roomType

    def getPricePerNight(self):
        return self._pricePerNight

    def setPricePerNight(self, pricePerNight):
        self._pricePerNight = pricePerNight

    def getAmenities(self):
        return self._amenities

    def setAmenities(self, amenities):
        self._amenities = amenities

    def getAvailability(self):
        return self._availability

    def setAvailability(self, availability):
        self._availability = availability

    def getRate(self):
        return self._rate

    def setRate(self, rate):
        self._rate = rate

    def checkAvailability(self):
        return self._availability

    def bookRoom(self):
        if self._availability:
            self._availability = False
            return f"Room {self._roomNumber} successfully booked."
        return f"Room {self._roomNumber} is not available."

    def __str__(self):
        return (f"Room Info:\n
        Room Number: {self._roomNumber}\n
        Room Type: {self._roomType}\n
        Price/Night: {self._pricePerNight}\n
        Rate: {self._rate}\n
        Available: {self._availability}\n
        Amenities: {', '.join(self._amenities)}"


class User:
    """
    Base class for any user of the hotel system.
    """
    def __init__(self, userId, name, email, phoneNumber, nationality):
        self._userId = userId
        self._name = name
        self._email = email
        self._phoneNumber = phoneNumber
        self._nationality = nationality

    def getUserId(self):
        return self._userId
    def setUserId(self, userId):
        self._userId = userId

    def getName(self):
        return self._name
    def setName(self, name):
        self._name = name

    def getEmail(self):
        return self._email
    def setEmail(self, email):
        self._email = email

    def getPhoneNumber(self):
        return self._phoneNumber
    def setPhoneNumber(self, phoneNumber):
        self._phoneNumber = phoneNumber

    def getNationality(self):
        return self._nationality
    def setNationality(self, nationality):
        self._nationality = nationality

    def login(self):
        return f"User {self._userId} logged in."

    def __str__(self):
        return f"User Info:\n
        ID: {self._userId}\n
        Name: {self._name}\n
        Email: {self._email}\n
        Nationality: {self._nationality}"


class Guest(User):
    """
    Represents a Guest, inherits from User.
    """
    def __init__(self, userId, name, email, phoneNumber, nationality, loyaltyStatus, bookingsList, loyaltyList, feedbackList):
        super().__init__(userId, name, email, phoneNumber, nationality)
        self._loyaltyStatus = loyaltyStatus
        self._bookingsList = bookingsList  # List of Booking
        self._loyaltyList = loyaltyList    # List of LoyaltyProgram
        self._feedbackList = feedbackList  # List of Feedback

    def getLoyaltyStatus(self):
        return self._loyaltyStatus
    def setLoyaltyStatus(self, loyaltyStatus):
        self._loyaltyStatus = loyaltyStatus

    def getBookingsList(self):
        return self._bookingsList
    def setBookingsList(self, bookingsList):
        self._bookingsList = bookingsList

    def getloyaltyList(self):
        return self._loyaltyList
    def setloyaltyList(self, loyaltyList):
        self._loyaltyList = loyaltyList

    def getFeedbackList(self):
        return self._feedbackList
    def setFeedbackList(self, feedbackList):
        self._feedbackList = feedbackList

    def makeBookings(self, booking):
        self._bookingsList.append(booking)
        return f"Booking {booking} added."

    def viewRewards(self):
        return f"Rewards available: {len(self._loyaltyList)} entries."

    def searchRoomAvailability(self):
        return True

    def addService(self):
        return ["Wifi", "Room Service","Gym Access", "Laundry"]

    def createAccount(self):
        return f"Guest account created for {self._name}"

    def updateProfile(self):
        return f"Profile updated for {self._name}"

    def viewReservation(self):
        return f"You have {len(self._bookingsList)} reservations."
    def __str__(self):
        return f"Guest({self._name}\n
        Loyalty: {self._loyaltyStatus}\n 
        Bookings: {len(self._bookingsList)})"

class Admin(User):
    """
    Represents an Admin, inherits from User.
    """
    def __init__(self, userId, name, email, phoneNumber, nationality, role, permissions):
        super().__init__(userId, name, email, phoneNumber, nationality)
        self._role = role
        self._permissions = permissions

    def getRole(self):
        return self._role
    def setRole(self, role):
        self._role = role

    def getPermission(self):
        return self._permissions
    def setPermission(self, permissions):
        self._permissions = permissions

    def manageRooms(self):
        return "Admin is managing rooms."

    def __str__(self):
        return f"Admin Info: {self._name}\n
        Role: {self._role}\n
        Permissions: {self._permissions}"
        
class Feedback:
    """Represents guest feedback on the stay."""
    def __init__(self, feedbackId, rating, comments, datetime):
        self._feedbackId = feedbackId
        self._rating = rating
        self._comments = comments
        self._datetime = datetime

    def getFeedbackId(self):
        return self._feedbackId
    def setFeedbackId(self, feedbackId):
        self._feedbackId = feedbackId

    def getRating(self):
        return self._rating
    def setRating(self, rating):
        self._rating = rating

    def getComments(self):
        return self._comments
    def setComments(self, comments):
        self._comments = comments

    def getDateTime(self):
        return self._datetime
    def setDateTime(self, datetime):
        self._datetime = datetime

    def submitFeedBack(self):
        return "Feedback submitted successfully."

def __str__(self):
        return f"Feedback({self._feedbackId}\n 
        Rating: {self._rating}\n
        Date: {self._datetime})"


class LoyaltyProgram:
    """Represents loyalty program membership for a guest."""
    def __init__(self, loyaltyId, guest, points):
        self._loyaltyId = loyaltyId
        self._guest = guest
        self._points = points

    def getLoyaltyId(self):
        return self._loyaltyId
    def setLoyaltyId(self, loyaltyId):
        self._loyaltyId = loyaltyId

    def getGuest(self):
        return self._guest
    def setGuest(self, guest):
        self._guest = guest

    def getPoints(self):
        return self._points
    def setPoints(self, points):
        self._points = points

    def updateRewards(self, points):
        self._points += points
        return "Rewards updated."

    def displayReward(self):
        return self._points
  
    def __str__(self):
        return f"LoyaltyProgram:\n
        ID: {self._loyaltyId}\n 
        Guest: {self._guest.getName()}\n
        Points: {self._points})"
