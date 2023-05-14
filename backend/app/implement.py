from Domain import Ticket, HotelBooking, Booking, TravelCompany, Hotel, Agency, Customer

# from flask import Flask, request, jsonify

"""
This document is for the implementation of all CRUD functionalities on the database.
"""


class Service:
    # -- Booking --
    def createBooking(
        destination, departureDate, returnDate, passengers, price, departureCity
    ):
        pass

    def getBooking(bookingNumber):
        pass

    def deleteBooking(bookingNumber):
        pass

    def updateBookingPrice(bookingNumber, newPrice):
        pass

    # infinite arguments
    def findAllBookingsBy(*args):
        # build query from args
        query = "SELECT * FROM Booking WHERE "
        for arg in args:
            pass

        # execute query

        # return results

        pass

    # -- Ticket --
    def createTicket(
        travelCompany,
        departureCity,
        destination,
        departureDate,
        returnDate,
        passengers,
        price,
    ):
        # super()
        pass

    def getTicket(bookingNumber):
        pass

    def bookTicket(bookingNumber):
        pass

    def cancelTicket(bookingNumber):
        pass

    def createHotelBooking(
        hotel, destination, departureDate, returnDate, passengers, price
    ):
        # super()
        pass

    def getHotelBooking(bookingNumber):
        pass

    def bookHotel(bookingNumber):
        pass

    def cancelHotel(bookingNumber):
        pass

    def createTravelCompany(name, wayOfTravel):
        pass

    def createHotel(name, location, address):
        pass
