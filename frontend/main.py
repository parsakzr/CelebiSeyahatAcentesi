import tkinter as tk
from tkcalendar import  DateEntry

from root import Root
from framehandler import FrameHandler

background_color = "#F2CECE"
active_background_color = "#DDBDBD"

root = Root()

photo = tk.PhotoImage(file="icons/toggle_menu.png", )
photoimage_tm = photo.subsample(20, 20)

photo = tk.PhotoImage(file="icons/close.png", )
photoimage_c = photo.subsample(20, 20)

photo = tk.PhotoImage(file="icons/sun-umbrella.png", )
photoimage_h = photo.subsample(20, 20)

photo = tk.PhotoImage(file="icons/tickets.png", )
photoimage_t = photo.subsample(20, 20)

def holiday_frame_open():
    holiday_frame = FrameHandler(root)

    region_label = tk.Label(holiday_frame.left_frame, text="Region", font="Verdana, 14", bg="white")
    region_label.grid(row=1, column=0, padx=5, pady=5, sticky="WN")

    region_text = tk.Text(holiday_frame.left_frame, height=1, width=15)
    region_text.grid(row=1, column=1, padx=2, pady=2, sticky="WN")

    date_label_d = tk.Label(holiday_frame.left_frame, text="Departure Date", font="Verdana, 14", bg="white")
    date_label_d.grid(row=2, column=0, padx=5, pady=5, sticky="WN")

    date_departure = DateEntry(holiday_frame.left_frame, width=25, background="magenta3", foreground="white", bd=2,
                          date_pattern="dd/MM/yyyy")
    date_departure.grid(row=2, column=1, padx=5, pady=5, sticky="WN")

    date_label_a = tk.Label(holiday_frame.left_frame, text="Arrival Date", font="Verdana, 14", bg="white")
    date_label_a.grid(row=3, column=0, padx=5, pady=5, sticky="WN")

    date_arrival = DateEntry(holiday_frame.left_frame, width=25, background="magenta3", foreground="white", bd=2,
                          date_pattern="dd/MM/yyyy")
    date_arrival.grid(row=3, column=1, padx=5, pady=5, sticky="WN")

    submit_btn_h = tk.Button(holiday_frame.left_frame, text="Submit", font="Verdana, 14", foreground="black", width=15, height=1)
    submit_btn_h.grid(row=3, column=1, padx=5, pady=5, sticky="NE")
def ticket_frame_open():
    ticket_frame = FrameHandler(root)

    ticket_compaines = ["Uçan Türk Özel Havayolu", "Devlet Demir Yolları", "YTUR Otobüs"]

    departure_date_label = tk.Label(ticket_frame.left_frame, text="Departure Date", font="Verdana, 14", foreground="black")
    departure_date_label.grid(row=0, column=0, padx=5, pady=5, sticky="WN")
    departure_date = DateEntry(ticket_frame.left_frame, width=25, background="magenta3", foreground="white", bd=2,
                          date_pattern="dd/MM/yyyy")
    departure_date.grid(row=0, column=1, padx=5, pady=5)

    arrival_date_label = tk.Label(ticket_frame.left_frame, text="Arrival Date", font="Verdana, 14", foreground="black")
    arrival_date_label.grid(row=1, column=0, padx=5, pady=5, sticky="WN")
    arrival_date = DateEntry(ticket_frame.left_frame, width=25, background="magenta3", foreground="white", bd=2,
                          date_pattern="dd/MM/yyyy")
    arrival_date.grid(row=1, column=1, padx=5, pady=5)

    company_label = tk.Label(ticket_frame.left_frame, text="Select Company", font="Verdana, 14", foreground="black")
    company_label.grid(row=2, column=0, padx=5, pady=5, sticky="WN")

    listbox_compaines = tk.Listbox(ticket_frame.left_frame, bg="lime", height=len(ticket_compaines), width=25)
    for item in ticket_compaines:
        listbox_compaines.insert(tk.END, item)
    listbox_compaines.grid(row=2, column=1, padx=5, pady=5, sticky="NEW")

    def select(evt):
        print(listbox_compaines.get(tk.ANCHOR))
    listbox_compaines.bind('<<ListboxSelect>>', select)

    right_frame_label = tk.Label(ticket_frame.right_frame, text="Right Frame", font="Verdana, 14", foreground="black")
    right_frame_label.grid(row=1, column=0, padx=5, pady=5, sticky="WN")

    submit_btn_t = tk.Button(ticket_frame.left_frame, text="Submit", font="Verdana, 14", foreground="black", width=15, height=1)
    submit_btn_t.grid(row=3, column=1, padx=5, pady=5, sticky="NE")

def toggle_menu():
    def collapse_toggle_menu():
        toggle_menu_fm.destroy()
        toggle_btn.config(image=photoimage_tm)
        toggle_btn.config(command=toggle_menu)

    toggle_menu_fm = tk.Frame(root, bg=background_color)

    holiday_btn = tk.Button(toggle_menu_fm, text="Holiday", image=photoimage_h, font=("Bold", 14), bd=0, pady=12, padx=22, bg=background_color, fg="black", compound=tk.LEFT)
    holiday_btn.pack(side=tk.TOP, fill=tk.X)

    ticket_btn = tk.Button(toggle_menu_fm, text="Ticket", image=photoimage_t, font=("Bold", 14), bd=0, pady=12, padx=22, bg=background_color, fg="black", compound=tk.LEFT)
    ticket_btn.pack(side=tk.TOP, fill=tk.X)

    holiday_btn.config(command=holiday_frame_open)
    ticket_btn.config(command=ticket_frame_open)

    toggle_menu_fm.grid(row=1, column=0, rowspan=2, sticky="WENS")
    toggle_btn.config(image=photoimage_c)
    toggle_btn.config(command=collapse_toggle_menu)


head_frame = tk.Frame(root, bg=background_color, highlightbackground="white", highlightthickness=0)

toggle_btn = tk.Button(head_frame, background=background_color, foreground="black",  text="Menu", image=photoimage_tm,
                       compound=tk.LEFT, font=("Bold", 15), pady=15, padx=15, bd=0, activebackground=active_background_color,
                       command=toggle_menu, anchor="w", width=174)

toggle_btn.pack(side=tk.LEFT)
head_frame.grid(row=0, column=0, sticky="WNES", columnspan=3)

welcome_frame = tk.Frame(root, bg="#154c79", highlightbackground="white", highlightthickness=0)
welcome_frame.grid(row=1, column=1, sticky="WENS")
welcome_frame.columnconfigure(0, weight=1)

welcome_text = tk.Label(welcome_frame, text="Welcome!", font=("Verdana", 26), bg="#154c79",)
welcome_text.grid(row=0, column=0, padx=5, pady=5, sticky="WENS")

root.mainloop()