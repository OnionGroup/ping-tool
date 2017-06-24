# -*- coding: utf-8 -*-
import Tkinter as tk
import ttk

class EditSettingsFrame(ttk.LabelFrame):

    def __init__(self, parent):
        ttk.LabelFrame.__init__(self, parent, text="ערוך הגדרות", labelanchor="ne")

        self.setup_widgets(parent)

    def setup_widgets(self, parent):
        ttk.Separator(parent, orient=tk.HORIZONTAL).pack(side=tk.TOP, fill=tk.X, pady=10)

        self.run_time_label = ttk.Label(self, text=":שעת ריצה")
        self.run_time_label.grid(row=0, column=1)

        self.run_time_entry = ttk.Entry(self, justify=tk.CENTER)
        self.run_time_entry.grid(row=0)

        self.pack(side=tk.TOP, fill=tk.X)