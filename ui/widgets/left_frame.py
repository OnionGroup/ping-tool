# -*- coding: utf-8 -*-
import Tkinter as tk
import ttk

from .edit_entry_frame import EditEntryFrame
from .edit_settings_frame import EditSettingsFrame

class LeftFrame(ttk.Frame):

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        self.new_entry_btn = ttk.Button(self, text="הוסף שרת חדש")
        self.new_entry_btn.pack(side=tk.TOP, fill=tk.X)

        self.edit_entry_frame = EditEntryFrame(self)
        self.edit_settings_frame = EditSettingsFrame(self)

        self.save_settings_btn = ttk.Button(self, text = "שמור שינויים")
        self.save_settings_btn.pack(side=tk.TOP, fill=tk.X)

        self.pack(side=tk.LEFT, fill=tk.BOTH, padx=(15, 5), pady=20)