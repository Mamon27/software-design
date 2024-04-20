# Система управління інформацією

:penguin:
# Вміст

- [Запуск](#запуск)
- [Опис](#опис)
- [Структура проекту](#структура-проекту)
- [Патерни](#патерни)
- [Принципи](#принципи)
  

  

# Запуск

1. Встановіть Python.
2. Запустіть файл `main.py`.

```bash
main.py 
```
# Опис 

- Ця програма реалізує систему управління інформацією, яка дозволяє користувачам додавати, переглядати, редагувати та видаляти інформацію враховуючи їх роль яку Ви вказуєте при реєстрації. 
-  Також є можливість реєстрації користувача (поки примітивно)
-  Можливість входу в обліковий запис (поки примітивно)
# Структура проекту

- **main.py**: Файл для запуску програми.

- **register_window**: створює вікно для реєстрації нового користувача. Він містить поля для введення логіну, паролю та ролі користувача, а також кнопку для реєстрації. Після успішної реєстрації та кнопку назад , яка повертає Вас назад у головне вікно. 

- **login_window.py**: творює вікно для входу в програму. Він містить поля для введення логіну та паролю, а також кнопку для входу в програму. Після введення коректних даних користувачу надається доступ до головного вікна програми.

- **main_window.py**: Файл відповідає за створення головного вікна програми для входу  та реєстрації користувача. Він містить графічний інтерфейс  з кнопками для переходу до різних функцій програми, таких як Логін та Реєстрація.

- **dashboard_window.py** Цей файл створює вікно для додавання нового користувача до бази даних. Він містить кнопки які в свою чергу виконують різні функції.
  
- **add_data_function.py** Створює вікно для додавання нового користувача до бази даних. Він містить поля для введення даних користувача, таких як прізвище, ім'я, вік тощо, а також кнопку для додавання користувача.
  
- **show_all_function.py** створює вікно для відображення списку всіх користувачів з бази даних. Він містить таблицю з даними користувачів та кнопки для редагування та видалення користувачів. ***Для редагуваня чи видалення інформації потрібно зробити даблклік по обраному рядку.***
  
- **edit_user.py** Створює вікно для редагування даних конкретного користувача. Він містить поля для зміни даних користувача, таких як прізвище, ім'я, вік тощо, а також кнопку для збереження змін.
  
- **delete_function.py** Надає можливість видалити користувача з бази даних. Він містить метод для видалення користувача за його ідентифікатором.
  
- **dialog.py** Модуль dialog.py містить клас CustomDialog, який створює спеціальне вікно для вибору операцій, таких як редагування або видалення користувача. Також присутня кнопка назад.

# Патерни
## Factroy Method
Взаємодія між між графічними інтерфейсами вікон входу, реєстрації з вікном входу.
```python
def open_login_window(self):
        self.master.withdraw()
        login_window = tk.Toplevel(self.master)
        login_window.title("Вхід")
        login_window.geometry("800x600")

        from login_window import LoginWindow
        login_frame = LoginWindow(login_window, self)  
```
```python
def open_register_window(self):
        self.master.withdraw()
        register_window = tk.Toplevel(self.master)
        register_window.title("Реєстрація")
        register_window.geometry("800x600")

        from register_window import RegisterWindow
        register_frame = RegisterWindow(register_window, self)
```
## Command
Використувується клас CustomDialog для оброки команд.Присутній вибір таких команд у цьому класі як редагування, виделаення та відміна. Та інші функції у інших класах.
```python
def add_data_to_database(self):
        lastname = self.entry_lastname.get()
        firstname = self.entry_firstname.get()
        patronymic = self.entry_patronymic.get()
        age = self.entry_age.get()
        gender = self.gender_var.get()
        notes = self.entry_notes.get()

        if not all([lastname, firstname, patronymic, age, gender, notes]):
            messagebox.showerror("Помилка", "Будь ласка, заповніть всі поля.")
            return

        try:
            conn = sqlite3.connect("lab02/databases/infodatabase.db")
            cursor = conn.cursor()

            cursor.execute("INSERT INTO infodatabase (lastname, firstname, patronymic, age, gender, notes) VALUES (?, ?, ?, ?, ?, ?)",
                           (lastname, firstname, patronymic, age, gender, notes))

            conn.commit()
            conn.close()
            messagebox.showinfo("Успіх", "Дані успішно додані до бази даних.")
            self.master.destroy()

        except Exception as e:
            messagebox.showerror("Помилка", f"Під час додавання даних виникла помилка: {str(e)}")
```
```python
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
```

## Command
Використовується методи які відповідають за конкретну команду 
```python
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

```
# Принципи
Використовуются основні принципи SOLID 
## Принцип єдиного обов'язку (SRP):
Класи мають тільки ті функції які від них очкікує користувач ( ну наскілкьи це можливо на даному етапі)
## Принцип відкритості/закритості (OCP)
Присутня можливість доповненя окремих частин коду, це не буде впливати на роботи інших частин коду.
## Принцип розділення інтерфейсу (ISP)
Присутній клас EditUser ,який використовується тільки тоді, коли це потрібно.
## Fail Fast
Присутня перевірка та діалогові вікна з текстом про помилку
Приклади:
```python
if gender.lower() not in ("чоловік", "жінка"):
            messagebox.showerror("Помилка", "Стать повинна бути 'чоловік' або 'жінка'")
            return
```
```python
def on_edit(self):
        if self.role == "Адміністратор":
            self.user_choice = 'edit'
            self.destroy()
        else:
            messagebox.showerror("Помилка", "У вас недостатньо прав")
```
```python
def on_add_button_click(self):
        allowed_roles=["Адміністратор"]
        if self.role in allowed_roles:
            add_data_window = tk.Toplevel(self.master)
            add_data_function = AddDataFunction(add_data_window)
            add_data_window.mainloop()
        else:
             messagebox.showerror("Примітка", "У Вас недостатньо прав")
```
## KISS
На даному етапі особливо лишнього немає.
Наприклад у вікні додавання інформації є кнопка додати та поля ввода даннх , які можна прибрати або розширити за потреби.

## YAGNI 
Елементи інтерфейсу не використовуються без потреби та не розширяються наперед. Всі функції використовуються окремо ( додавання, редагування, видалення., тощо.)
```python
def open_add_data_window(self):
    add_data_window = tk.Toplevel(self.master)
    add_data_window.title("Додати користувача")
    add_data_window.geometry("800x600")

    from add_data_function import AddDataWindow
    add_data_frame = AddDataWindow(add_data_window, self.role)
```
```python
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
```
```python
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
```
```python
def on_double_click(self, event):
        selected_item = self.tree.selection()[0]
        selected_data = self.tree.item(selected_item, 'values')

        self.action_dialog = CustomDialog(self.master, self.role, self.delete_callback)  
        self.master.wait_window(self.action_dialog)

        if self.action_dialog and self.action_dialog.user_choice == 'edit':
            edit_data_window = tk.Toplevel(self.master)
            edit_data_function = EditUser(edit_data_window, selected_data[0], self.db_path)
            edit_data_window.mainloop()
```