import tkinter as tk
from animal_manager import AnimalManager
from enclosure_manager import EnclosureManager
from worker_manager import WorkerManager

class ZooApp:
    def __init__(self, master):
        self.master = master
        self.animals = []
        self.enclosures = []
        self.workers = []
        self.master.geometry("1200x600")
        self.master.title("Управління класами")

        # Создаем кнопки управления для каждого менеджера
        self.button_animals = tk.Button(master, text="Управління тваринами", command=self.show_animal_manager, width=30, height=4)
        self.button_animals.pack()

        self.button_enclosures = tk.Button(master, text="Управління вольєрами", command=self.show_enclosure_manager, width=30, height=4)
        self.button_enclosures.pack()

        self.button_workers = tk.Button(master, text="Управління співробітниками", command=self.show_worker_manager, width=30, height=4)
        self.button_workers.pack()

    def show_animal_manager(self):
        animal_manager = AnimalManager(self.master, self.animals)
        animal_manager.show_manager()

    def show_enclosure_manager(self):
        enclosure_manager = EnclosureManager(self.master, self.enclosures)
        enclosure_manager.show_manager()

    def show_worker_manager(self):
        worker_manager = WorkerManager(self.master, self.workers)
        worker_manager.show_manager()

root = tk.Tk()
app = ZooApp(root)
root.mainloop()
