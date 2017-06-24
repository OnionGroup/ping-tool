# -*- coding: utf-8 -*-
import Tkinter as tk
import ttk

class EditEntryFrame(ttk.LabelFrame):

    def __init__(self, parent):
        ttk.LabelFrame.__init__(self, parent, text="ערוך שרת", labelanchor="ne")

        self.setup_widget(parent)

    def setup_widget(self, parent):
        ttk.Separator(parent, orient=tk.HORIZONTAL).pack(side=tk.TOP, fill=tk.X, pady=10)

        self.nickname_label = ttk.Label(self, text=":כינוי")
        self.nickname_label.grid(row=0, column=1)

        self.nickname_entry = ttk.Entry(self)
        self.nickname_entry.grid(row=0)

        self.hostname_label = ttk.Label(self, text=":שם שרת")
        self.hostname_label.grid(row=1, column=1)

        self.hostname_entry = ttk.Entry(self)
        self.hostname_entry.grid(row=1)

        self.edit_save_entry = ttk.Button(self, text="ערוך")
        self.edit_save_entry.grid(row=2, column=0)

        self.edit_delete = ttk.Button(self, text="מחיקה")
        self.edit_delete.grid(row=2, column=1)

        self.pack(side=tk.TOP)