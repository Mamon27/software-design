# Зоопарк

:penguin:
# Вміст

- [Запуск](#запуск)
- [Опис](#опис)
- [Структура проекту](#структура-проекту)
- [Принципи](#принципи)
- [Тест](#тест)
  

# Запуск

1. Встановіть Python.
2. Запустіть файл `zoo_app.py`.

```bash
zoo_app.py 
```
# Опис 
- Ця програма реалізує систему упраління різними класами, таких як:(Тварини, Співробітники, Вольєри)
-  
# Структура проекту
  ### Структура проекту
- **animal_manager.py**: Містить клас `AnimalManager`, який представляє тварин в зоопарку.

- **enclosure_manger.py**: Містить клас `EnclosureManager`, представлення вольєрів у зоопарку.

- **worker_manager.py**: Містить клас `WorkerManager`, який представляє співробітників зоопарку.

- **zoo_app.py**: Основний файл з класом `ZooApp`, який взаємодіє з графічним інтерфейсом.


# Принципи
### KISS 
#### Простий метод для виведення інформації про всіх співробітників, та кнопки для полегшення користування.
```python
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
```
```python
self.button_animals = tk.Button(master, text="Управління тваринами", command=self.show_animal_manager, width=30, height=4)
        self.button_animals.pack()
```
### DRY 
 #### У класах AnimalManager та інших код для додавання, видалення і відображення працівників, тварин і вольєрів структурований як окремі методи (add_worker, remove_all_workers і т. д.). 
```python
def add_enclosure(self):
        add_enclosure_window = tk.Toplevel(self.enclosure_window)
        add_enclosure_window.title("Додати вольєр")
        add_enclosure_window.geometry("300x200")

        self.add_enclosure_entry = tk.Entry(add_enclosure_window)
        self.add_enclosure_entry.pack(pady=5)

        size_options = ["Маленький", "Середній", "Великий"]
        self.size_var = tk.StringVar(add_enclosure_window)
        self.size_var.set(size_options[0])
        size_combobox = ttk.Combobox(add_enclosure_window, textvariable=self.size_var, values=size_options, state="readonly")
        size_combobox.pack(pady=5)

        button_confirm = tk.Button(add_enclosure_window, text="Додати", command=self.confirm_add_enclosure, width=15)
        button_confirm.pack(pady=5)
```
### YAGNI
 - У Класах присутні тільки ті методи які потрібні на даному етапі, можливо розширити новим функіоналом , не змініючи даний код.
### Fail Fast
 - Присутня перевірка наявності значення перед використанням
```python
 def remove_all_animals(self):
        if self.animals:
            confirmation = messagebox.askyesno("Видалення тварин", "Ви впевнені, що бажаєте видалити усіх тварин?")
            if confirmation:
                self.animals.clear()
                messagebox.showinfo("Успішно", "Усі тварини видалені")
        else:
            messagebox.showinfo("Пусто", "Немає доступних тварин для видалення")    
```
### Program to Interfaces not Implementations
 - Присутнє використання інтерфейсів з інших класів

### Composition Over Inheritance
 - Клас ZooApp містить об'єкти класів 
 ```python
def show_animal_manager(self):
        animal_manager = AnimalManager(self.master, self.animals)
        animal_manager.show_manager()

    def show_enclosure_manager(self):
        enclosure_manager = EnclosureManager(self.master, self.enclosures)
        enclosure_manager.show_manager()

    def show_worker_manager(self):
        worker_manager = WorkerManager(self.master, self.workers)
        worker_manager.show_manager()
 ```
### SOLID
 #### ***Single Responsibility Principle***
- Class 'AnimalManager'
- Class 'WorkerManager'
- Class 'EnclosureManager'

    Окремі класи з методами які відносяться тільки до своїх класів.


 #### ***Open/Closed Principle***
  ```python
 def confirm_add_animal(self):
        name = self.add_animal_entry.get()
        species = self.species_var.get()
        if name:
            animal_info = f"Тварина: {name}, Вид: {species}"
            self.animals.append(animal_info)
            messagebox.showinfo("Успішно", "Тварина успішно додана!")
            self.animal_window.destroy()
 ```
 Кожний клас можливо доповнити новими функціями , за потреби ( все залежить від кінцевого результату який Ви бажаєте отримати )
 #### ***Liskov Substitution Principle***
 #### ***Interface Segregation Principle***
  ```python
def confirm(self):
    if not self.entry_var.get():
        self.prompt_label.config(text="Вкажіть дані", fg="red")
    else:
        self.result = {
            'name': self.entry_var.get(),
            'species': self.type_combobox.get() if hasattr(self, 'type_combobox') else None,
            'type': self.type_combobox.get() if hasattr(self, 'type_combobox') else None
        }
        self.destroy()
 ```
 #### ***Dependency Inversion Principle***
 - Передаються аргументи у конструктор
 

# Тест
  - Для тестування програми запустіть файл `zoo_test.py`
  ### Опис тесту
  Цей тест перевіряє функціонал додавання тварини до програми. Використовує механізм mock для імітації діалогового вікна та отримання імені новоЇ тварини. Тест перевіряє, чи правильно додано тварину до списку.
