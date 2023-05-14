from datetime import datetime
from dataclasses import dataclass, field
import json


@dataclass
class Customer:
    name: str
    credit: int = 0

    def addCredit(self, amount):
        self.credit += amount


@dataclass
class TravelCompany:  # Firma
    name: str
    wayOfTravel: str
    tickets: list = field(default_factory=list)


@dataclass
class Hotel:
    name: str
    region: str  # city name, Bolge
    address: str
    bookings: list = field(default_factory=list)  # one to many


@dataclass
class Booking:  # abstract, but avoid inheritance with hotel and ticket
    bookingNumber: str
    destination: str
    departureDate: datetime
    returnDate: datetime | None
    passengers: int
    price: int
    bonus: int


@dataclass
class Ticket(Booking):
    travelCompany: TravelCompany
    departureCity: str  # from city


@dataclass
class HotelBooking(Booking):
    hotel: Hotel  # many to one relationship


@dataclass
class Agency:
    name: str
    bookings: list[Booking] = field(default_factory=list)
    customers: list[Customer] = field(default_factory=list)
    travelCompanies: list[TravelCompany] = field(default_factory=list)
    hotels: list[Hotel] = field(default_factory=list)
    # kasa: int = 0

    def addCustomer(self, customer: Customer):
        self.customers.append(customer)

    def addTravelCompany(self, travelCompany: TravelCompany):
        self.travelCompanies.append(travelCompany)

    def addHotel(self, hotel: Hotel):
        self.hotels.append(hotel)

    def findAvailableBookings(self, destination, departureDate) -> list[Booking]:
        availableBookings = []
        for booking in self.bookings:
            if (
                booking.destination == destination
                and booking.departureDate == departureDate
            ):
                availableBookings.append(booking)
        return availableBookings

    def book(self, booking: Booking):
        self.bookings.append(booking)
        # customer.addCredit(booking.price * 2/100)

    def cancelBooking(self, booking: Booking):
        if booking in self.bookings:
            self.bookings.remove(booking)

    def addCredit(self, customer: Customer, amount: int):
        customer.addCredit(amount)

    def getCredit(self, customer: Customer):
        return customer.credit


if __name__ == "__main__":
    agency = Agency("My Travel Agency")

    customers = [Customer("John", "john@doe.com"), Customer("Jane", "jane@doe.com")]
    for customer in customers:
        agency.addCustomer(customer)

    travelCompanies = [TravelCompany("THY", "Plane"), TravelCompany("TCDD", "Ferry")]
    for travelCompany in travelCompanies:
        agency.addTravelCompany(travelCompany)

    hotels = [
        Hotel("Hilton", "Istanbul", "Beyoglu, Istanbul"),
        Hotel("Mariott", "Ankara", "Merkez, Ankara"),
        Hotel("Mariott", "Istanbul", "Beyoglu, Istanbul"),
    ]
    for hotel in hotels:
        agency.addHotel(hotel)

    bookings = [
        Ticket(
            destination="Istanbul",
            departureDate=datetime(2023, 7, 1),
            returnDate=datetime(2023, 7, 8),
            passengers=2,
            price=100,
            ticketNumber="123456",
            travelCompany=travelCompanies[0],
            departureCity="London",
        ),
        Ticket(
            destination="Frankfurt",
            departureDate=datetime(2023, 7, 3),
            returnDate=datetime(2023, 7, 10),
            passengers=2,
            price=100,
            ticketNumber="654321",
            travelCompany=travelCompanies[0],
            departureCity="Istanbul",
        ),
    ]
    for booking in bookings:
        agency.book(booking)

    # bookingOptions = BookingOptions(
    #     destination="Istanbul",
    #     departureDate=datetime(2023, 7, 1),
    #     returnDate=datetime(2023, 7, 8),
    #     passengers=2,
    # )

    print(
        agency.findAvailableBookings(
            destination="Istanbul", departureDate=datetime(2023, 7, 1)
        )
    )

    agency.cancelBooking(bookings[0])

    print(
        agency.findAvailableBookings(
            destination="Istanbul", departureDate=datetime(2023, 7, 1)
        )
    )
