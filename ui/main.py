# -*- coding: utf-8 -*-

import Tkinter as tk
import ttk

from widgets.entries_table import EntriesTable
from widgets.left_frame import LeftFrame

from common.config_reader import read_config

class AppWindow(ttk.Frame):

    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)

        self.master.title("PingTool")
        self.master.resizable(False, False)

        self.define_widgets()
        self.pack()

    def define_widgets(self):

        self.table = EntriesTable(self)
        entries = read_config("../configuration/config.json")["hosts"]
        self.table.set_entries(entries)

        self.left_frame = LeftFrame(self)


app = AppWindow()
app.mainloop()