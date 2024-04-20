import tkinter as tk
from tkinter import messagebox
from function_dashboard.add_data_function import AddDataFunction
from function_dashboard.show_all_function import ShowAllFunction
from function_dashboard.edit_user import EditUser
from function_dashboard.delete_function import DeleteUser
from dialogs.dialog import CustomDialog

class DashboardWindow:
    def __init__(self, master, username, role, db, main_menu):
        self.master = master
        self.username = username
        self.role = role
        self.db = db
        self.main_menu = main_menu

        self.label_username = tk.Label(master, text=f"Логін: {username}", font=("Arial", 12))
        self.label_username.pack(pady=(20, 5))

        self.label_role = tk.Label(master, text=f"Роль: {role}", font=("Arial", 12))
        self.label_role.pack(pady=(5, 10))

        self.add_button = tk.Button(master, text="Додати", command=self.on_add_button_click, font=("Arial", 12, "bold"), relief=tk.RAISED, bg="lightgreen", fg="black", width=20)
        self.add_button.pack(pady=5)

        self.show_all_button = tk.Button(master, text="Показати усіх", command=self.on_show_all_button_click, font=("Arial", 12, "bold"), relief=tk.RAISED, bg="lightgreen", fg="black", width=20)
        self.show_all_button.pack(pady=5)

        self.exit_button = tk.Button(master, text="Вийти", command=self.on_exit_button_click, font=("Arial", 12, "bold"), relief=tk.RAISED, bg="red", fg="black", width=20)
        self.exit_button.pack(side=tk.BOTTOM, padx=20, pady=(0, 20), anchor='se')

    def on_add_button_click(self):
        allowed_roles=["Адміністратор"]
        if self.role in allowed_roles:
            add_data_window = tk.Toplevel(self.master)
            add_data_function = AddDataFunction(add_data_window)
            add_data_window.mainloop()
        else:
             messagebox.showerror("Примітка", "У Вас недостатньо прав")
        
    def on_show_all_button_click(self):
        show_all_window = tk.Toplevel(self.master)
        db_path = "lab02/databases/infodatabase.db"  
        show_all_function = ShowAllFunction(show_all_window, db_path, self.role)
        show_all_function.show_data_from_database()
        show_all_window.mainloop()

    def get_selected_data(self):
        selected_item = self.tree.selection()[0]
        selected_data = self.tree.item(selected_item, 'values')
        return selected_data

    def on_exit_button_click(self):
        self.master.destroy() 
        self.main_menu.master.deiconify()

if __name__ == "__main__":
    root = tk.Tk()
    root.mainloop()
