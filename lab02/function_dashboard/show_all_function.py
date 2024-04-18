import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
from function_dashboard.edit_user import EditUser
from function_dashboard.delete_function import DeleteUser
from dialogs.dialog import CustomDialog

class ShowAllFunction:
    def __init__(self, master, db_path, role):
        self.master = master
        self.db_path = db_path
        self.role = role
        self.action_dialog = None
        
        self.master.title("Показати всі дані")
        self.master.geometry("800x600")

        self.tree = ttk.Treeview(master, columns=("ID" , "Прізвище", "Ім'я", "По батькові", "Вік", "Стать", "Примітка"))

        self.tree.heading("#0", text="ID")
        self.tree.heading("#1", text="ID")
        self.tree.heading("#2", text="Прізвище")
        self.tree.heading("#3", text="Ім'я")
        self.tree.heading("#4", text="По батькові")
        self.tree.heading("#5", text="Вік")
        self.tree.heading("#6", text="Стать")
        self.tree.heading("#7", text="Примітка")

        self.tree.column("#0", width=0, stretch=False)
        self.tree.column("#1", width=100, anchor="center")
        self.tree.column("#2", width=100, anchor="center")
        self.tree.column("#3", width=100, anchor="center")
        self.tree.column("#4", width=50, anchor="center")
        self.tree.column("#5", width=80, anchor="center")
        self.tree.column("#6", width=150, anchor="center")
        self.tree.column("#7", width=150, anchor="center")
        
        self.scroll_y = ttk.Scrollbar(master, orient="vertical", command=self.tree.yview)
        self.scroll_y.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=self.scroll_y.set)

        self.show_data_from_database()

        self.tree.pack(expand=True, fill="both")

        self.tree.bind("<Double-1>", self.on_double_click)

    def show_data_from_database(self):
        self.tree.delete(*self.tree.get_children())  
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, lastname, firstname, patronymic, age, gender, notes FROM infodatabase")
        rows = cursor.fetchall()
        for row in rows:
            values = row[0], *row[1:]
            self.tree.insert("", "end", values=row)
        conn.close()

    def on_double_click(self, event):
        selected_item = self.tree.selection()[0]
        selected_data = self.tree.item(selected_item, 'values')

        self.action_dialog = CustomDialog(self.master, self.role, self.delete_callback)  # передаем callback-функцию для удаления
        self.master.wait_window(self.action_dialog)

        if self.action_dialog and self.action_dialog.user_choice == 'edit':
            edit_data_window = tk.Toplevel(self.master)
            edit_data_function = EditUser(edit_data_window, selected_data[0], self.db_path)
            edit_data_window.mainloop()

    def delete_callback(self, role):
        # Эта функция будет вызываться при нажатии кнопки "Видалити" в диалоговом окне
        # Здесь можно вызвать функцию удаления данных из базы данных
        if role == "Адміністратор":
            selected_item = self.tree.selection()[0]
            selected_data = self.tree.item(selected_item, 'values')
            delete_data_function = DeleteUser(selected_data[0], self.db_path, self.tree, selected_item, role)
            delete_data_function.delete_user()  # вызываем метод delete_user для удаления данных

if __name__ == "__main__":
    root = tk.Tk()
    show_all_window = ShowAllFunction(root, "lab02/databases/infodatabase.db", "Адміністратор")
    root.mainloop()
