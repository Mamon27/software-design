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
python zoo_app.py 
```
# Опис 
- Цей додаток для ведення списку співробітників, тварин та вольєрів у зоопарку
# Структура проекту
  ### Структура проекту
- **animal.py**: Містить клас `Animal`, який представляє тварин в зоопарку.

- **dialog.py**: Містить клас `DataEntryDialog`, використовується для відображення діалогових вікон введення даних.

- **enclosure.py**: Містить клас `Enclosure`, представлення вольєрів у зоопарку.

- **worker.py**: Містить клас `Worker`, який представляє співробітників зоопарку.

- **zoo_app.py**: Основний файл з класом `ZooApp`, який взаємодіє з графічним інтерфейсом.

# Принципи
### KISS 
#### Простий метод для виведення інформації про всіх співробітників
```python
def display_all_workers(self):
    self.listbox_workers.delete(0, tk.END)
    for worker in self.workers:
        self.listbox_workers.insert(tk.END, str(worker))
```
### DRY 
 #### У класі ZooApp код для додавання, видалення і відображення працівників, тварин і вольєрів структурований як окремі методи (add_worker, remove_all_workers і т. д.). Це допомагає підтримувати чистий і не повторюваний код.
```python
def remove_entity(entity_list, listbox):
    selected_index = listbox.curselection()
    if selected_index:
        selected_entity = entity_list.pop(selected_index[0])
        listbox.delete(selected_index)
        print(f"{selected_entity.__class__.__name__} видалено: {selected_entity}")
```
### YAGNI
 #### Тільки функції
### Fail Fast
 #### Присутня перевірка наявності значення перед використанням
```python
 def confirm(self):
        if not self.entry_var.get():
            self.prompt_label.config(text="Вкажіть дані", fg="red")
        else:
            self.result = {
                'name': self.entry_var.get(),
                'type': self.type_combobox.get() if hasattr(self, 'type_combobox') else None
            }
            self.destroy()
```
### Program to Interfaces not Implementations
 #### Присутнє використання DataEntryDialog
```python
class DataEntryDialog(tk.Toplevel):
    def __init__(self, master, prompt, title, choices=None):
        super().__init__(master)
        self.title(title)

        self.prompt_label = tk.Label(self, text=prompt, font=("Arial", 12, "bold"))
        self.prompt_label.pack(pady=10)

        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.entry_var, font=("Arial", 12))
        self.entry.pack(pady=10)

        if choices:
            self.type_label = tk.Label(self, text="Виберіть тип:", font=("Arial", 12, "bold"))
            self.type_label.pack(pady=5)

            self.type_combobox = ttk.Combobox(self, values=choices, font=("Arial", 12))
            self.type_combobox.pack(pady=5)

        self.confirm_button = tk.Button(self, text="Підтвердити", command=self.confirm, font=("Arial", 12, "bold"), bd=5, width=15)
        self.confirm_button.pack(pady=10)
```
### Composition Over Inheritance
 #### Клас ZooApp складається з окремих класів Worker, Animal, Enclosure, а не успадковує їх.
 ```python
class ZooApp:
    def __init__(self, master):

    def add_worker(self):
        #
    def add_animal(self):
        #
    def add_enclosure(self):
        #
 ```
### SOLID
 #### ***Single Responsibility Principle***
- Class 'Animal'
- Class 'Worker'
- Class 'Enclosure'

___Усі ці класи в подальшому можуть стати окремеми класами у зв'язку з розширенням функіоналу___

 #### ***Open/Closed Principle***
  ```python
 types = ['Птахи', 'Рептилії', 'Хижаки']  
dialog = DataEntryDialog(self.master, "Введіть ім'я тварини", "Додавання тварини", choices=types)
 ```
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
 #### __ZooApp використовує класи Worker, Animal, Enclosure через абстракцію.__
 ```python
def add_animal(self):
    types = ['Птахи', 'Рептилії', 'Хижаки']  
    dialog = DataEntryDialog(self.master, "Введіть ім'я тварини", "Додавання тварини", choices=types)
    self.master.wait_window(dialog)
    if dialog.result:
        animal = Animal(dialog.result['name'], dialog.result['species'], dialog.result['type'])
        self.animals.append(animal)
        self.listbox_animals.insert(tk.END, str(animal))
```
# Тест
  - Для тестування програми запустіть файл `zoo_test.py`
  ### Опис тесту
  Цей тест перевіряє функціонал додавання співробітника до програми. Використовує механізм mock для імітації діалогового вікна та отримання імені нового співробітника. Тест перевіряє, чи правильно додано співробітника до списку.
