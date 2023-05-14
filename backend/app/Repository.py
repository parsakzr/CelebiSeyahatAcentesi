import psycopg2


class Repository:
    def __init__(self) -> None:
        self.conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="postgres",
        )

    def __del__(self):
        self.conn.close()

    def createCustomer(self, name):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO customer (cName) VALUES (%s)", (name,))
        self.conn.commit()
        cur.close()

    def createTravelCompany(self, name, wayOfTravel, bonus):
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO travel_company (cName, way_of_travel, bonus) VALUES (%s, %s, %s)",
            (name, wayOfTravel, bonus),
        )
        self.conn.commit()
        cur.close()

    def createHotel(self, name, region, address, bonus):
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO hotel (hName, region, address, bonus) VALUES (%s, %s, %s, %s)",
            (name, region, address, bonus),
        )
        self.conn.commit()
        cur.close()

    def createTransport(self, travelCompany, tFrom, tTo, tDatetime, tPrice):
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO transport (travelCompany, tFrom, tTo, tDatetime, tPrice) VALUES (%s, %s, %s, %s, %s)",
            (travelCompany, tFrom, tTo, tDatetime, tPrice),
        )
        self.conn.commit()
        cur.close()

    def createHotelStay(self, hotelID, price):
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO hotel_stay (hotel, price) VALUES (%s, %s)",
            (hotelID, price),
        )
        self.conn.commit()
        cur.close()

    # def bookHotel(
    #     self,
    #     customerID,
    #     hotelStayID,
    #     fromDate,
    #     toDate,
    #     numOfPassengers,
    #     totalPrice, # totalPrice = price * numOfPassengers, #TODO
    #     totalBonus,
    # ):
    #     cur = self.conn.cursor()
    #     cur.execute(
    #         "INSERT INTO booking (customer, typeOfBooking, hotel_stay, fromDate, toDate, numOfPassengers, totalPrice, totalBonus) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
    #         (
    #             customerID,
    #             "H",
    #             hotelStayID,
    #             fromDate,
    #             toDate,
    #             numOfPassengers,
    #             totalPrice,
    #             totalBonus,
    #         ),
    #     )
    #     self.conn.commit()
    #     cur.close()

    # def bookTransport(
    #     self,
    #     customerID,
    #     transportID,
    #     fromDate,
    #     toDate,
    #     numOfPassengers,
    #     totalPrice,  # totalPrice = price * numOfPassengers, #TODO
    #     totalBonus,
    # ):
    #     cur = self.conn.cursor()
    #     cur.execute(
    #         "INSERT INTO booking (customerID, typeOfBooking, transport, fromDate, toDate, numOfPassengers, totalPrice, totalBonus) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
    #         (
    #             customerID,
    #             "T",
    #             transportID,
    #             fromDate,
    #             toDate,
    #             numOfPassengers,
    #             totalPrice,
    #             totalBonus,
    #         ),
    #     )
    #     self.conn.commit()
    #     cur.close()
