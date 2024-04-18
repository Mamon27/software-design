import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3

class EditUser:
    def __init__(self, master, user_id, db_path):
        self.master = master
        self.user_id = user_id
        self.db_path = db_path

        # Создаем подключение к базе данных и извлекаем информацию о пользователе по его ID
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT lastname, firstname, patronymic, age, gender FROM infodatabase WHERE id=?", (user_id,))
        user_data = cursor.fetchone()
        conn.close()

        if user_data:
            self.label_lastname = tk.Label(master, text="Прізвище:", font=("Arial", 12))
            self.label_lastname.grid(row=0, column=0, padx=5, pady=5)
            self.entry_lastname = tk.Entry(master, font=("Arial", 12))
            self.entry_lastname.grid(row=0, column=1, padx=5, pady=5)
            self.entry_lastname.insert(0, user_data[0])

            self.label_firstname = tk.Label(master, text="Ім'я:", font=("Arial", 12))
            self.label_firstname.grid(row=1, column=0, padx=5, pady=5)
            self.entry_firstname = tk.Entry(master, font=("Arial", 12))
            self.entry_firstname.grid(row=1, column=1, padx=5, pady=5)
            self.entry_firstname.insert(0, user_data[1])

            self.label_patronymic = tk.Label(master, text="По батькові:", font=("Arial", 12))
            self.label_patronymic.grid(row=2, column=0, padx=5, pady=5)
            self.entry_patronymic = tk.Entry(master, font=("Arial", 12))
            self.entry_patronymic.grid(row=2, column=1, padx=5, pady=5)
            self.entry_patronymic.insert(0, user_data[2])

            self.label_age = tk.Label(master, text="Вік:", font=("Arial", 12))
            self.label_age.grid(row=3, column=0, padx=5, pady=5)
            self.entry_age = tk.Entry(master, font=("Arial", 12))
            self.entry_age.grid(row=3, column=1, padx=5, pady=5)
            self.entry_age.insert(0, user_data[3])

            self.label_gender = tk.Label(master, text="Стать:", font=("Arial", 12))
            self.label_gender.grid(row=4, column=0, padx=5, pady=5)
            self.gender_var = tk.StringVar(master)
            self.gender_var.set(user_data[4])  # Устанавливаем текущее значение пола
            self.gender_combobox = ttk.Combobox(master, textvariable=self.gender_var, values=["Чоловік", "Жінка"])
            self.gender_combobox.grid(row=4, column=1, padx=5, pady=5)

            self.save_button = tk.Button(master, text="Зберегти", command=self.save_changes, font=("Arial", 12, "bold"), relief=tk.RAISED, bg="lightblue", fg="black")
            self.save_button.grid(row=5, column=0, columnspan=2, pady=10)
        else:
            messagebox.showerror("Помилка", f"Користувача з ID {user_id} не знайдено в базі даних.")

    def save_changes(self):
        lastname = self.entry_lastname.get()
        firstname = self.entry_firstname.get()
        patronymic = self.entry_patronymic.get()
        age = self.entry_age.get()
        gender = self.gender_var.get()

        if not lastname or not firstname or not patronymic or not age or not gender:
            messagebox.showerror("Помилка", "Будь ласка, заповніть всі поля")
            return

        try:
            age = int(age)
        except ValueError:
            messagebox.showerror("Помилка", "Вік має бути цілим числом")
            return

        if gender.lower() not in ("чоловік", "жінка"):
            messagebox.showerror("Помилка", "Стать повинна бути 'чоловік' або 'жінка'")
            return

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE infodatabase SET lastname=?, firstname=?, patronymic=?, age=?, gender=? WHERE id=?",
                       (lastname, firstname, patronymic, age, gender, self.user_id))
        conn.commit()
        conn.close()

        messagebox.showinfo("Успіх", "Дані користувача успішно оновлено")
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    edit_user_window = EditUser(root, 1, "lab02/databases/infodatabase.db")
    root.mainloop()
