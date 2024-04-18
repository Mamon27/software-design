import tkinter as tk
from tkinter import ttk, messagebox
from databases.database import Database
from main_window import MainMenu

class RegisterWindow:
    def __init__(self, master, main_menu):
        self.master = master
        self.main_menu = main_menu
        self.db = Database()

        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.role_var = tk.StringVar()

        self.master.title("Реєстрація")
        self.master.geometry("500x300")

        self.label_username = tk.Label(master, text="Логін:", font=("Arial", 12))
        self.label_username.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_username = tk.Entry(master, textvariable=self.username_var, font=("Arial", 12))
        self.entry_username.grid(row=0, column=1, padx=10, pady=5)

        self.label_password = tk.Label(master, text="Пароль:", font=("Arial", 12))
        self.label_password.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_password = tk.Entry(master, textvariable=self.password_var, show="*", font=("Arial", 12))
        self.entry_password.grid(row=1, column=1, padx=10, pady=5)

        self.label_role = tk.Label(master, text="Роль:", font=("Arial", 12))
        self.label_role.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.role_menu = ttk.Combobox(master, textvariable=self.role_var, values=["Адміністратор", "Користувач", "Бухгалтер"], font=("Arial", 12))
        self.role_menu.grid(row=2, column=1, padx=10, pady=5)

        self.register_button = tk.Button(master, text="Зареєструватися", command=self.on_register, font=("Arial", 12, "bold"), relief=tk.RAISED, bg="lightblue", fg="black", width=20)
        self.register_button.grid(row=3, column=1, pady=10, padx=10, sticky="e")

        self.back_button = tk.Button(master, text="Назад", command=self.on_back, font=("Arial", 12, "bold"), relief=tk.RAISED, bg="lightblue", fg="black", width=20)
        self.back_button.grid(row=3, column=0, pady=10, padx=10, sticky="w")

    def on_register(self):
        username = self.username_var.get()
        password = self.password_var.get()
        role = self.role_var.get()

        if not username or not password or not role:
            messagebox.showerror("Помилка реєстрації", "Будь-ласка, заповніть усі поля")
            return

        success = self.db.create_user(username, password, role)

        if success:
            messagebox.showinfo("Реєстрація успішна", "Користувач успішно доданий")
            self.master.destroy()  # Закрываем окно регистрации
            self.main_menu.open_main_menu()  # Открываем главное меню
        else:
            messagebox.showerror("Помилка реєстрації", "Користувач з таким ім'ям вже зареєстрований")

    def on_back(self):
        self.master.destroy()
        self.main_menu.master.deiconify()

if __name__ == "__main__":
    root = tk.Tk()
    main_menu = MainMenu(root)
    register_window = tk.Toplevel(root)
    register_frame = RegisterWindow(register_window, main_menu)
    root.mainloop()
