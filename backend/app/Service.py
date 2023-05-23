from Domain import Ticket, HotelBooking, Booking, TravelCompany, Hotel, Agency, Customer
from Repository import Repository

# from flask import Flask, request, jsonify

"""
This document is for the implementation of the Agency Service
"""


class Service:
    def __init__(self) -> None:
        self.repository = Repository()
        self.agency = Agency("Celebi Travel Agency")

    # -- Agency --
    def getAgency(self):
        return self.agency

    def getAgencyKasa(self):
        return self.agency.kasa

    # def getAgencyBookings(self):
    #     return self.agency.bookings

    # def getAgencyCustomers(self):
    #     return self.agency.customers

    # def getAgencyTravelCompanies(self):
    #     return self.agency.travelCompanies

    # def getAgencyHotels(self):
    #     return self.agency.hotels

    # -- Customer --
    def addCustomer(self, customerName):
        customer = Customer(customerName)
        customerID = self.repository.createCustomer(customer)
        if not customerID:
            return None

        return customerID

    def getCustomer(self, customerID):
        return self.repository.getCustomer(customerID)

    def getCustomerByName(self, customerName):
        return self.repository.getCustomerByName(customerName)

    def addCustomerBonus(self, customerID, bonus):
        customer = self.getCustomer(customerID)
        customer.bonus += bonus
        self.repository.updateCustomerBonus(customerID, customer.bonus)

    def deleteCustomer(self, customerID):
        self.repository.deleteCustomer(customerID)

    # -- Travel Company --
    def addTravelCompany(self, travelCompany):
        travelCompanyID = self.repository.createTravelCompany(travelCompany)
        if not travelCompanyID:
            return None

        for ticket in travelCompany.tickets:
            self.repository.createTransport(ticket)

        return travelCompanyID

    def getTravelCompany(self, travelCompanyID):
        return self.repository.getTravelCompany(travelCompanyID)

    def getTravelCompanyByName(self, travelCompanyName):
        return self.repository.getTravelCompanyByName(travelCompanyName)

    def deleteTravelCompany(self, travelCompanyID):
        travelCompany = self.repository.getTravelCompany(travelCompanyID)

        if travelCompany == None:
            print("ERR: Travel company not found")
            return None

        for ticket in travelCompany.tickets:
            self.repository.deleteTransport(ticket.id)

        self.repository.deleteTravelCompany(travelCompanyID)

    # -- Hotel --
    def addHotel(self, hotel):
        hotelID = self.repository.createHotel(hotel)
        if not hotelID:
            return None

        for hotelBooking in hotel.hotelBookings:
            self.repository.createHotelStay(hotelBooking)

        return hotelID

    def getHotel(self, hotelID):
        return self.repository.getHotel(hotelID)

    def getHotelByName(self, hotelName):
        return self.repository.getHotelByName(hotelName)

    def deleteHotel(self, hotelID):
        hotel = self.repository.getHotel(hotelID)

        if hotel == None:
            print("ERR: Hotel not found")
            return

        for hotelBooking in hotel.hotelBookings:
            self.repository.deleteHotelStay(hotelBooking.id)

        self.repository.deleteHotel(hotelID)

    # -- Ticket -- (Transport)
    def addTicket(self, ticket):
        ticketID = self.repository.createTransport(ticket)
        if not ticketID:
            return None

        self.repository.createTransport(ticket)
        return ticketID

    def getTicket(self, ticketID):
        return self.repository.getTransport(ticketID)

    def getAllTicketsBy(self, travelCompany=None, tFrom=None, tTo=None, tDatetime=None):
        return self.repository.getAllTransportsBy(travelCompany, tFrom, tTo, tDatetime)

    def deleteTicket(self, ticketID):
        self.repository.deleteTransport(ticketID)

    # -- Hotel Stay --
    def addHotelStay(self, hotelStay):
        hotelStayID = self.repository.createHotelStay(hotelStay)
        if not hotelStayID:
            return None

        self.repository.createHotelStay(hotelStay)
        return hotelStayID

    def getHotelStay(self, hotelStayID):
        return self.repository.getHotelStay(hotelStayID)

    def getAllHotelStaysBy(self, hotel=None, fromDate=None, toDate=None):
        return self.repository.getAllHotelStaysBy(hotel, fromDate, toDate)

    def deleteHotelStay(self, hotelStayID):
        self.repository.deleteHotelStay(hotelStayID)

        # -- Booking --

    def bookTicket(self, ticketID, customerID, numOfPassengers):
        ticket = self.repository.getTicket(ticketID)
        bonus = self.repository.getTravelCompany(ticket.travelCompany).bonus
        customer = self.repository.getCustomer(customerID)
        if ticket == None or customer == None:
            print("ERR: Ticket or customer not found")
            return None

        booking = Booking(
            customer=customerID,
            typeOfBooking="T",
            transport=ticket,
            fromDate=ticket.tDatetime,
            toDate=ticket.tDatetime,
            numOfPassengers=numOfPassengers,
            totalPrice=ticket.tPrice * numOfPassengers,
            totalBonus=bonus * numOfPassengers,
        )

        bookingID = self.repository.createBooking(ticket, customer)
        if not bookingID:
            return None

        self.agency.kasa += booking.totalPrice

        return bookingID

    def bookHotel(self, hotelStayID, customerID, numOfPassengers):
        hotelStay = self.repository.getHotelStay(hotelStayID)
        bonus = self.repository.getHotel(hotelStay.hotel).bonus
        customer = self.repository.getCustomer(customerID)
        if hotelStay == None or customer == None:
            print("ERR: Hotel stay or customer not found")
            return None

        totalPrice = hotelStay.price * numOfPassengers
        totalBonus = bonus * numOfPassengers

        booking = Booking(
            customer=customerID,
            typeOfBooking="H",
            hotelStay=hotelStay,
            fromDate=hotelStay.fromDate,
            toDate=hotelStay.toDate,
            numOfPassengers=numOfPassengers,
            totalPrice=totalPrice,
            totalBonus=totalBonus,
        )

        bookingID = self.repository.createBooking(hotelStay, customer)
        if not bookingID:
            return None

        self.agency.kasa += booking.totalPrice

        return bookingID

    def cancelBooking(self, bookingID):
        booking = self.repository.getBooking(bookingID)
        if booking == None:
            print("ERR: Booking not found")
            return None

        # subtract bonus from customer
        customer = self.repository.getCustomer(booking.customer)
        customer.bonus -= booking.totalBonus
        self.repository.updateCustomerBonus(customer.id, customer.bonus)

        self.agency.kasa -= booking.totalPrice

        self.repository.deleteBooking(bookingID)
