import tkinter as tk
from tkinter import messagebox
import sqlite3

class DeleteUser:
    def __init__(self, user_id, db_path, treeview, selected_item, role):
        self.user_id = user_id
        self.db_path = db_path
        self.treeview = treeview
        self.selected_item = selected_item
        self.role = role
    
    def delete_user(self):
        if self.role == "Адміністратор":
            try:
                conn = sqlite3.connect(self.db_path)
                cursor = conn.cursor()
                cursor.execute("DELETE FROM infodatabase WHERE id=?", (self.user_id,))
                conn.commit()
                conn.close()
                messagebox.showinfo("Успіх", "Дані були успішно видалені!")
                if self.treeview:
                    self.treeview.delete(self.selected_item) 
            except sqlite3.Error as e:
                messagebox.showerror("Помилка", f"Помилка при видаленні: {str(e)}")
        else:
            messagebox.showerror("Помилка", "У вас недостатньо прав")