import tkinter as tk
from tkinter import simpledialog
from tkinter import ttk

class DataEntryDialog(tk.Toplevel):
    def __init__(self, master, prompt, title, choices=None):
        super().__init__(master)
        self.title(title)

        self.prompt_label = tk.Label(self, text=prompt, font=("Arial", 12, "bold"))
        self.prompt_label.pack(pady=10)

        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.entry_var, font=("Arial", 12))
        self.entry.pack(pady=10)

        if choices:
            self.type_label = tk.Label(self, text="Виберіть тип:", font=("Arial", 12, "bold"))
            self.type_label.pack(pady=5)

            self.type_combobox = ttk.Combobox(self, values=choices, font=("Arial", 12))
            self.type_combobox.pack(pady=5)

        self.confirm_button = tk.Button(self, text="Підтвердити", command=self.confirm, font=("Arial", 12, "bold"), bd=5, width=15)
        self.confirm_button.pack(pady=10)

        self.geometry("300x200")
        self.update_idletasks()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - self.winfo_width()) // 2
        y = (screen_height - self.winfo_height()) // 2
        self.geometry(f"+{x}+{y}")

    def confirm(self):
        if not self.entry_var.get():
            self.prompt_label.config(text="Вкажіть дані", fg="red")
        else:
            self.result = {
                'name': self.entry_var.get(),
                'species': self.type_combobox.get() if hasattr(self, 'type_combobox') else None,
                'type': self.type_combobox.get() if hasattr(self, 'type_combobox') else None
            }
            self.destroy()
