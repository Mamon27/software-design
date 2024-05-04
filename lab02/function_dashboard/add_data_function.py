import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3

class AddDataFunction:
    def __init__(self, master):
        self.master = master
        self.master.title("Заповнення даних")
        self.master.geometry("400x600")
        self.master.configure(bg="#f0f0f0")

        # Заголовок
        self.label_title = tk.Label(master, text="Додати дані", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
        self.label_title.pack(pady=20)

        # Прізвище
        # self.label_lastname = tk.Label(master, text="Прізвище:", font=("Helvetica", 12), bg="#f0f0f0")
        # self.label_lastname.pack(pady=5)
        self.label_lastname = self.create_label(master, "Прізвище:")
        self.entry_lastname = self.create_entry(master)

        # Ім'я
        self.label_firstname = self.create_label(master, "Ім'я")
        self.entry_firstname = self.create_entry(master)

        # По батькові
        self.label_patronymic = self.create_label(master, "По батькові:")
        self.entry_patronymic = self.create_entry(master)

        # Вік
        self.label_age = self.create_label(master, "Вік:")
        self.entry_age = self.create_entry(master)

        # Стать
        self.label_gender = self.create_label(master, "Стать:")
        self.gender_var = tk.StringVar(master)
        self.gender_var.set("Чоловік")  # Значення за замовчуванням
        self.gender_combobox = ttk.Combobox(master, textvariable=self.gender_var, values=["Чоловік", "Жінка"],
                                            font=("Helvetica", 12))
        self.gender_combobox.pack(pady=5, padx=10, ipady=4, fill=tk.X)

        # Примітка
        self.label_notes = self.create_label(master, "Примітка:")
        self.entry_notes = self.create_entry(master)

        # Кнопка "Додати"
        self.submit_button = tk.Button(master, text="Додати", command=self.add_data_to_database,
                                       font=("Helvetica", 14, "bold"), bg="#4CAF50", fg="white")
        self.submit_button.pack(pady=20, ipadx=20, ipady=8)

    def create_label(self, master: tk.Misc | None = None, text: float | str = ...):
        it = tk.Label(master, text=text, font=("Helvetica", 12), bg="#f0f0f0")
        it.pack(pady=5)
        return it

    def create_entry(self, master: tk.Misc | None = None):
        it = tk.Entry(master, font=("Helvetica", 12))
        it.pack(pady=5, padx=10, ipady=4, fill=tk.X)
        return it

    def add_data_to_database(self):
        lastname = self.entry_lastname.get()
        firstname = self.entry_firstname.get()
        patronymic = self.entry_patronymic.get()
        age = self.entry_age.get()
        gender = self.gender_var.get()
        notes = self.entry_notes.get()

        if not all([lastname, firstname, patronymic, age, gender, notes]):
            messagebox.showerror("Помилка", "Будь ласка, заповніть всі поля.")
            return

        try:
            conn = sqlite3.connect("lab02/databases/infodatabase.db")
            cursor = conn.cursor()

            cursor.execute("INSERT INTO infodatabase (lastname, firstname, patronymic, age, gender, notes) VALUES (?, ?, ?, ?, ?, ?)",
                           (lastname, firstname, patronymic, age, gender, notes))

            conn.commit()
            conn.close()
            messagebox.showinfo("Успіх", "Дані успішно додані до бази даних.")
            self.master.destroy()

        except Exception as e:
            messagebox.showerror("Помилка", f"Під час додавання даних виникла помилка: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    add_data_window = AddDataFunction(root)
    root.mainloop()
