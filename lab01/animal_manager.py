import tkinter as tk
from tkinter import simpledialog, messagebox, ttk

class AnimalManager:
    def __init__(self, master, animals):
        self.master = master
        self.animals = animals

    def show_manager(self):
        self.animal_window = tk.Toplevel(self.master)
        self.animal_window.title("Управління тваринами")
        self.animal_window.geometry("400x300")

        self.button_add = tk.Button(self.animal_window, text="Додати", command=self.add_animal, width=15)
        self.button_add.pack(pady=5)

        self.button_show = tk.Button(self.animal_window, text="Показати усіх", command=self.display_all_animals, width=15)
        self.button_show.pack(pady=5)

        self.button_remove = tk.Button(self.animal_window, text="Видалити усіх", command=self.remove_all_animals, width=15)
        self.button_remove.pack(pady=5)

    def add_animal(self):
        add_animal_window = tk.Toplevel(self.animal_window)
        add_animal_window.title("Додати тварину")
        add_animal_window.geometry("300x200")

        self.add_animal_entry = tk.Entry(add_animal_window)
        self.add_animal_entry.pack(pady=5)

        species_options = ["Птиці", "Хижаки", "Рептилії"]
        self.species_var = tk.StringVar(add_animal_window)
        self.species_var.set(species_options[0])
        species_combobox = ttk.Combobox(add_animal_window, textvariable=self.species_var, values=species_options, state="readonly")
        species_combobox.pack(pady=5)

        button_confirm = tk.Button(add_animal_window, text="Додати", command=self.confirm_add_animal, width=15)
        button_confirm.pack(pady=5)

    def confirm_add_animal(self):
        name = self.add_animal_entry.get()
        species = self.species_var.get()
        if name:
            animal_info = f"Тварина: {name}, Вид: {species}"
            self.animals.append(animal_info)
            messagebox.showinfo("Успішно", "Тварина успішно додана!")
            self.animal_window.destroy()

    def display_all_animals(self):
        if self.animals:
            display_animals_window = tk.Toplevel(self.master)
            display_animals_window.title("Усі тварини")
            display_animals_window.geometry("400x300")

            for animal in self.animals:
                label_animal = tk.Label(display_animals_window, text=animal)
                label_animal.pack()
        else:
            messagebox.showinfo("Пусто", "Немає доступних тварин")
        
    def remove_all_animals(self):
        if self.animals:
            confirmation = messagebox.askyesno("Видалення тварин", "Ви впевнені, що бажаєте видалити усіх тварин?")
            if confirmation:
                self.animals.clear()
                messagebox.showinfo("Успішно", "Усі тварини видалені")
        else:
            messagebox.showinfo("Пусто", "Немає доступних тварин для видалення")
