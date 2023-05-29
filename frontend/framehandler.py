import tkinter as tk


class FrameHandler(tk.Frame):
    def __init__(self, root):
        super().__init__(
            root, bg="white", highlightbackground="white", highlightthickness=0
        )
        self.grid(row=1, column=1, sticky="WENS", columnspan=3, rowspan=3)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.grid_propagate(False)
        self.right_frame = tk.Frame(self, bg="white", highlightbackground="white")
        self.right_frame.grid(row=0, column=1, sticky="WENS")
        self.left_frame = tk.Frame(self, bg="white", highlightbackground="white")
        self.left_frame.grid(row=0, column=0, sticky="WENS")
        self.left_frame.grid_propagate(False)
        self.right_frame.grid_propagate(False)
