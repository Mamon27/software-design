import tkinter as tk
from tkinter import messagebox
from databases.database import Database
from main_window import MainMenu
from dashboard_window import DashboardWindow

class LoginWindow:
    def __init__(self, master, main_menu):
        self.master = master
        self.main_menu = main_menu
        self.db = Database()

        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

        self.label_username = tk.Label(master, text="Логін:", font=("Arial", 12))
        self.label_username.grid(row=0, column=0, sticky="e")

        self.entry_username = tk.Entry(master, textvariable=self.username_var, font=("Arial", 12))
        self.entry_username.grid(row=0, column=1)

        self.label_password = tk.Label(master, text="Пароль:", font=("Arial", 12))
        self.label_password.grid(row=1, column=0, sticky="e")

        self.entry_password = tk.Entry(master, textvariable=self.password_var, show="*", font=("Arial", 12))
        self.entry_password.grid(row=1, column=1)

        self.login_button = tk.Button(master, text="Увійти", command=self.on_login, font=("Arial", 12, "bold"), relief=tk.RAISED, bg="lightblue", fg="black", width=20)
        self.login_button.grid(row=2, column=1, pady=10)

        self.back_button = tk.Button(master, text="Назад", command=self.on_back, font=("Arial", 12, "bold"), relief=tk.RAISED, bg="lightblue", fg="black", width=20)
        self.back_button.grid(row=2, column=0, pady=10)

    def on_login(self):
        username = self.username_var.get()
        password = self.password_var.get()

        if not username or not password:
            messagebox.showerror("Зверніть увагу", "Будь ласка, введіть ім'я користувача та пароль")
            return

        user_data = self.db.fetch_user(username, password)

        if user_data:
            role = user_data[0][3]  # Assuming the role is at index 3
            self.show_dashboard(username, role)
        else:
            messagebox.showerror("Зверніть увагу", "Невірне ім'я користувача або пароль")

    def show_dashboard(self, username, role):
        self.master.withdraw()  # Скрываем окно входа
        dashboard_window = tk.Toplevel()  # Создаем новое окно
        dashboard_window.title("Dashboard")
        dashboard_window.geometry("800x600")
        dashboard_frame = DashboardWindow(dashboard_window, username, role, self.db, self.main_menu)  # Передаем экземпляр MainMenu в DashboardWindow
        dashboard_window.protocol("WM_DELETE_WINDOW", lambda: self.on_dashboard_close(dashboard_window))  # Устанавливаем обработчик закрытия окна

    def on_dashboard_close(self, dashboard_window):
        dashboard_window.destroy()  # Закрываем текущее окно Dashboard
        self.main_menu.master.deiconify()  # Восстанавливаем видимость главного меню

    def on_back(self):
        self.master.destroy()
        self.main_menu.master.deiconify()
