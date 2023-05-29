import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

from root import Root
from framehandler import FrameHandler

# from backend.app import Service
# from backend.app.Domain import (
#     Customer,
#     Hotel,
#     HotelStay,
#     Transport,
#     TravelCompany,
#     Booking,
# )


COLORS = {
    "black": "#2B2D42",
    "grey": "#8D99AE",
    "white": "#EDF2F4",
    "red": "#EF233C",
    "red2": "#D90429",
}

icons = {
    "toggle": "icons/toggle_menu.png",
    "close": "icons/close.png",
    "hotel": "icons/sun-umbrella.png",
    "ticket": "icons/tickets.png",
}


class app:
    root = Root()

    def __init__(self):
        self.root = Root()

        self.icons = {}
        for key, value in icons.items():
            self.icons[key] = tk.PhotoImage(file=value, master=self.root).subsample(
                20, 20
            )

        # self.service = Service()

        self.head_frame()
        self.welcome_frame()

        self.root.mainloop()

    def hotel_frame_open(self):
        hotel_frame = FrameHandler(self.root)

        region_label = tk.Label(hotel_frame.left_frame, text="Region")
        region_label.grid(row=1, column=0, padx=5, pady=5, sticky="WN")
        region_text = tk.Text(hotel_frame.left_frame, height=1, width=15)
        region_text.grid(row=1, column=1, padx=2, pady=2, sticky="WN")

        date_departure_label = tk.Label(
            hotel_frame.left_frame,
            text="Departure Date",
        )
        date_departure_label.grid(row=2, column=0, padx=5, pady=5, sticky="WN")

        date_departure = DateEntry(
            hotel_frame.left_frame,
            width=25,
            bd=2,
            date_pattern="dd/MM/yyyy",
        )
        date_departure.grid(row=2, column=1, padx=5, pady=5, sticky="WN")

        date_arrival_label = tk.Label(hotel_frame.left_frame, text="Arrival Date")
        date_arrival_label.grid(row=3, column=0, padx=5, pady=5, sticky="WN")

        date_arrival = DateEntry(
            hotel_frame.left_frame,
            width=25,
            bd=2,
            date_pattern="dd/MM/yyyy",
        )
        date_arrival.grid(row=3, column=1, padx=5, pady=5, sticky="WN")

        submit_btn = tk.Button(
            hotel_frame.left_frame,
            text="Submit",
            width=15,
            height=1,
        )
        submit_btn.grid(row=3, column=1, padx=5, pady=5, sticky="NE")

    def ticket_frame_open(self):
        ticket_frame = FrameHandler(self.root)

        travel_companies = [
            "Uçan Türk Özel Havayolu",
            "Devlet Demir Yolları",
            "YTUR Otobüs",
        ]

        departure_date_label = tk.Label(
            ticket_frame.left_frame,
            text="Departure Date",
        )
        departure_date_label.grid(row=0, column=0, padx=5, pady=5, sticky="WN")
        departure_date = DateEntry(
            ticket_frame.left_frame,
            width=25,
            bd=2,
            date_pattern="dd/MM/yyyy",
        )
        departure_date.grid(row=0, column=1, padx=5, pady=5)

        arrival_date_label = tk.Label(
            ticket_frame.left_frame,
            text="Arrival Date",
        )
        arrival_date_label.grid(row=1, column=0, padx=5, pady=5, sticky="WN")
        arrival_date = DateEntry(
            ticket_frame.left_frame,
            width=25,
            bd=2,
            date_pattern="dd/MM/yyyy",
        )
        arrival_date.grid(row=1, column=1, padx=5, pady=5)

        company_label = tk.Label(
            ticket_frame.left_frame,
            text="Select Company",
            foreground="black",
        )
        company_label.grid(row=2, column=0, padx=5, pady=5, sticky="WN")

        listbox_companies = tk.Listbox(
            ticket_frame.left_frame, bg="lime", height=len(travel_companies), width=25
        )
        for item in travel_companies:
            listbox_companies.insert(tk.END, item)
        listbox_companies.grid(row=2, column=1, padx=5, pady=5, sticky="NEW")

        def select(evt):
            company = listbox_companies.get(tk.ANCHOR)
            print(company)

        listbox_companies.bind("<<ListboxSelect>>", select)

        right_frame_label = tk.Label(
            self.ticket_frame.right_frame,
            text="Right Frame",
        )
        right_frame_label.grid(row=1, column=0, padx=5, pady=5, sticky="WN")

        submit_btn_t = tk.Button(
            self.ticket_frame.left_frame,
            text="Submit",
            width=15,
            height=1,
        )
        submit_btn_t.grid(row=3, column=1, padx=5, pady=5, sticky="NE")

    def customer_frame_open(self):
        customer_frame = FrameHandler(self.root)

        customer_name_label = tk.Label(
            customer_frame.left_frame,
            text="Customer Name",
        )
        customer_name_label.grid(row=0, column=0, padx=5, pady=5, sticky="WN")
        customer_name = tk.Text(customer_frame.left_frame, height=1, width=15)
        customer_name.grid(row=0, column=1, padx=2, pady=2, sticky="WN")

        submit_btn = tk.Button(
            customer_frame.left_frame,
            text="Submit",
            width=15,
            height=1,
        )
        submit_btn.grid(row=1, column=1, padx=5, pady=5, sticky="NE")

    def toggle_menu(self):
        def collapse_toggle_menu():
            toggle_menu_fm.destroy()
            self.toggle_btn.config(image=self.icons["toggle"])
            self.toggle_btn.config(command=self.toggle_menu)

        toggle_menu_fm = tk.Frame(self.root, bg=COLORS["white"])

        holiday_btn = tk.Button(
            toggle_menu_fm,
            text="Holiday",
            image=self.icons["hotel"],
            font=("Bold", 14),
            bd=0,
            pady=12,
            padx=22,
            bg=COLORS["white"],
            fg="black",
            compound=tk.LEFT,
        )
        holiday_btn.pack(side=tk.TOP, fill=tk.X)

        ticket_btn = tk.Button(
            toggle_menu_fm,
            text="Ticket",
            image=self.icons["ticket"],
            font=("Bold", 14),
            bd=0,
            pady=12,
            padx=22,
            bg=COLORS["white"],
            fg="black",
            compound=tk.LEFT,
        )
        ticket_btn.pack(side=tk.TOP, fill=tk.X)

        holiday_btn.config(command=self.hotel_frame_open)
        ticket_btn.config(command=self.ticket_frame_open)

        toggle_menu_fm.grid(row=1, column=0, rowspan=2, sticky="WENS")
        self.toggle_btn.config(image=self.icons["close"])
        self.toggle_btn.config(command=collapse_toggle_menu)

    def head_frame(self):
        head_frame = tk.Frame(
            self.root,
            bg=COLORS["black"],
            highlightbackground="white",
            highlightthickness=0,
        )

        self.toggle_btn = tk.Button(
            head_frame,
            background=COLORS["black"],
            foreground=COLORS["red"],
            text="Menu",
            image=self.icons["toggle"],
            compound=tk.LEFT,
            font=("Bold", 15),
            pady=15,
            padx=15,
            bd=0,
            activebackground=COLORS["grey"],
            command=self.toggle_menu,
            anchor="w",
            width=174,
        )

        self.toggle_btn.pack(side=tk.LEFT)
        head_frame.grid(row=0, column=0, sticky="WNES", columnspan=3)

    def welcome_frame(self):
        welcome_frame = tk.Frame(self.root, highlightthickness=0)
        welcome_frame.grid(row=1, column=1, sticky="WENS")
        welcome_frame.columnconfigure(0, weight=1)

        welcome_text = tk.Label(welcome_frame, text="Welcome!")
        welcome_text.grid(row=0, column=0, padx=5, pady=5, sticky="WENS")


if __name__ == "__main__":
    app()
