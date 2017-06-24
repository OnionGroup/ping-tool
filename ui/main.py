# -*- coding: utf-8 -*-

import Tkinter as tk
import ttk

from common.config_reader import read_config

class AppWindow(ttk.Frame):

    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)

        self.master.title("PingTool")

        self.style = ttk.Style()
        self.style.configure("TLabel", anchor=tk.CENTER)

        self.define_widgets()
        self.pack()

    def define_widgets(self):
        self.define_left_frame()
        self.define_table()
        self.add_values()


    def define_left_frame(self):
        self.left_frame = ttk.Frame(self)
        self.left_frame.pack(side=tk.LEFT, padx=(15, 5), pady=20, fill=tk.BOTH)

        self.define_new_entry()
        self.define_edit_panel()
        self.define_settings_panel()

        self.edit_save = ttk.Button(self.left_frame, text="שמור הגדרות")
        self.edit_save.pack(side=tk.TOP, fill=tk.X, pady=(10, 0))

    def define_new_entry(self):
        self.newentry_btn = ttk.Button(self.left_frame, text="הוסף שרת חדש")
        self.newentry_btn.pack(side=tk.TOP, fill=tk.X)

    def define_edit_panel(self):
        ttk.Separator(self.left_frame, orient=tk.HORIZONTAL).pack(side=tk.TOP, fill=tk.X, pady=10)

        self.edit_frame = ttk.LabelFrame(self.left_frame, text="ערוך שרת", labelanchor="ne")
        self.edit_frame.pack(side=tk.TOP, fill=tk.X)

        self.nickname_label = ttk.Label(self.edit_frame, text=":כינוי")
        self.nickname_label.grid(row=0, column=1)

        self.nickname_entry = ttk.Entry(self.edit_frame)
        self.nickname_entry.grid(row=0)

        self.hostname_label = ttk.Label(self.edit_frame, text=":שם שרת")
        self.hostname_label.grid(row=1, column=1)

        self.hostname_entry = ttk.Entry(self.edit_frame)
        self.hostname_entry.grid(row=1)

        self.edit_save_entry = ttk.Button(self.edit_frame, text="ערוך")
        self.edit_save_entry.grid(row=2, column=0, sticky=tk.W + tk.E)

        self.edit_delete = ttk.Button(self.edit_frame, text="מחיקה")
        self.edit_delete.grid(row=2, column=1)

    def define_settings_panel(self):
        ttk.Separator(self.left_frame, orient=tk.HORIZONTAL).pack(side=tk.TOP, fill=tk.X, pady=10)

        self.settings_frame = ttk.LabelFrame(self.left_frame, text="ערוך הגדרות", labelanchor="ne")
        self.settings_frame.pack(side=tk.TOP, fill=tk.X)

        self.run_time_label = ttk.Label(self.settings_frame, text=":שעת ריצה")
        self.run_time_label.grid(row=0, column=1)

        self.run_time_entry = ttk.Entry(self.settings_frame, justify=tk.CENTER)
        self.run_time_entry.grid(row=0)

    def define_table(self):
        self.style.configure("Treeview", foreground='black')
        self.style.configure("Treeview.Heading", font=("Arial", 12))

        table = ttk.Treeview(self)
        table["columns"] = ("hostname", "nickname")
        table['show'] = 'headings'

        table.heading("nickname", text="כינוי")
        table.column("nickname", anchor="e")
        table.heading("hostname", text="שם שרת")
        table.column("hostname", anchor="e")

        table.pack(fill=tk.X, padx=10, pady=20)

        self.table = table

    def add_values(self):
        config = read_config("../configuration/config.json")

        for host in config["hosts"]:
            self.table.insert("", "end", values=(host["value"], host["nickname"]))

app = AppWindow()
app.mainloop()