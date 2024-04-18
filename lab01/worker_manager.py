import tkinter as tk
from tkinter import simpledialog, messagebox, ttk


class WorkerManager:
    def __init__(self, master, workers):
        self.master = master
        self.workers = workers
        

    def show_manager(self):
        self.worker_window = tk.Toplevel(self.master)
        self.worker_window.title("Управління співробітниками")
        self.worker_window.geometry("400x300")

        self.button_add = tk.Button(self.worker_window, text="Додати", command=self.add_worker, width=15)
        self.button_add.pack(pady=5)

        self.button_show = tk.Button(self.worker_window, text="Показати усіх", command=self.display_all_workers, width=15)
        self.button_show.pack(pady=5)

        self.button_remove = tk.Button(self.worker_window, text="Видалити усіх", command=self.remove_all_workers, width=15)
        self.button_remove.pack(pady=5)

    def add_worker(self):
        add_worker_window = tk.Toplevel(self.worker_window)
        add_worker_window.title("Додати співробітника")
        add_worker_window.geometry("300x200")

        self.add_worker_entry = tk.Entry(add_worker_window)
        self.add_worker_entry.pack(pady=5)

        age_options = [str(age) for age in range(18, 61)]
        self.age_var = tk.StringVar(add_worker_window)
        self.age_var.set(age_options[0])
        age_combobox = ttk.Combobox(add_worker_window, textvariable=self.age_var, values=age_options, state="readonly")
        age_combobox.pack(pady=5)

        profession_options = ["Доглядальник", "Годувальник", "Ветеринар"]
        self.profession_var = tk.StringVar(add_worker_window)
        self.profession_var.set(profession_options[0])
        profession_combobox = ttk.Combobox(add_worker_window, textvariable=self.profession_var, values=profession_options, state="readonly")
        profession_combobox.pack(pady=5)

        button_confirm = tk.Button(add_worker_window, text="Додати", command=self.confirm_add_worker, width=15)
        button_confirm.pack(pady=5)

    def confirm_add_worker(self):
        name = self.add_worker_entry.get()
        age = self.age_var.get()
        profession = self.profession_var.get()
        if name:
            worker_info = f"Співробітник: {name}, Вік: {age}, Професія: {profession}"
            self.workers.append(worker_info)
            messagebox.showinfo("Успішно", "Свіпробітника додано")
            self.worker_window.destroy()

    def display_all_workers(self):
        if self.workers:
            display_workers_window = tk.Toplevel(self.master)
            display_workers_window.title("Усі співробітники")
            display_workers_window.geometry("400x300")

            for worker in self.workers:
                label_worker = tk.Label(display_workers_window, text=worker)
                label_worker.pack()
        else:
            messagebox.showinfo("Порожньо", "Немає доданих співробітників")

    def remove_all_workers(self):
        if self.workers:
            confirmation = messagebox.askyesno("Видалення", "Ви впевнені?")
            if confirmation:
                self.workers.clear()
                messagebox.showinfo("Успішно", "Усі співробітники видалені!")
        else:
            messagebox.showinfo("Порожньо", "Немає співробітників для видалення")
