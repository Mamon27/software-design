import tkinter as tk
from tkinter import messagebox
from dashboard_window import DashboardWindow

class MainMenu:
    def __init__(self, master):
        self.master = master
        self.master.geometry("800x600")
        self.master.title("Головне меню")

        self.login_button = tk.Button(master, text="Вхід", command=self.open_login_window, font=("Arial", 12, "bold"), relief=tk.RAISED, bg="lightgreen", fg="black", width=20)
        self.login_button.pack(pady=20, side=tk.TOP)

        self.register_button = tk.Button(master, text="Реєстрація", command=self.open_register_window, font=("Arial", 12, "bold"), relief=tk.RAISED, bg="lightgreen", fg="black", width=20)
        self.register_button.pack(side=tk.TOP)

    def open_login_window(self):
        self.master.withdraw()
        login_window = tk.Toplevel(self.master)
        login_window.title("Вхід")
        login_window.geometry("800x600")

        from login_window import LoginWindow
        login_frame = LoginWindow(login_window, self)  

    def open_register_window(self):
        self.master.withdraw()
        register_window = tk.Toplevel(self.master)
        register_window.title("Реєстрація")
        register_window.geometry("800x600")

        from register_window import RegisterWindow
        register_frame = RegisterWindow(register_window, self)

    def open_main_menu(self):
        self.master.deiconify()

if __name__ == "__main__":
    root = tk.Tk()
    main_menu = MainMenu(root)
    root.mainloop()
