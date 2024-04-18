import tkinter as tk
from tkinter import simpledialog, messagebox, ttk

class EnclosureManager:
    def __init__(self, master, enclosures):
        self.master = master
        self.enclosures = enclosures

    def show_manager(self):
        self.enclosure_window = tk.Toplevel(self.master)
        self.enclosure_window.title("Управління вольєрами")
        self.enclosure_window.geometry("400x300")

        self.button_add = tk.Button(self.enclosure_window, text="Додати", command=self.add_enclosure, width=15)
        self.button_add.pack(pady=5)

        self.button_show = tk.Button(self.enclosure_window, text="Показати усіх", command=self.display_all_enclosures, width=15)
        self.button_show.pack(pady=5)

        self.button_remove = tk.Button(self.enclosure_window, text="Видалити усіх", command=self.remove_all_enclosures, width=15)
        self.button_remove.pack(pady=5)

    def add_enclosure(self):
        add_enclosure_window = tk.Toplevel(self.enclosure_window)
        add_enclosure_window.title("Додати вольєр")
        add_enclosure_window.geometry("300x200")

        self.add_enclosure_entry = tk.Entry(add_enclosure_window)
        self.add_enclosure_entry.pack(pady=5)

        size_options = ["Маленький", "Середній", "Великий"]
        self.size_var = tk.StringVar(add_enclosure_window)
        self.size_var.set(size_options[0])
        size_combobox = ttk.Combobox(add_enclosure_window, textvariable=self.size_var, values=size_options, state="readonly")
        size_combobox.pack(pady=5)

        button_confirm = tk.Button(add_enclosure_window, text="Додати", command=self.confirm_add_enclosure, width=15)
        button_confirm.pack(pady=5)

    def confirm_add_enclosure(self):
        name = self.add_enclosure_entry.get()
        size = self.size_var.get()
        if name:
            enclosure_info = f"Вольєр: {name}, Розмір: {size}"
            self.enclosures.append(enclosure_info)
            messagebox.showinfo("Успішно", "Вольєр успішно доданий!")
            self.enclosure_window.destroy()

    def display_all_enclosures(self):
        if self.enclosures:
            display_enclosures_window = tk.Toplevel(self.master)
            display_enclosures_window.title("Усі вольєри")
            display_enclosures_window.geometry("400x300")

            for enclosure in self.enclosures:
                label_enclosure = tk.Label(display_enclosures_window, text=enclosure)
                label_enclosure.pack()
        else:
            messagebox.showinfo("Пусто", "Немає доступних вольеєрів")

    def remove_all_enclosures(self):
        if self.enclosures:
            confirmation = messagebox.askyesno("Видалення вольеєрів", "Вы впевнені, що бажаєте видалити усі вольєри?")
            if confirmation:
                self.enclosures.clear()
                messagebox.showinfo("Успішно", "Усі вольєри видалені")
        else:
            messagebox.showinfo("Пусто", "Немає вольєрів для видалення!")
