import psycopg2
from app.Domain import Customer, Hotel, HotelStay, Transport, TravelCompany, Booking


class Repository:
    def __init__(self) -> None:
        try:
            self.conn = psycopg2.connect(
                host="localhost",
                database="agencydb",
                user="postgres",
                password="postgres",
            )
        except:
            print("ERR: Unable to connect to the database")

    def __del__(self):
        self.conn.close()

    def createCustomer(self, customer):
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO customer (cName, totalPoints) VALUES (%s, %s) RETURNING cID;",
            (customer.name, 0),
        )
        self.conn.commit()
        customerID = cur.fetchone()[0]
        cur.close()
        return customerID

    def createTravelCompany(self, travelCompany):
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO travelcompany (tcName, wayoftravel, bonus) VALUES (%s, %s, %s) RETURNING tcID;",
            (travelCompany.name, travelCompany.wayOfTravel, travelCompany.bonus),
        )
        self.conn.commit()
        travelCompanyID = cur.fetchone()[0]
        cur.close()
        return travelCompanyID

    def createHotel(self, hotel):
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO hotel (hName, region, address, bonus) VALUES (%s, %s, %s, %s) RETURNING hID;",
            (hotel.name, hotel.region, hotel.address, hotel.bonus),
        )
        self.conn.commit()
        hotelID = cur.fetchone()[0]
        cur.close()
        return hotelID

    def createTransport(self, ticket):
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO transport (travelCompany, tFrom, tTo, tDatetime, tPrice) VALUES (%s, %s, %s, %s, %s) RETURNING tID;",
            (
                ticket.travelCompany,
                ticket.tFrom,
                ticket.tTo,
                ticket.tDatetime,
                ticket.tPrice,
            ),
        )
        self.conn.commit()
        ticketID = cur.fetchone()[0]
        cur.close()
        return ticketID

    def createHotelStay(self, hotelstay):
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO hotelstay (hotel, hsPrice) VALUES (%s, %s) RETURNING hsID;",
            (hotelstay.hotelID, hotelstay.price),
        )
        self.conn.commit()
        hotelStayID = cur.fetchone()[0]
        cur.close()
        return hotelStayID

    def createBooking(self, booking: Booking):
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO booking (customerID, typeOfBooking, hotelStay, transport, fromDate, toDate, numOfPassengers, totalPrice, totalBonus) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING bID;",
            (
                booking.customer,
                booking.typeOfBooking,
                booking.hotelStay,
                booking.transport,
                booking.fromDate,
                booking.toDate,
                booking.numOfPassengers,
                booking.totalPrice,
                booking.totalBonus,
            ),
        )
        bookingID = cur.fetchone()[0]
        self.conn.commit()
        return bookingID

    # READ
    def getCustomer(self, customerID):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM customer WHERE cID = %s", (customerID,))
        customer = Customer(*cur.fetchone())
        cur.close()
        return customer

    def getCustomerByName(self, customerName):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM customer WHERE cName = %s", (customerName,))
        customer = Customer(*cur.fetchone())
        cur.close()
        return customer

    def getTravelCompany(self, travelCompanyID):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM travelcompany WHERE tcID = %s", (travelCompanyID,))
        travelCompany = TravelCompany(*cur.fetchone())
        cur.close()
        return travelCompany

    def getTravelCompanyByName(self, travelCompanyName):
        cur = self.conn.cursor()
        cur.execute(
            "SELECT * FROM travelcompany WHERE tcName = %s", (travelCompanyName,)
        )
        travelCompany = TravelCompany(*cur.fetchone())
        cur.close()
        return travelCompany

    def getAllTravelCompanies(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM travelcompany")
        rows = cur.fetchall()
        travelCompanyList = []
        for row in rows:
            travelCompanyList.append(TravelCompany(*row))

        cur.close()
        return travelCompanyList

    def getHotel(self, hotelID):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM hotel WHERE hID = %s", (hotelID,))
        hotel = Hotel(*cur.fetchone())
        cur.close()
        return hotel

    def getHotelByName(self, hotelName):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM hotel WHERE hName = %s", (hotelName,))
        hotel = Hotel(*cur.fetchone())
        cur.close()
        return hotel

    def getAllHotels(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM hotel")
        rows = cur.fetchall()
        hotelList = []
        for row in rows:
            hotelList.append(Hotel(*row))

        cur.close()
        return hotelList

    def getTransport(self, transportID):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM transport WHERE tID = %s", (transportID,))
        transport = Transport(*cur.fetchone())
        cur.close()
        return transport

    def getHotelStay(self, hotelStayID):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM hotelstay WHERE hsID = %s", (hotelStayID,))
        hotelStay = HotelStay(*cur.fetchone())
        cur.close()
        return hotelStay

    def getAllTransportsBy(
        self, travelCompany=None, tFrom=None, tTo=None, tDatetime=None
    ):
        cur = self.conn.cursor()

        query = "SELECT * FROM transport "
        query_args = []
        if travelCompany is not None:
            query_args.append("travelCompany = %s ")
        if tFrom is not None:
            query_args.append("tFrom = %s ")
        if tTo is not None:
            query_args.append("tTo = %s")
        if tDatetime is not None:
            query_args.append("tDatetime = %s")

        if len(query_args) > 0:
            query += "WHERE "
            query += " AND ".join(query_args)

        query_arg_values = tuple(
            x for x in (travelCompany, tFrom, tTo, tDatetime) if x is not None
        )

        cur.execute(query, query_arg_values)

        # cur.execute("SELECT * FROM transport WHERE tFrom = %s AND tTo = %s", (tFrom, tTo,))
        rows = cur.fetchall()
        transportList = []
        for row in rows:
            transportList.append(Transport(*row))

        cur.close()
        return transportList

    def getAllHotelStaysBy(self, hotelname=None, region=None):
        cur = self.conn.cursor()

        query = "SELECT hid FROM hotel "
        query_args = []
        if hotelname is not None:
            query_args.append("hname = %s")
        if region is not None:
            query_args.append("region = %s")

        if len(query_args) > 0:
            query += "WHERE "
            query += " AND ".join(query_args)

        query_arg_values = tuple(x for x in (hotelname, region) if x is not None)

        query = "SELECT * FROM hotelstay WHERE hotel in (" + query + ")"

        cur.execute(query, query_arg_values)

        # cur.execute("SELECT * FROM hotelstay WHERE region = %s", (region,))
        rows = cur.fetchall()
        hotelStayList = []
        for row in rows:
            hotelStayList.append(HotelStay(*row))

        cur.close()
        return hotelStayList

    def getBooking(self, bookingID):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM booking WHERE bID = %s", (bookingID,))
        booking = Booking(*cur.fetchone())
        cur.close()
        return booking

    # -- Update --
    def updateCustomerBonus(self, customerID, bonus):
        cur = self.conn.cursor()
        cur.execute(
            "UPDATE customer SET totalPoints = %s WHERE cID = %s",
            (
                bonus,
                customerID,
            ),
        )
        self.conn.commit()
        cur.close()

    def updateTravelCompanyBonus(self, travelCompanyID, bonus):
        cur = self.conn.cursor()
        cur.execute(
            "UPDATE travelcompany SET tcBonus = %s WHERE tcID = %s",
            (
                bonus,
                travelCompanyID,
            ),
        )
        self.conn.commit()
        cur.close()

    def updateHotelStayPrice(self, hotelStayID, price):
        cur = self.conn.cursor()
        cur.execute(
            "UPDATE hotelstay SET hsPrice = %s WHERE hsID = %s",
            (
                price,
                hotelStayID,
            ),
        )
        self.conn.commit()
        cur.close()

    # -- Delete --
    def deleteCustomer(self, customerID):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM customer WHERE cID = %s", (customerID,))
        self.conn.commit()
        cur.close()

    def deleteTravelCompany(self, travelCompanyID):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM travelcompany WHERE tcID = %s", (travelCompanyID,))
        self.conn.commit()
        cur.close()

    def deleteHotel(self, hotelID):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM hotel WHERE hID = %s", (hotelID,))
        self.conn.commit()
        cur.close()

    def deleteTransport(self, transportID):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM transport WHERE tID = %s", (transportID,))
        self.conn.commit()
        cur.close()

    def deleteHotelStay(self, hotelStayID):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM hotelstay WHERE hsID = %s", (hotelStayID,))
        self.conn.commit()
        cur.close()

    def deleteBooking(self, bookingID):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM booking WHERE bookingID = %s", (bookingID,))
        self.conn.commit()
        cur.close()


if __name__ == "__main__":
    db = Repository()
    print(db.getAllTransportsBy())
