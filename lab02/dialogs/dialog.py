import tkinter as tk
from tkinter import messagebox
from function_dashboard.delete_function import DeleteUser

class CustomDialog(tk.Toplevel):
    def __init__(self, parent, role, callback=None, instance=None):
        tk.Toplevel.__init__(self, parent)
        self.title("Вибір")
        self.geometry("400x150")
        self.role = role
        self.callback = callback
        self.instance = instance

        self.label = tk.Label(self, text="Оберіть дію:", font=("Arial", 12))
        self.label.pack(pady=10)

        self.edit_button = tk.Button(self, text="Редагувати", command=self.on_edit, font=("Arial", 10, "bold"), relief=tk.RAISED, bg="lightblue", fg="black")
        self.edit_button.pack(side="left", padx=(20, 10))

        self.delete_button = tk.Button(self, text="Видалити", command=self.on_delete, font=("Arial", 10, "bold"), relief=tk.RAISED, bg="lightcoral", fg="black")
        self.delete_button.pack(side="left")

        self.cancel_button = tk.Button(self, text="Назад", command=self.on_cancel, font=("Arial", 10, "bold"), relief=tk.RAISED, bg="lightgreen", fg="black")
        self.cancel_button.pack(side="right", padx=(10, 20))

        self.user_choice = None

    def on_edit(self):
        if self.role == "Адміністратор":
            self.user_choice = 'edit'
            self.destroy()
        else:
            messagebox.showerror("Помилка", "У вас недостатньо прав")

    def on_delete(self):
        if self.role == "Адміністратор":
            confirm = messagebox.askyesno("Підтвердження", "Ви впевнені, що хочете видалити цей запис?")
            if confirm:
                if self.callback:
                    self.user_choice = 'delete'
                    self.destroy()
                    self.callback(self.role) 
                else:
                    messagebox.showerror("Помилка", "Не вказано функцію зворотного виклику для видалення")
        else:
            messagebox.showerror("Помилка", "У вас недостатньо прав")


    def on_cancel(self):
        self.user_choice = 'cancel'
        self.destroy()