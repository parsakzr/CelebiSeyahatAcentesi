import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry


from app.Service import Service
from app.Domain import (
    Customer,
    Hotel,
    HotelStay,
    Transport,
    TravelCompany,
    Booking,
)

service = Service()

COLORS = {
    "black": "#2B2D42",
    "grey": "#8D99AE",
    "white": "#EDF2F4",
    "red": "#EF233C",
    "red2": "#D90429",
}


def get_travel_company_options():
    return service.getAllTravelCompanyNames()


def get_hotel_options():
    return service.getAllHotelNames()


def get_hotel_stays(city, hotelName):
    def hotelstay_row(frame, hotelstay):
        row = tk.Frame(frame)
        row.pack(side="top", fill="x")
        service.getHotel(hotelstay.hotel)
        hotel = service.getHotel(hotelstay.hotel)
        text_label = tk.Label(row, text=f"Hotel: {hotel.name} Price: {hotelstay.price}")
        text_label.pack(side="left", fill="x")
        book_button = tk.Button(row, text="Book")
        book_button.pack(side="right", fill="x")

        book_button.config(command=lambda: bookProcedure("H", hotelstay.hotel))

    popup = tk.Toplevel()
    popup.title("Hotel Stays")

    # table of hotel stays
    table = tk.Frame(popup)
    table.pack(side="top", fill="x", padx=5, pady=5)

    hotelstays = service.getAllHotelStaysBy(hotelname=hotelName, region=city)

    # DEBUG
    hotelstays = [
        HotelStay(id=1, hotel=1, price=1000),
        HotelStay(id=2, hotel=2, price=2000),
        HotelStay(id=3, hotel=3, price=3000),
    ]

    for hotelstay in hotelstays:
        hotelstay_row(table, hotelstay)


def get_transports(travel_company, destination_city, departure_date):
    def transport_row(frame, transport):
        row = tk.Frame(frame)
        row.pack(side="top", fill="x")
        text_label = tk.Label(
            row,
            text=f"Transport: {transport.travelCompany.name} Price: {transport.price}",
        )
        text_label.pack(side="left", fill="x")
        book_button = tk.Button(row, text="Book")
        book_button.pack(side="right", fill="x")

        book_button.config(command=lambda: bookProcedure("T", transport.id))

    popup = tk.Toplevel()
    popup.title("Transports")

    # table of transports
    table = tk.Frame(popup)
    table.pack(side="top", fill="x", padx=5, pady=5)

    travel_company_id = service.getTravelCompanyByName(travel_company).id
    transports = service.getAllTransportsBy(
        travelCompany=travel_company_id,
        tFrom=destination_city,
        tDatetime=departure_date,
    )

    # DEBUG
    transports = [
        Transport(id=1, travelCompany=1, price=1000),
        Transport(id=2, travelCompany=2, price=2000),
        Transport(id=3, travelCompany=3, price=3000),
    ]

    for transport in transports:
        transport_row(table, transport)


def get_customer(customer_id=None, costumer_name=None):
    customer = None
    if customer_id:
        customer = service.getCustomer(customer_id)
    elif costumer_name:
        customer = service.getCustomerByName(costumer_name)

    if not customer:
        print("ERR: Customer not found")
        return None

    return customer


def bookProcedure(type, id):
    # pop up window to ask for customer id and number of passengers
    # Create the popup window
    popup = tk.Toplevel()
    popup.title("Booking info")

    # Create the customer ID label
    customer_id_label = tk.Label(popup, text="Customer ID")
    customer_id_label.pack(side="top", fill="x")

    # Create the customer ID input
    customer_id_input = tk.Entry(popup)
    customer_id_input.pack(side="top", fill="x")

    # Create the customer name label
    customer_name_label = tk.Label(popup, text="or Customer Name")
    customer_name_label.pack(side="top", fill="x")

    # Create the customer name input
    customer_name_input = tk.Entry(popup)
    customer_name_input.pack(side="top", fill="x")

    # create a label for number of passengers
    number_of_passengers_label = tk.Label(popup, text="Number of Passengers")
    number_of_passengers_label.pack(side="top", fill="x")
    # create an input for number of passengers
    number_of_passengers_input = tk.Entry(popup)
    number_of_passengers_input.pack(side="top", fill="x")

    if type == "H":
        # Create the from dates label
        from_date_label = tk.Label(popup, text="from Date")
        from_date_label.pack(side="top", fill="x")
        # Create the from date input
        from_date_input = DateEntry(popup, width=12)
        from_date_input.pack(side="top", fill="x")

        # Create the to dates label
        to_date_label = tk.Label(popup, text="to Date")
        to_date_label.pack(side="top", fill="x")
        # Create the to date input
        to_date_input = DateEntry(popup, width=12)
        to_date_input.pack(side="top", fill="x")

    # Create the book button
    book_button = tk.Button(popup, text="Book")
    book_button.pack(side="bottom")

    def book_button_callback():
        customer = None
        if customer_id_input.get():
            customer = service.getCustomer(int(customer_id_input.get()))
        elif customer_name_input.get():
            customer = service.getCustomerByName(customer_name_input.get())

        if customer == None:
            print("ERR: Customer not found")
            return None

        customerId = customer.id
        bonus = customer.totalPoints

        bonus_label = tk.Label(popup, text=f"Customer bonus: {bonus}")

        numOfPassangers = int(number_of_passengers_input.get()) or 1

        bookingId = None
        if type == "H":
            bookingId = service.bookHotel(
                id,
                customerId,
                numOfPassangers,
                from_date_input.get(),
                to_date_input.get(),
            )
        elif type == "T":
            bookingId = service.bookTicket(id, customerId, numOfPassangers)

        if bookingId == None:
            print("ERR: Booking failed")
            return None

        print("Booking successful")
        success_label = tk.Label(popup, text=f"Booking id: {bookingId}", fg="green")
        success_label.pack(side="bottom", fill="x")

    # Bind the book button to a function that calls the service.getCustomerBonus() function
    book_button.config(command=book_button_callback)

    # get customer id and number of passengers
    # calculate total price and bonus


# --- GUI ---------------------------------------------------------------------
# Define the main window
root = tk.Tk()
root.title("Çelebi Seyahat Acentası")
# root.geometry("920x720")
root.configure(bg=COLORS["black"])
root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=5)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=99)
root.grid_propagate(False)


# Create the sidebar
sidebar = tk.Frame(root, width=200)
sidebar.pack(side="left", fill="y")

# Create the hotel label
hotel_label = tk.Label(sidebar, text="Hotels")
hotel_label.pack(side="top", fill="x")

# Create the ticket label
ticket_label = tk.Label(sidebar, text="Tickets")
ticket_label.pack(side="top", fill="x")


# Create the hotels frame
hotels_frame = tk.Frame(root)
hotels_frame.pack(side="left", fill="both", expand=True)

# Create the city label
city_label = tk.Label(hotels_frame, text="City")
city_label.pack(side="top", fill="x")

# Create the city input
city_input = tk.Entry(hotels_frame)
city_input.pack(side="top", fill="x")
# Create the hotel company label
hotel_label = tk.Label(hotels_frame, text="Hotel")
hotel_label.pack(side="top", fill="x")

# Create the hotel company select
hotel_select = tk.StringVar()
# hotel_options = ["", "Jet Airways", "SpiceJet"]
hotel_options = get_hotel_options()
hotel_select.set("")
hotel_dropdown = tk.OptionMenu(hotels_frame, hotel_select, *hotel_options)
hotel_dropdown.pack(side="top", fill="x")

# Create the list button
list_button = tk.Button(hotels_frame, text="List hotels")
list_button.pack(side="bottom")

# Bind the list button to a function that calls the service.getAllHotelStaysBy() function
list_button.config(
    command=lambda: get_hotel_stays(city=city_input.get(), hotelName=hotel_select.get())
)

# Create the tickets frame
tickets_frame = tk.Frame(root)
tickets_frame.pack(side="right", fill="both", expand=True)

# Create the destination city label
destination_city_label = tk.Label(tickets_frame, text="Destination City")
destination_city_label.pack(side="top", fill="x")

# Create the destination city input
destination_city_input = tk.Entry(tickets_frame)
destination_city_input.pack(side="top", fill="x")

# Create the travel company label
travel_company_label = tk.Label(tickets_frame, text="Travel Company")
travel_company_label.pack(side="top", fill="x")

# Create the travel company select
travel_company_select = tk.StringVar()
# travel_company_options = ["Air India", "Jet Airways", "SpiceJet"]
travel_company_options = get_travel_company_options()
travel_company_select.set(travel_company_options[0])
travel_company_dropdown = tk.OptionMenu(
    tickets_frame, travel_company_select, *travel_company_options
)
travel_company_dropdown.pack(side="top", fill="x")

# Create the departure date label
departure_date_label = tk.Label(tickets_frame, text="Departure Date")
departure_date_label.pack(side="top", fill="x")

# Create the departure date input
departure_date_input = DateEntry(tickets_frame, width=12)
departure_date_input.pack(side="top", fill="x")

# Create the list button
list_button = tk.Button(tickets_frame, text="List tickets")
list_button.pack(side="bottom")

# Bind the list button to a function that calls the service.getAllTransportsBy() function
list_button.config(
    command=lambda: get_transports(
        destination_city=destination_city_input.get(),
        travel_company=travel_company_select.get(),
        departure_date=departure_date_input.get(),
    )
)


# Start the main loop
root.mainloop()
