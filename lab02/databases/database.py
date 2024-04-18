import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        );
        """
        self.conn.execute(query)
        self.conn.commit()

    def user_exists(self, username):
        try:
            query = "SELECT * FROM users WHERE username=?;"
            cursor = self.conn.execute(query, (username,))
            return cursor.fetchone() is not None
        except sqlite3.Error as e:
            print(f"Error checking if user exists: {e}")
            return False

    def create_user(self, username, password, role):
        try:
            if self.user_exists(username):
                print(f"Пользователь с именем '{username}' уже существует.")
                return False

            query = "INSERT INTO users (username, password, role) VALUES (?, ?, ?);"
            self.conn.execute(query, (username, password, role))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error creating user: {e}")
            return False

    def fetch_user(self, username, password):
        try:
            query = "SELECT * FROM users WHERE username=? AND password=?;"
            cursor = self.conn.execute(query, (username, password))
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error fetching user: {e}")
            return []
