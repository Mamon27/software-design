import tkinter as tk
from tkinter import simpledialog
from tkinter import ttk
from worker import Worker
from animal import Animal
from enclosure import Enclosure
from dialog import DataEntryDialog

class ZooApp:
    def __init__(self, master):
        self.master = master
        master.title("Зоопарк")
        master.geometry("1200x600")

        self.zoo = []
        self.workers = []
        self.animals = []
        self.enclosures = []

        self.label = tk.Label(master, text="Зоопарк", font=("Arial", 30, "bold"))
        self.label.pack()

        self.frame_workers = tk.Frame(master)
        self.frame_workers.pack(side=tk.LEFT, padx=20)

        self.label_workers = tk.Label(self.frame_workers, text="Співробітники:", font=("Arial", 14, "bold"))
        self.label_workers.pack()

        self.listbox_workers = tk.Listbox(self.frame_workers, width=40, height=10, font=("Arial", 12))
        self.listbox_workers.pack(pady=10)

        self.button_add_worker = tk.Button(self.frame_workers, text="Додати співробітника", command=self.add_worker, font=("Arial", 12, "bold"), bd=5, width=30)
        self.button_add_worker.pack(pady=10)

        self.button_remove_all_workers = tk.Button(self.frame_workers, text="Видалити всіх співробітників", command=self.remove_all_workers, font=("Arial", 12, "bold"), bd=5, width=30)
        self.button_remove_all_workers.pack(pady=10)

        self.button_display_info = tk.Button(self.frame_workers, text="Показати всіх співробітників", command=self.display_all_workers, font=("Arial", 12, "bold"), bd=5, width=30)
        self.button_display_info.pack(pady=10)

        self.button_remove_selected_worker = tk.Button(self.frame_workers, text="Видалити вибраного співробітника", command=self.remove_selected_worker, font=("Arial", 12, "bold"), bd=5, width=30)
        self.button_remove_selected_worker.pack(pady=10)

        self.frame_animals = tk.Frame(master)
        self.frame_animals.pack(side=tk.LEFT, padx=20)

        self.label_animals = tk.Label(self.frame_animals, text="Тварини:", font=("Arial", 14, "bold"))
        self.label_animals.pack()

        self.listbox_animals = tk.Listbox(self.frame_animals, width=40, height=10, font=("Arial", 12))
        self.listbox_animals.pack(pady=10)

        self.button_add_animal = tk.Button(self.frame_animals, text="Додати тварину", command=self.add_animal, font=("Arial", 12, "bold"), bd=5, width=30)
        self.button_add_animal.pack(pady=10)

        self.button_remove_all_animals = tk.Button(self.frame_animals, text="Видалити всіх тварин", command=self.remove_all_animals, font=("Arial", 12, "bold"), bd=5, width=30)
        self.button_remove_all_animals.pack(pady=10)

        self.button_display_animals = tk.Button(self.frame_animals, text="Показати всіх тварин", command=self.display_all_animals, font=("Arial", 12, "bold"), bd=5, width=30)
        self.button_display_animals.pack(pady=10)

        self.button_remove_selected_animal = tk.Button(self.frame_animals, text="Видалити вибрану тварину", command=self.remove_selected_animal, font=("Arial", 12, "bold"), bd=5, width=30)
        self.button_remove_selected_animal.pack(pady=10)

        self.frame_enclosures = tk.Frame(master)
        self.frame_enclosures.pack(side=tk.LEFT, padx=20)

        self.label_enclosures = tk.Label(self.frame_enclosures, text="Вольєри:", font=("Arial", 14, "bold"))
        self.label_enclosures.pack()

        self.listbox_enclosures = tk.Listbox(self.frame_enclosures, width=40, height=10, font=("Arial", 12))
        self.listbox_enclosures.pack(pady=10)

        self.button_add_enclosure = tk.Button(self.frame_enclosures, text="Додати вольєр", command=self.add_enclosure, font=("Arial", 12, "bold"), bd=5, width=30)
        self.button_add_enclosure.pack(pady=10)

        self.button_remove_all_enclosures = tk.Button(self.frame_enclosures, text="Видалити всі вольєри", command=self.remove_all_enclosures, font=("Arial", 12, "bold"), bd=5, width=30)
        self.button_remove_all_enclosures.pack(pady=10)

        self.button_display_enclosures = tk.Button(self.frame_enclosures, text="Показати всі вольєри", command=self.display_all_enclosures, font=("Arial", 12, "bold"), bd=5, width=30)
        self.button_display_enclosures.pack(pady=10)

        self.button_remove_selected_enclosure = tk.Button(self.frame_enclosures, text="Видалити вибраний вольєр", command=self.remove_selected_enclosure, font=("Arial", 12, "bold"), bd=5, width=30)
        self.button_remove_selected_enclosure.pack(pady=10)

    def add_worker(self):
        types = ['Робітник', 'Ветеринар', 'Доглядальник']  
        dialog = DataEntryDialog(self.master, "Введіть ім'я співробітника", "Добавлення співробітника", choices=types)
        self.master.wait_window(dialog)
        if dialog.result:
            worker = Worker(dialog.result['name'], dialog.result['species'])
            self.workers.append(worker)
            self.listbox_workers.insert(tk.END, str(worker))

    def remove_all_workers(self):
        self.listbox_workers.delete(0, tk.END)
        self.workers = []

    def display_all_workers(self):
        self.listbox_workers.delete(0, tk.END)
        for worker in self.workers:
            self.listbox_workers.insert(tk.END, str(worker))

    def remove_selected_worker(self):
        selected_index = self.listbox_workers.curselection()
        if selected_index:
            selected_worker = self.workers.pop(selected_index[0])
            self.listbox_workers.delete(selected_index)
            print(f"Співробітник видаленний: {selected_worker}")

    def add_animal(self):
        types = ['Птиці', 'Рептилії', 'Хижаки']  
        dialog = DataEntryDialog(self.master, "Введіть ім'я тварини", "Додавання тварин", choices=types)
        self.master.wait_window(dialog)
        if dialog.result:
            animal = Animal(dialog.result['name'], dialog.result['species'], dialog.result['type'])
            self.animals.append(animal)
            self.listbox_animals.insert(tk.END, str(animal))

    def remove_all_animals(self):
        self.listbox_animals.delete(0, tk.END)
        self.animals = []

    def display_all_animals(self):
        self.listbox_animals.delete(0, tk.END)
        for animal in self.animals:
            self.listbox_animals.insert(tk.END, str(animal))

    def remove_selected_animal(self):
        selected_index = self.listbox_animals.curselection()
        if selected_index:
            selected_animal = self.animals.pop(selected_index[0])
            self.listbox_animals.delete(selected_index)
            print(f"Тварина видалена: {selected_animal}")

    def add_enclosure(self):
        sizes = ['Маленький', 'Середній', 'Великий']  
        dialog = DataEntryDialog(self.master, "Введіть назву вольєра:", "Додавання вольєру", choices=sizes)
        self.master.wait_window(dialog)
        if dialog.result:
            enclosure = Enclosure(dialog.result['name'], dialog.result['type'])
            self.enclosures.append(enclosure)
            self.listbox_enclosures.insert(tk.END, str(enclosure))

    def remove_all_enclosures(self):
        self.listbox_enclosures.delete(0, tk.END)
        self.enclosures = []

    def display_all_enclosures(self):
        self.listbox_enclosures.delete(0, tk.END)
        for enclosure in self.enclosures:
            self.listbox_enclosures.insert(tk.END, str(enclosure))

    def remove_selected_enclosure(self):
        selected_index = self.listbox_enclosures.curselection()
        if selected_index:
            selected_enclosure = self.enclosures.pop(selected_index[0])
            self.listbox_enclosures.delete(selected_index)
            print(f"Вольєр видалений: {selected_enclosure}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ZooApp(root)
    root.mainloop()
