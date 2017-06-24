# -*- coding: utf-8 -*-

import Tkinter as tk
import ttk

class EntriesTable(ttk.Treeview):

    def __init__(self, parent):
        ttk.Treeview.__init__(self, parent)
        self.setup_widget()

    def setup_widget(self):
        self["columns"] = ("hostname", "nickname")
        self['show'] = 'headings'

        self.heading("nickname", text="כינוי")
        self.column("nickname", anchor="e")
        self.heading("hostname", text="שם שרת")
        self.column("hostname", anchor="e")

        self.pack(side=tk.RIGHT, fill=tk.X, padx=10, pady=20)

    def set_entries(self, entries):
        for entry in entries:
            self.insert("", "end", values=(entry["value"], entry["nickname"]))