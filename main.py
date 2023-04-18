import tkinter as tk
from tkcalendar import Calendar, DateEntry

from root import Root

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

    window_height = root.winfo_height()
    toggle_menu_fm.grid(row=1, column=0, rowspan=2, sticky="WENS")
    toggle_btn.config(image=photoimage_c)
    toggle_btn.config(command=collapse_toggle_menu)


head_frame = tk.Frame(root, bg=background_color, highlightbackground="white", highlightthickness=0)

toggle_btn = tk.Button(head_frame, background=background_color, foreground="black",  text="Menu", image=photoimage_tm,
                       compound=tk.LEFT, font=("Bold", 15), pady=15, padx=15, bd=0, activebackground=active_background_color,
                       command=toggle_menu, anchor="w", width=174)

toggle_btn.pack(side=tk.LEFT)
#head_frame.pack(side=tk.TOP, fill=tk.X)
head_frame.grid(row=0, column=0, sticky="WNES", columnspan=3)



holiday_frame = tk.Frame(root, bg="#154c79", highlightbackground="white", highlightthickness=0)
holiday_frame.grid(row=1, column=1, sticky="WENS", columnspan=3, rowspan=3)
holiday_frame.columnconfigure(0, weight=1)
holiday_frame.columnconfigure(1, weight=1)
holiday_frame.rowconfigure(0, weight=1)
holiday_frame.grid_propagate(False)

right_frame = tk.Frame(holiday_frame, bg="orange", highlightbackground="white")
right_frame.grid(row=0, column=1, sticky="WENS")

left_frame = tk.Frame(holiday_frame, bg="white", highlightbackground="white")
left_frame.grid(row=0, column=0, sticky="WENS")

price_label = tk.Label(left_frame, text="Price", font=("Verdana, 14"), bg="white")
price_label.grid(row=1, column=0,  padx=5, pady=5)

price_text = tk.Text(left_frame, height = 1, width = 25)
price_text.grid(row=1, column=1, padx=2, pady=2)

date_label = tk.Label(right_frame, text="Date", font=("Verdana, 14"), bg="white")
date_label.grid(row=0, column=0, padx=5, pady=5)

date_text = DateEntry(right_frame, width= 25, background= "magenta3", foreground= "white", bd=2, date_pattern="dd/MM/yyyy")
date_text.grid(row=0, column=1, padx=5, pady=5)

root.mainloop()