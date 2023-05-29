import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

from root import Root


from ..backend.app.Service import Service
from ..backend.app.Domain import (
    Customer,
    Hotel,
    HotelStay,
    Transport,
    TravelCompany,
    Booking,
)


COLORS = {
    "black": "#2B2D42",
    "grey": "#8D99AE",
    "white": "#EDF2F4",
    "red": "#EF233C",
    "red2": "#D90429",
}


def get_travel_company_options():
    pass


def get_hotel_stays(city, stay_dates):
    pass


def get_transports(destination_city, travel_company, departure_date):
    pass


def get_customer_bonus(customer_id):
    pass


# Define the main window
root = tk.Tk()
root.title("Travel Agency Service")


# Create the sidebar
sidebar = tk.Frame(root)
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

# Create the stay dates label
stay_dates_label = tk.Label(hotels_frame, text="Stay Dates")
stay_dates_label.pack(side="top", fill="x")

# Create the stay dates input
stay_dates_input = tk.Entry(hotels_frame)
stay_dates_input.pack(side="top", fill="x")

# Create the book button
book_button = tk.Button(hotels_frame, text="Book")
book_button.pack(side="bottom")

# Bind the book button to a function that calls the service.getAllHotelStaysBy() function
book_button.config(
    command=lambda: get_hotel_stays(city_input.get(), stay_dates_input.get())
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
travel_company_options = ["Air India", "Jet Airways", "SpiceJet"]
travel_company_select.set("Air India")
travel_company_dropdown = tk.OptionMenu(
    tickets_frame, travel_company_select, *travel_company_options
)
travel_company_dropdown.pack(side="top", fill="x")

# Create the departure date label
departure_date_label = tk.Label(tickets_frame, text="Departure Date")
departure_date_label.pack(side="top", fill="x")

# Create the departure date input
departure_date_input = tk.Entry(tickets_frame)
departure_date_input.pack(side="top", fill="x")

# Create the book button
book_button = tk.Button(tickets_frame, text="Book")
book_button.pack(side="bottom")

# Bind the book button to a function that calls the service.getAllTransportsBy() function
book_button.config(
    command=lambda: get_transports(
        destination_city_input.get(),
        travel_company_select.get(),
        departure_date_input.get(),
    )
)
# Create the popup window
popup = tk.Toplevel()
popup.title("Customer ID")

# Create the customer ID label
customer_id_label = tk.Label(popup, text="Customer ID")
customer_id_label.pack(side="top", fill="x")

# Create the customer ID input
customer_id_input = tk.Entry(popup)
customer_id_input.pack(side="top", fill="x")

# Create the book button
book_button = tk.Button(popup, text="Book")
book_button.pack(side="bottom")

# Bind the book button to a function that calls the service.getCustomerBonus() function
book_button.config(command=lambda: get_customer_bonus(customer_id_input.get()))


# Start the main loop
root.mainloop()
