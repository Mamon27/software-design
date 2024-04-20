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
        self.label_lastname = tk.Label(master, text="Прізвище:", font=("Helvetica", 12), bg="#f0f0f0")
        self.label_lastname.pack(pady=5)
        self.entry_lastname = tk.Entry(master, font=("Helvetica", 12))
        self.entry_lastname.pack(pady=5, padx=10, ipady=4, fill=tk.X)

        # Ім'я
        self.label_firstname = tk.Label(master, text="Ім'я:", font=("Helvetica", 12), bg="#f0f0f0")
        self.label_firstname.pack(pady=5)
        self.entry_firstname = tk.Entry(master, font=("Helvetica", 12))
        self.entry_firstname.pack(pady=5, padx=10, ipady=4, fill=tk.X)

        # По батькові
        self.label_patronymic = tk.Label(master, text="По батькові:", font=("Helvetica", 12), bg="#f0f0f0")
        self.label_patronymic.pack(pady=5)
        self.entry_patronymic = tk.Entry(master, font=("Helvetica", 12))
        self.entry_patronymic.pack(pady=5, padx=10, ipady=4, fill=tk.X)

        # Вік
        self.label_age = tk.Label(master, text="Вік:", font=("Helvetica", 12), bg="#f0f0f0")
        self.label_age.pack(pady=5)
        self.entry_age = tk.Entry(master, font=("Helvetica", 12))
        self.entry_age.pack(pady=5, padx=10, ipady=4, fill=tk.X)

        # Стать
        self.label_gender = tk.Label(master, text="Стать:", font=("Helvetica", 12), bg="#f0f0f0")
        self.label_gender.pack(pady=5)
        self.gender_var = tk.StringVar(master)
        self.gender_var.set("Чоловік")  # Значення за замовчуванням
        self.gender_combobox = ttk.Combobox(master, textvariable=self.gender_var, values=["Чоловік", "Жінка"], font=("Helvetica", 12))
        self.gender_combobox.pack(pady=5, padx=10, ipady=4, fill=tk.X)

        # Примітка
        self.label_notes = tk.Label(master, text="Примітка:", font=("Helvetica", 12), bg="#f0f0f0")
        self.label_notes.pack(pady=5)
        self.entry_notes = tk.Entry(master, font=("Helvetica", 12))
        self.entry_notes.pack(pady=5, padx=10, ipady=4, fill=tk.X)

        # Кнопка "Додати"
        self.submit_button = tk.Button(master, text="Додати", command=self.add_data_to_database, font=("Helvetica", 14, "bold"), bg="#4CAF50", fg="white")
        self.submit_button.pack(pady=20, ipadx=20, ipady=8)

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
